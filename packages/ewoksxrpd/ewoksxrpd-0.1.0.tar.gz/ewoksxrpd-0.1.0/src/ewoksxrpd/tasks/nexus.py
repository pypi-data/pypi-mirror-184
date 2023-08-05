from typing import Tuple
import h5py
import pyFAI
from silx.io.dictdump import dicttonx

from ewokscore.task import TaskInputError
from ewoksdata.data import nexus

from .utils.xrpd_utils import energy_wavelength
from .utils import data_utils
from .data_access import TaskWithDataAccess


__all__ = ["SaveNexusPattern1D"]


class SaveNexusPattern1D(
    TaskWithDataAccess,
    input_names=[
        "url",
        "x",
        "y",
        "xunits",
    ],
    optional_input_names=["header", "yerror", "metadata", "bliss_scan_url"],
    output_names=["saved"],
):
    def run(self):
        with self.open_h5item(self.inputs.url, mode="a", create=True) as parent:
            self.save_nxprocess(parent)
            self.save_bliss_links(parent)
            self.save_metadata(parent)
        self.outputs.saved = True

    def _get_xunits(self) -> Tuple[str]:
        xunits = data_utils.data_from_storage(self.inputs.xunits, remove_numpy=True)
        tpl = xunits.split("_")
        if len(tpl) != 2:
            raise TaskInputError("xunits")
        return tpl

    def save_bliss_links(self, parent):
        url = data_utils.data_from_storage(
            self.inputs.bliss_scan_url, remove_numpy=True
        )
        if url:
            self.link_bliss_scan(parent, url)
            parent["measurement/diffractogram"] = h5py.SoftLink(
                f"{parent.name}/integrate/diffractogram/data"
            )

    def save_nxprocess(self, parent):
        if "process" in parent:
            del parent["process"]
        nxprocess = parent.create_group("integrate")
        nxprocess.attrs["NX_class"] = "NXprocess"
        nxprocess["program"] = "pyFAI"
        nxprocess["version"] = pyFAI.version
        self.save_configuration(nxprocess)
        self.save_diffractogram(nxprocess)

    def save_diffractogram(self, parent):
        xname, xunits = self._get_xunits()
        x = self.inputs.x
        y = self.inputs.y
        yerror = self.inputs.yerror

        yname = "data"
        if "diffractogram" in parent:
            del parent["diffractogram"]
        nxdata = parent.create_group("diffractogram")
        nxdata.attrs["NX_class"] = "NXdata"
        nexus.select_default_plot(nxdata)
        nxdata.attrs["axes"] = [xname]
        nxdata.attrs["signal"] = yname
        xdset = nxdata.create_dataset(xname, data=x)
        xdset.attrs["units"] = xunits
        nxdata.create_dataset(yname, data=y)
        if data_utils.is_data(yerror):
            nxdata.create_dataset(f"{yname}_errors", data=yerror)
        nexus.select_default_plot(nxdata)

    def save_configuration(self, nxprocess):
        header = self.inputs.header
        if not header:
            return
        if "configuration" in nxprocess:
            del nxprocess["configuration"]
        configuration = nxprocess.create_group("configuration")
        configuration.attrs["NX_class"] = "NXcollection"

        info = dict(header)

        if info.get("energy") or info.get("wavelength"):
            energy = info.pop("energy", None)
            wavelength = info.pop("wavelength", None)
            if not energy:
                energy = energy_wavelength(wavelength)
            elif not wavelength:
                wavelength = energy_wavelength(energy)
            dset = configuration.create_dataset("energy", data=energy)
            dset.attrs["units"] = "keV"
            dset = configuration.create_dataset("wavelength", data=wavelength)
            dset.attrs["units"] = "Angstrom"

        if info.get("detector"):
            configuration["detector"] = str(info.pop("detector"))

        if info.get("geometry"):
            cgeometry = configuration.create_group("geometry")
            cgeometry.attrs["NX_class"] = "NXcollection"

            geometry = info.pop("geometry")
            for k, v in geometry.items():
                if k == "dist":
                    dset = cgeometry.create_dataset("dist", data=v)
                    dset.attrs["units"] = "m"
                elif k == "poni1":
                    dset = cgeometry.create_dataset("poni1", data=v)
                    dset.attrs["units"] = "m"
                elif k == "poni2":
                    dset = cgeometry.create_dataset("poni2", data=v)
                    dset.attrs["units"] = "m"
                elif k == "rot1":
                    dset = cgeometry.create_dataset("rot1", data=v)
                    dset.attrs["units"] = "rad"
                elif k == "rot2":
                    dset = cgeometry.create_dataset("rot2", data=v)
                    dset.attrs["units"] = "rad"
                elif k == "rot3":
                    dset = cgeometry.create_dataset("rot3", data=v)
                    dset.attrs["units"] = "rad"

        info.pop("mask", None)

        if info:
            dicttonx(info, configuration)

    def save_metadata(self, parent):
        metadata = self.inputs.metadata
        if not metadata:
            return
        dicttonx(metadata, parent, update_mode="add")
