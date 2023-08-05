import os

try:
    from bliss import setup_globals
except ImportError:
    setup_globals = None
from ..exafs_plotting.exafs_plotter import ExafsPlotter
from ..resources.bm23 import RESOURCE_ROOT


class DemoExafsPlotter(ExafsPlotter):
    def __init__(self) -> None:
        super().__init__()
        self._set_parameter_default("workflow", os.path.join(RESOURCE_ROOT, "bm23.ows"))
        self._set_parameter_default("_scan_type", "any")
        self._counters.setdefault(
            "any",
            {
                "mu_name": "diode1",
                "energy_name": "roby",
                "energy_unit": "keV",
            },
        )

    def _scan_type_from_scan(self, scan) -> str:
        return "any"

    def run(self):
        scan = setup_globals.ascan(
            setup_globals.roby, 7, 7.1, 200, 0.01, setup_globals.diode1, run=False
        )
        super().run(scan)


if setup_globals is None:
    exafs_plotter = None
else:
    exafs_plotter = DemoExafsPlotter()
