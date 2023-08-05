from blissoda.demo.streamline_scanner import streamline_sc  # noqa F401
from blissoda.demo.streamline_scanner import streamline_scanner


def streamline_demo(with_calibration=True):
    streamline_scanner.init_workflow(with_calibration=with_calibration)
    streamline_scanner.calib(0.1)
    streamline_scanner.run(0.1, nholders=2)
