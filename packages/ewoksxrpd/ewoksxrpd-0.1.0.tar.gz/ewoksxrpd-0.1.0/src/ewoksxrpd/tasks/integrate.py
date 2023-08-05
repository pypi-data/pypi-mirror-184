import json
from contextlib import contextmanager
from numbers import Number
from typing import Optional

import numpy
import h5py
import pyFAI
from ewoksdata.data import nexus
from ewoksdata.data.hdf5.dataset_writer import DatasetWriter

from .worker import persistent_worker
from .utils import xrpd_utils
from .utils import data_utils
from .data_access import TaskWithDataAccess

__all__ = ["Integrate1D", "IntegrateBlissScan"]


class _BaseIntegrate(
    TaskWithDataAccess,
    input_names=["detector", "geometry", "energy"],
    optional_input_names=["mask", "integration_options"],
    register=False,
):
    """The intensity will be normalized to the reference:

    .. code:

        Inorm = I / monitor * reference
    """

    @contextmanager
    def _worker(self):
        options = self._get_pyfai_options()
        with persistent_worker(options) as worker:
            yield worker, options

    def _get_pyfai_options(self) -> dict:
        geometry = data_utils.data_from_storage(self.inputs.geometry)
        xrpd_utils.validate_geometry(geometry)
        integration_options = data_utils.data_from_storage(
            self.inputs.integration_options, remove_numpy=True
        )
        if integration_options:
            config = {**integration_options, **geometry}
        else:
            config = dict(geometry)
        config.setdefault("unit", "2th_deg")
        config["detector"] = data_utils.data_from_storage(self.inputs.detector)
        config["wavelength"] = xrpd_utils.energy_wavelength(self.inputs.energy)
        if not self.missing_inputs.mask and self.inputs.mask is not None:
            config["mask"] = self.get_image(
                data_utils.data_from_storage(self.inputs.mask)
            )
        return config


class Integrate1D(
    _BaseIntegrate,
    input_names=["image"],
    optional_input_names=["monitor", "reference"],
    output_names=["x", "y", "yerror", "xunits", "info"],
):
    """1D integrate a single diffraction pattern.

    The intensity will be normalized to the reference:

    .. code:

        Inorm = I / monitor * reference
    """

    def run(self):
        raw_data = self.get_image(self.inputs.image)
        normalization_factor, monitor, reference = self.get_normalization()

        with self._worker() as (worker, config):
            result = worker.process(raw_data, normalization_factor=normalization_factor)

            self.outputs.x = result.radial
            self.outputs.y = result.intensity
            if result.sigma is None:
                yerror = numpy.full_like(self.outputs.y, numpy.nan)
            else:
                yerror = result.sigma
            self.outputs.yerror = numpy.abs(yerror)
            self.outputs.xunits = result.unit.name

            info = {
                "detector": config["detector"],
                "energy": xrpd_utils.energy_wavelength(config["wavelength"]),
                "geometry": {
                    k: config[k]
                    for k in ["dist", "poni1", "poni2", "rot1", "rot2", "rot3"]
                },
            }
            info["monitor"] = monitor
            info["reference"] = reference
            self.outputs.info = info

    def get_normalization(self) -> tuple:
        # Inorm = I / normalization_factor
        monitor = self.inputs.monitor
        reference = self.inputs.reference
        if data_utils.is_data(reference):
            if not data_utils.is_data(monitor):
                raise ValueError("provide a 'monitor' when providing a 'reference'")
            monitor = self.get_data(monitor)
            reference = self.get_data(reference)
            normalization_factor = monitor / reference
        else:
            if data_utils.is_data(monitor):
                monitor = self.get_data(monitor)
            else:
                monitor = float("nan")
            reference = float("nan")
            normalization_factor = None
        return normalization_factor, monitor, reference


class IntegrateBlissScan(
    _BaseIntegrate,
    input_names=["filename", "scan", "detector_name", "output_filename"],
    optional_input_names=[
        "counter_names",
        "monitor_name",
        "reference",
        "subscan",
        "retry_timeout",
        "retry_period",
        "demo",
    ],
):
    """1D or 2D integrate data from one detector of a single Bliss scan.

    The intensity will be normalized to the reference:

    .. code:

        Inorm = I / monitor * reference
    """

    def run(self):
        with self._worker() as (worker, config):
            if self.inputs.counter_names:
                counter_names = list(self.inputs.counter_names)
            else:
                counter_names = list()
            detector_name = self.inputs.detector_name
            monitor_name = self.get_input_value("monitor_name", None)
            if monitor_name and monitor_name not in counter_names:
                counter_names.append(monitor_name)
            reference = self.get_input_value("reference", None)
            reference_name = None
            if isinstance(reference, str):
                reference_name = reference
                if reference not in counter_names:
                    counter_names.append(reference)
            subscan = self.get_input_value("subscan", None)

            with self.output_context() as outentry:
                dconfig = dict(config)
                dconfig.pop("mask", None)
                outentry[f"{self._nxprocess_name}/configuration/data"] = json.dumps(
                    dconfig
                )
                nxdata = outentry[f"{self._nxprocess_name}/integrated"]
                measurement = outentry["measurement"]
                h5data = None
                h5errors = None
                h5counters = dict()

                for index, ptdata in self.iter_bliss_data(
                    self.inputs.filename,
                    self.inputs.scan,
                    lima_names=[detector_name],
                    counter_names=counter_names,
                    subscan=subscan,
                ):
                    normalization_factor = self.get_normalization(
                        ptdata.get(monitor_name), ptdata.get(reference_name, reference)
                    )
                    image = ptdata[detector_name]
                    if self.inputs.demo:
                        image = image[:-1, :-1]
                    result = worker.process(
                        image, normalization_factor=normalization_factor
                    )
                    if h5data is None:
                        axes = list()
                        if result.intensity.ndim == 2:
                            xname = "azimuth"
                            xunits = "deg"
                            nxdata[xname] = result.azimuthal
                            nxdata[xname].attrs["units"] = xunits
                            axes.append(xname)
                        xname = result.unit.name
                        xunits = result.unit.unit_symbol
                        nxdata[xname] = result.radial
                        nxdata[xname].attrs["units"] = xunits
                        axes.append(xname)

                        nxdata.attrs["signal"] = "data"
                        if result.intensity.ndim == 2:
                            nxdata.attrs["interpretation"] = "image"
                        else:
                            nxdata.attrs["interpretation"] = "spectrum"

                        h5data = DatasetWriter(nxdata, "data")
                        if result.sigma is not None:
                            h5errors = DatasetWriter(nxdata, "data_errors")
                        for name in counter_names:
                            h5counters[name] = DatasetWriter(measurement, name)

                    flush = h5data.add_point(result.intensity)
                    if result.sigma is not None:
                        flush |= h5errors.add_point(result.sigma)
                    for name in counter_names:
                        flush |= h5counters[name].add_point(ptdata[name])
                    if flush:
                        outentry.file.flush()

                if h5data is None:
                    raise RuntimeError("No scan data")
                h5data.flush_buffer()
                if h5errors is not None:
                    h5errors.flush_buffer()

                nxdata["points"] = numpy.arange(h5data.dataset.shape[0])
                nxdata.attrs["axes"] = ["points"] + axes

    def get_normalization(
        self, monitor: Optional[Number], reference: Optional[Number]
    ) -> tuple:
        # Inorm = I / normalization_factor
        if reference is None:
            normalization_factor = None
        else:
            if monitor is None:
                raise ValueError(
                    "provide a 'monitor_name' when providing a 'reference_name'"
                )
            normalization_factor = monitor / reference
        return normalization_factor

    @property
    def _nxprocess_name(self):
        return f"{self.inputs.detector_name}_integrated"

    @contextmanager
    def output_context(self):
        scan = self.inputs.scan
        subscan = self.get_input_value("subscan", 1)
        url = f"silx://{self.inputs.output_filename}?path=/{scan}.{subscan}"
        with super().open_h5item(url, mode="a", create=True) as entry:
            measurement = entry.create_group("measurement")
            measurement.attrs["NX_class"] = "NXcollection"

            process = entry.create_group(self._nxprocess_name)
            process.attrs["NX_class"] = "NXprocess"
            process["program"] = "pyFAI"
            process["version"] = pyFAI.version

            configuration = process.create_group("configuration")
            configuration.attrs["NX_class"] = "NXnote"
            configuration["type"] = "application/json"

            data = process.create_group("integrated")
            data.attrs["NX_class"] = "NXdata"
            nexus.select_default_plot(data)

            yield entry

            url = f"silx://{self.inputs.filename}?path=/{scan}.{subscan}"
            self.link_bliss_scan(entry, url)

            name = f"{self._nxprocess_name}/integrated/data"
            if name in entry:
                entry[f"measurement/{self._nxprocess_name}"] = h5py.SoftLink(
                    entry[name].name
                )
