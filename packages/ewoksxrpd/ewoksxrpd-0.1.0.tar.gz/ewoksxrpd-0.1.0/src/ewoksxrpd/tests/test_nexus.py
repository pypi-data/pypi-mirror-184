import numpy
import h5py
from silx.io.utils import h5py_read_dataset
from ..tasks import SaveNexusPattern1D
from orangecontrib.ewoksxrpd.nexus import OWSaveNexusPattern1D
from .utils import execute_task


def test_save_nexus_task(tmpdir, setup1, bliss_lab6_scan):
    assert_save_nexus(tmpdir, setup1, None, bliss_lab6_scan)


def test_save_nexus_widget(tmpdir, setup1, qtapp, bliss_lab6_scan):
    assert_save_nexus(tmpdir, setup1, qtapp, bliss_lab6_scan)


def assert_save_nexus(tmpdir, setup1, qtapp, bliss_lab6_scan):
    bliss_scan_url = f"{bliss_lab6_scan}::/2.1"
    inputs = {
        "url": str(tmpdir / "result.h5"),
        "x": numpy.linspace(1, 60, 60),
        "y": numpy.random.random(60),
        "xunits": "2th_deg",
        "header": {
            "energy": 10.2,
            "detector": setup1.detector,
            "geometry": setup1.geometry,
        },
        "metadata": {"dummy": {"test": "test"}},
        "bliss_scan_url": bliss_scan_url,
        "retry_timeout": 5,
    }

    execute_task(
        SaveNexusPattern1D,
        OWSaveNexusPattern1D,
        inputs=inputs,
        widget=qtapp is not None,
    )

    with h5py.File(str(tmpdir / "result.h5")) as root:
        expected = {"instrument", "measurement", "integrate", "dummy"}
        nxprocess = root["results/integrate"]
        assert set(root["results"].keys()) == expected
        numpy.testing.assert_array_equal(nxprocess["diffractogram/2th"], inputs["x"])
        numpy.testing.assert_array_equal(nxprocess["diffractogram/data"], inputs["y"])
        numpy.testing.assert_array_equal(
            root["results/measurement/diffractogram"], inputs["y"]
        )
        numpy.testing.assert_array_equal(
            nxprocess["configuration/energy"], inputs["header"]["energy"]
        )
        numpy.testing.assert_array_equal(
            nxprocess["configuration/energy"].attrs["units"], "keV"
        )
        assert h5py_read_dataset(root["results/dummy/test"]) == "test"
