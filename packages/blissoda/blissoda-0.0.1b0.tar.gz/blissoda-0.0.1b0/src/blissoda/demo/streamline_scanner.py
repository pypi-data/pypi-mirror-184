import numpy
import json
from contextlib import contextmanager

try:
    from bliss import setup_globals
except ImportError:
    setup_globals = None

from ..streamline.streamline_scanner import StreamlineScanner


def energy_wavelength(x):
    """keV to Angstrom and vice versa"""
    return 12.398419843320026 * 1e-10 / x


class StreamlineDemoScanner(StreamlineScanner):
    def __init__(self):
        super().__init__()
        self._set_parameter_default("detector_name", "difflab6")
        self._set_parameter_default("detector_type", "Pilatus1M")
        self._set_parameter_default("calibrant", "LaB6")
        self._set_parameter_default("sample_changer_name", "streamline_sc")
        self._set_parameter("image_slice", "0,0:-1,0:-1")
        self._set_parameter_default(
            "integration_options",
            {
                "error_model": "azimuthal",
                "method": "csr_no_cython",
                "integrator_name": "sigma_clip_ng",
                "extra_options": {"max_iter": 3, "thres": 0},
                "nbpt_rad": 1024,
                "unit": "q_nm^-1",
            },
        )

    def measure_sample(self, *args, **kwargs):
        return setup_globals.sct(*args, setup_globals.difflab6, **kwargs)

    def calib(self, *args, sample_index=0, **kwargs):
        return super().calib(*args, sample_index=sample_index, **kwargs)

    def init_workflow(self, with_calibration: bool = True):
        self._ensure_pyfai_config()
        return super().init_workflow(with_calibration=with_calibration)

    def _ensure_pyfai_config(self):
        if self.pyfai_config:
            return
        cfgfile = "/tmp/test.json"
        poni = {
            "dist": 5e-2,  # 10 cm
            "poni1": 10e-2,  # 10 cm
            "poni2": 10e-2,  # 10 cm
            "rot1": numpy.radians(10),  # 10 deg
            "rot2": 0,  # 0 deg
            "rot3": 0,  # 0 deg
            "wavelength": energy_wavelength(12),  # A
            "detector": self.detector_type,
        }
        with open(cfgfile, "w") as f:
            json.dump(poni, f)
        self.pyfai_config = cfgfile

    @contextmanager
    def run_context(self):
        yield

    @property
    def sample_changer(self):
        return streamline_sc


class MockSampleChanger:
    def select_sample(self, sample_index):
        return f"lab6_{sample_index}"

    def select_sample_without_qr(self, sample_index):
        return f"lab6_{sample_index}"

    def iterate_samples(self, sample_indices=None):
        if not sample_indices:
            sample_indices = range(16)
        for i in sample_indices:
            yield f"lab6_{i}"

    def iterate_samples_without_qr(self, sample_indices=None):
        if not sample_indices:
            sample_indices = range(16)
        for i in sample_indices:
            yield f"lab6_{i}"

    def eject_old_baguette(self):
        pass

    def load_baguette_with_homing(self):
        pass

    def has_remaining_baguettes(self):
        return True

    @property
    def number_of_remaining_baguettes(self):
        return 1


if setup_globals is None:
    streamline_scanner = None
    streamline_sc = None
else:
    streamline_scanner = StreamlineDemoScanner()
    streamline_sc = MockSampleChanger()
