"""
.. code:: python

    DEMO_SESSION [1]: from blissoda.demo.streamline_scanner import streamline_scanner,sample_changer
    DEMO_SESSION [2]: streamline_scanner.eject()
    DEMO_SESSION [3]: streamline_scanner.load()
    DEMO_SESSION [4]: streamline_scanner.calib(1, sample_index=0)
    DEMO_SESSION [5]: streamline_scanner.run(0.1)
"""

import os
import re
import shutil
from numbers import Number
from contextlib import contextmanager
from typing import Optional, NamedTuple, Tuple
import numpy

try:
    from bliss import current_session
    from bliss import setup_globals
    from bliss.common.logtools import user_warning, user_info
except ImportError:
    setup_globals = None
    current_session = None
    user_warning = print
    user_info = print

try:
    from ewoksjob.client import submit
except ImportError:
    submit = None
from ..persistent import WithPersistentParameters
from ..resources.streamline import RESOURCE_ROOT
from ..utils.info import format_info
from ..utils.directories import get_processed_dir


class ScanInfo(NamedTuple):
    filename: str
    scan_nb: int

    @property
    def url(self):
        return f"{self.filename}::/{self.scan_nb}.1"


class StreamlineScanner(
    WithPersistentParameters,
    parameters=[
        "workflow",
        "sample_changer_name",
        "detector_name",
        "energy_name",
        "calibrations",
        "calibration_motor",
        "image_slice",
        "integration_options",
        "pyfai_config",
        "calibrant",
        "detector_type",
        "trigger_workflows",
    ],
):
    def __init__(self) -> None:
        super().__init__()
        self._set_parameter_default("image_slice", 0)
        self._set_parameter_default("trigger_workflows", True)

    def __info__(self):
        s = super().__info__()
        info = {
            "# sample holders": self.sample_changer.number_of_remaining_baguettes,
            "selected sample": int(self.sample_changer.translation.position),
            "vibration speed (%)": self.sample_changer.vibration_speed,
        }
        return f"{s}\n\nStatus:\n " + format_info(info)

    def measure_sample(self, *args, **kwargs):
        return setup_globals.sct(*args, **kwargs)

    @property
    def sample_changer(self):
        self._raise_when_missing("sample_changer_name")
        return current_session.env_dict[self.sample_changer_name]

    def eject(self):
        self.sample_changer.eject_old_baguette()
        print(
            "\n\nNumber of remaining sample holders:",
            self.sample_changer.number_of_remaining_baguettes,
        )

    def load(self):
        self.sample_changer.load_baguette_with_homing()

    def run(
        self,
        *scan_args,
        nholders: Optional[int] = None,
        use_qr_code: bool = True,
        current_holder: bool = False,
        sample_indices: Optional[Tuple[int]] = None,
        **scan_kwargs,
    ):
        if self.workflow_has_calib and not self._get_calibration():
            raise RuntimeError("measure a calibration standard first")

        with self.run_context():
            if current_holder:
                self.load()
                self._run_holder(
                    scan_args,
                    scan_kwargs,
                    use_qr_code=use_qr_code,
                    sample_indices=sample_indices,
                )
            elif nholders is None:
                while self.sample_changer.has_remaining_baguettes():
                    self.eject()
                    self.load()
                    self._run_holder(
                        scan_args,
                        scan_kwargs,
                        use_qr_code=use_qr_code,
                        sample_indices=sample_indices,
                    )
                self.eject()
            else:
                for _ in range(nholders):
                    self.eject()
                    self.load()
                    self._run_holder(
                        scan_args,
                        scan_kwargs,
                        use_qr_code=use_qr_code,
                        sample_indices=sample_indices,
                    )
                self.eject()

    def _run_holder(
        self,
        scan_args: tuple,
        scan_kwargs: dict,
        use_qr_code: bool = True,
        sample_indices: Optional[Tuple[int]] = None,
    ):
        if use_qr_code:
            itfunc = self.sample_changer.iterate_samples
        else:
            itfunc = self.sample_changer.iterate_samples_without_qr
        for sample_name in itfunc(sample_indices=sample_indices):
            self._process_sample(sample_name, scan_args, scan_kwargs)

    def calib(
        self,
        *scan_args,
        sample_index: Optional[int] = None,
        use_qr_code: bool = True,
        **scan_kwargs,
    ):
        if sample_index is None:
            raise ValueError("argument 'sample_index' not provided")
        with self.run_context():
            if use_qr_code:
                sample_name = self.sample_changer.select_sample(sample_index)
            else:
                sample_name = self.sample_changer.select_sample_without_qr(sample_index)
            self._process_sample(sample_name, scan_args, scan_kwargs, calibrant=True)

    def init_workflow(self, with_calibration: bool = True):
        if with_calibration:
            filename = "streamline_with_calib.ows"
        else:
            filename = "streamline_without_calib.ows"
        basename = os.path.splitext(filename)[0]
        source = os.path.join(RESOURCE_ROOT, filename)
        dirname = self._get_workflows_dirname(current_session.scan_saving.filename)
        os.makedirs(dirname, exist_ok=True)
        destination = os.path.join(dirname, f"{basename}.ows")
        i = 1
        while os.path.exists(destination):
            destination = os.path.join(dirname, f"{basename}{i}.ows")
            i += 1
        shutil.copyfile(source, destination)
        self.workflow = destination
        user_info(f"Active data processing workflow: {destination}")

    @property
    def workflow_has_calib(self):
        return self.workflow and "with_calib" in self.workflow

    def _set_calibration_scan(self, scan_info: ScanInfo):
        if not scan_info.filename:
            user_warning("Cannot use as calibration because no data was collected")
            return
        filename = self._get_gallery_filename(scan_info.filename, "ring_detection.png")
        info = {
            "image": self._get_image_url(scan_info),
            "gallery_filename": filename,
        }
        position = self._get_calibration_position()
        if self.calibrations is None:
            self.calibrations = dict()
        self.calibrations[position] = info

    def _trigger_processing(self, scan_info: ScanInfo, processed_metadata: dict):
        if not scan_info.filename:
            user_warning("Cannot trigger workflow because no data was collected")
            return
        args, kwargs = self._job_arguments(scan_info, processed_metadata)
        submit(args=args, kwargs=kwargs)

    @contextmanager
    def run_context(self):
        self.sample_changer.translation.on()
        self.sample_changer.vibration_speed = 100
        try:
            yield
        finally:
            self.sample_changer.vibration_speed = 0

    def _process_sample(
        self,
        sample_name: str,
        scan_args: tuple,
        scan_kwargs: dict,
        calibrant: bool = False,
    ):
        self._newsample(sample_name)
        try:
            self._set_scan_metadata(scan_args, scan_kwargs)
            self._set_raw_dataset_metadata(scan_args, scan_kwargs)
            scan = self.measure_sample(*scan_args, **scan_kwargs)
            scan_info = self._get_scan_info(scan)
            if calibrant:
                self._set_calibration_scan(scan_info)
            if self.trigger_workflows:
                processed_metadata = self._get_process_dataset_metadata(scan_args)
                self._trigger_processing(scan_info, processed_metadata)
        finally:
            setup_globals.enddataset()

    def _newsample(self, sample_name: str):
        sample_name = re.sub(r"\s+", "_", sample_name)
        setup_globals.newsample(sample_name)
        setup_globals.newdataset()

    def _set_raw_dataset_metadata(self, scan_args: tuple, scan_kwargs: dict) -> None:
        for k, v in self._get_raw_dataset_metadata(scan_args).items():
            current_session.scan_saving.dataset[k] = v

    def _set_scan_metadata(self, scan_args: tuple, scan_kwargs: dict) -> None:
        scan_info = self._get_scan_metadata()
        if scan_info:
            scan_kwargs["scan_info"] = scan_info

    def _get_scan_metadata(self) -> Optional[dict]:
        return None

    def _get_raw_dataset_metadata(self, scan_args: tuple) -> dict:
        metadata = {"definition": "HTXRPD"}
        if self.energy_name:
            metadata["HTXRPD_energy"] = getattr(
                setup_globals, self.energy_name
            ).position
        if scan_args and isinstance(scan_args[0], Number):
            metadata["HTXRPD_exposureTime"] = scan_args[0]
        return metadata

    def _get_process_dataset_metadata(self, scan_args: tuple) -> dict:
        metadata = self._get_raw_dataset_metadata(scan_args)
        metadata["Sample_name"] = current_session.scan_saving.dataset["Sample_name"]
        return metadata

    def _get_calibration_position(self) -> Optional[Number]:
        if self.calibration_motor:
            return getattr(setup_globals, self.calibration_motor).position

    def _get_calibration(self) -> Optional[dict]:
        calibrations = self.calibrations
        if not calibrations:
            return None
        position = self._get_calibration_position()
        if position is not None:
            positions = [p for p in calibrations if p is not None]
            if positions:
                idx = (numpy.abs(numpy.array(positions) - position)).argmin()
                position = positions[idx]
        return calibrations.get(position)

    def _get_scan_info(self, scan) -> ScanInfo:
        if scan is None:
            return ScanInfo(filename="", scan_nb=0)
        if isinstance(scan, ScanInfo):
            return scan
        filename = scan.scan_info.get("filename")
        scan_nb = scan.scan_info.get("scan_nb")
        return ScanInfo(filename=filename, scan_nb=scan_nb)

    def _get_image_url(self, scan_info: ScanInfo) -> str:
        url = f"silx://{scan_info.filename}?path=/{scan_info.scan_nb}.1/measurement/{self.detector_name}"
        image_slice = self.image_slice
        if image_slice is not None:
            image_slice = str(image_slice)
            image_slice = re.sub(r"[\s\(\)]+", "", image_slice)
            url = f"{url}&slice={image_slice}"
        return url

    def _get_output_dir(self, dataset_filename: str) -> str:
        return os.path.join(get_processed_dir(dataset_filename), "streamline")

    def _get_transient_dirname(self, dataset_filename: str) -> str:
        return os.path.join(get_processed_dir(dataset_filename), "_nobackup")

    def _get_workflows_dirname(self, dataset_filename: str) -> str:
        return os.path.join(get_processed_dir(dataset_filename), "workflows")

    def _get_output_dirname(self, dataset_filename: str) -> str:
        filename = os.path.basename(dataset_filename)
        return os.path.join(
            self._get_output_dir(dataset_filename), os.path.splitext(filename)[0]
        )

    def _get_gallery_dirname(self, dataset_filename: str) -> str:
        return os.path.join(self._get_output_dirname(dataset_filename), "gallery")

    def _get_output_filename(self, dataset_filename: str) -> str:
        return os.path.join(
            self._get_output_dirname(dataset_filename),
            os.path.basename(dataset_filename),
        )

    def _get_gallery_filename(self, dataset_filename: str, name: str) -> str:
        return os.path.join(self._get_gallery_dirname(dataset_filename), name)

    def _get_workflow_save_filename(self, dataset_filename: str) -> str:
        basename = os.path.basename(self.workflow)
        return os.path.join(
            self._get_output_dirname(dataset_filename),
            os.path.splitext(basename)[0] + ".json",
        )

    def _get_workflow_upload_parameters(
        self, dataset_filename: str, processed_metadata: dict
    ) -> Optional[dict]:
        raw = os.path.dirname(dataset_filename)
        dataset = "integrate"
        scan_saving = current_session.scan_saving
        proposal = scan_saving.proposal_name
        beamline = scan_saving.beamline
        path = self._get_output_dirname(dataset_filename)
        return {
            "beamline": beamline,
            "proposal": proposal,
            "dataset": dataset,
            "path": path,
            "raw": [raw],
            "metadata": processed_metadata,
        }

    def _job_arguments(self, scan_info: ScanInfo, processed_metadata: dict):
        """Arguments for the workflow execution"""
        self._raise_when_missing("workflow")
        if not self.workflow_has_calib:
            self._raise_when_missing("calibrations", "calibrant", "detector_type")

        inputs = list()

        # Configuration
        if self.energy_name:
            energy = getattr(setup_globals, self.energy_name).position
            inputs.append(
                {
                    "task_identifier": "PyFaiConfig",
                    "name": "energy",
                    "value": energy,
                }
            )
        if self.integration_options:
            inputs.append(
                {
                    "task_identifier": "PyFaiConfig",
                    "name": "integration_options",
                    "value": self.integration_options.to_dict(),
                }
            )
        if self.pyfai_config:
            inputs.append(
                {
                    "task_identifier": "PyFaiConfig",
                    "name": "filename",
                    "value": self.pyfai_config,
                }
            )
        if self.calibrant:
            inputs.append(
                {
                    "task_identifier": "PyFaiConfig",
                    "name": "calibrant",
                    "value": self.calibrant,
                }
            )
        if self.detector_type:
            inputs.append(
                {
                    "task_identifier": "PyFaiConfig",
                    "name": "detector",
                    "value": self.detector_type,
                }
            )

        # Calibration
        if self.workflow_has_calib:
            calibration = self._get_calibration()
            if calibration is None:
                raise RuntimeError("no valid calibration found")

            inputs.append(
                {
                    "task_identifier": "CalibrateSingle",
                    "name": "image",
                    "value": calibration["image"],
                }
            )
            inputs.append(
                {
                    "task_identifier": "CalibrateSingle",
                    "name": "fixed",
                    "value": ["energy"],
                }
            )
            inputs.append(
                {
                    "task_identifier": "CalibrateSingle",
                    "name": "robust",
                    "value": False,
                }
            )
            inputs.append(
                {
                    "task_identifier": "DiagnoseCalibrateSingleResults",
                    "name": "image",
                    "value": calibration["image"],
                }
            )
            inputs.append(
                {
                    "task_identifier": "DiagnoseCalibrateSingleResults",
                    "name": "filename",
                    "value": calibration["gallery_filename"],
                }
            )
        # Integration
        integrate_image_url = self._get_image_url(scan_info)
        inputs += [
            {
                "task_identifier": "Integrate1D",
                "name": "image",
                "value": integrate_image_url,
            },
            {
                "task_identifier": "SaveNexusPattern1D",
                "name": "url",
                "value": self._get_output_filename(scan_info.filename),
            },
            {
                "task_identifier": "SaveNexusPattern1D",
                "name": "bliss_scan_url",
                "value": scan_info.url,
            },
            {
                "task_identifier": "SaveNexusPattern1D",
                "name": "metadata",
                "value": {"integrate": {"configuration": {"workflow": self.workflow}}},
            },
            {
                "task_identifier": "DiagnoseIntegrate1D",
                "name": "filename",
                "value": self._get_gallery_filename(
                    scan_info.filename, "integrate.png"
                ),
            },
        ]

        if (
            self.workflow_has_calib
            and calibration["image"] == integrate_image_url
            and self.calibrant
        ):
            inputs += [
                {
                    "task_identifier": "DiagnoseIntegrate1D",
                    "name": "calibrant",
                    "value": self.calibrant,
                },
            ]

        # Job arguments
        args = (self.workflow,)
        convert_destination = self._get_workflow_save_filename(scan_info.filename)
        upload_parameters = self._get_workflow_upload_parameters(
            scan_info.filename, processed_metadata
        )
        if self.workflow_has_calib:
            varinfo = {
                "root_uri": self._get_transient_dirname(scan_info.filename),
                "scheme": "nexus",
            }
        else:
            varinfo = None
        kwargs = {
            "binding": None,
            "inputs": inputs,
            "varinfo": varinfo,
            "convert_destination": convert_destination,
            "upload_parameters": upload_parameters,
            "save_options": {"indent": 2},
        }
        return args, kwargs
