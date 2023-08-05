import json
from pyFAI.io.ponifile import PoniFile
from ewokscore import Task

from .utils.xrpd_utils import energy_wavelength

__all__ = ["PyFaiConfig"]


class PyFaiConfig(
    Task,
    optional_input_names=[
        "filename",
        "energy",
        "geometry",
        "mask",
        "detector",
        "calibrant",
        "integration_options",
    ],
    output_names=[
        "energy",
        "geometry",
        "detector",
        "calibrant",
        "mask",
        "integration_options",
    ],
):
    def run(self):
        integration_options = self.from_file()
        if self.inputs.integration_options:
            integration_options.update(self.inputs.integration_options)

        # Required outputs
        energy = self.inputs.energy
        wavelength = integration_options.pop("wavelength", None)
        if self.missing_inputs.energy and wavelength is not None:
            energy = energy_wavelength(wavelength)

        detector = self.inputs.detector
        cdetector = integration_options.pop("detector", None)
        if self.missing_inputs.detector and cdetector is not None:
            detector = cdetector

        geometry = self.inputs.geometry
        cgeometry = {
            k: integration_options.pop(k)
            for k in ["dist", "poni1", "poni2", "rot1", "rot2", "rot3"]
            if k in integration_options
        }
        if self.missing_inputs.geometry and len(cgeometry) == 6:
            geometry = cgeometry

        # Optional outputs
        calibrant = self.get_input_value("calibrant", None)

        mask = self.get_input_value("mask", None)
        cmask = integration_options.pop("mask_file", None)
        if self.missing_inputs.mask and cmask is not None:
            mask = cmask

        # Split integration and worker options
        self.outputs.energy = energy
        self.outputs.geometry = geometry
        self.outputs.detector = detector
        self.outputs.calibrant = calibrant
        self.outputs.mask = mask
        self.outputs.integration_options = integration_options

    def from_file(self) -> dict:
        filename = self.inputs.filename
        if not filename:
            return dict()
        if filename.endswith(".json"):
            with open(filename, "r") as fp:
                return json.load(fp)
        else:
            return PoniFile(filename).as_dict()
