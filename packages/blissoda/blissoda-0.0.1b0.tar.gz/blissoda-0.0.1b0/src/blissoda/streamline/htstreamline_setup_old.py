"""NEEDS REFACTORING"""
import os
import sys

from silx.io.h5py_utils import top_level_names

try:
    from bliss import setup_globals
    from bliss.common.logtools import user_print
except ImportError:
    setup_globals = None
    user_print = print

from ewoks import convert_graph
from ewoksjob.client import submit, cancel, get_not_finished

# TODO: find a better way
sys.path.append("/users/opid31/xrpd/config/")


def streamline_workflows():
    """Show how many workflows are running"""
    user_print(f"{len(get_not_finished())} workflows are running")


def streamline_cancel_all_workflow():
    """Cancel all running workflows"""
    streamline_workflows()
    for task_id in get_not_finished():
        cancel(task_id)
    streamline_workflows()


def _norack_it():
    for i in range(16):
        setup_globals.streamline_sc.sc_axis.move(i)
        yield f"hole{i+1}"


def streamline_scan_holder(*sct_args, experiment=None, **job_kwargs):
    """On each hole: read QR code, ct and start data processing workflows"""

    if experiment == "noqr_rack":
        it = _norack_it()
    else:
        it = setup_globals.streamline_sc.iterate_sample

    # Loop over the holes and measure the powders
    for i, qr_response in enumerate(it, 1):
        _streamline_measure_hole(
            i, qr_response, *sct_args, experiment=experiment, **job_kwargs
        )
        if experiment in ["basf_tryout", "noqr_rack"] and i == 15:
            return


def streamline_measure_hole(i, *sct_args, experiment=None, **job_kwargs):
    """On hole i: read QR code, ct and start data processing workflows"""
    setup_globals.streamline_sc.sc_axis.move(i)
    qr_response = setup_globals.streamline_sc.qr_read()
    _streamline_measure_hole(
        i, qr_response, *sct_args, experiment=experiment, **job_kwargs
    )


def _streamline_measure_hole(
    i,
    qr_response,
    *sct_args,
    experiment=None,
    workflow: bool = True,
    datasetname=None,
    **job_kwargs,
):
    # Define your calibration scan
    if experiment == "test":
        setup_globals.newproposal("id312205")
        job_kwargs["calib_collection_name"] = "test_1_01"
        job_kwargs["calib_dataset_name"] = "0001"
        job_kwargs["calib_scan_number"] = 32
    else:
        job_kwargs["calib_collection_name"] = "alignment_sixc"
        job_kwargs["calib_dataset_name"] = "0001"
        job_kwargs["calib_scan_number"] = 20

    """On hole i: ct and start data processing workflows"""
    user_print("\n------------------")
    user_print(f"Measure hole {i}")
    user_print("------------------")
    metadata = _streamline_parse_response(qr_response, experiment=experiment)
    user_print(f"Metadata: {metadata}")
    setup_globals.newsample(metadata["sample"]["name"])
    setup_globals.newdataset(datasetname)

    if workflow:
        args, kwargs = _streamline_job_arguments(
            experiment=experiment, metadata=metadata, **job_kwargs
        )
        submit(args=args, kwargs=kwargs)

    if experiment != "test":
        setup_globals.sct(*sct_args, scan_info=metadata)

    if workflow:
        streamline_workflows()


def _streamline_parse_response(response, experiment=None):
    """Extract metadata from QR code"""
    if experiment == "test":
        name = response.split(" ")[-1].strip().replace(":", "_")
        return {
            "sample": {"@NX_class": "NXsample", "name": name},
            "instrument": {
                "@NX_class": "NXinstrument",
                "sample_change": {
                    "@NX_class": "NXpositioner",
                    "value": setup_globals.streamline_sc.sc_axis.position,
                },
            },
        }
    elif experiment == "calib":
        name = response.split(" ")[-1].strip().replace(":", "_")
        return {
            "sample": {"@NX_class": "NXsample", "name": name},
            "instrument": {
                "@NX_class": "NXinstrument",
                "sample_change": {
                    "@NX_class": "NXpositioner",
                    "value": setup_globals.streamline_sc.sc_axis.position,
                },
                "nanodac": {
                    "@NX_class": "NXdetector",
                    "value": setup_globals.nanodac4.output.read(),
                },
            },
        }
    elif experiment == "basf":
        uuid = response.split(":")[0]
        name = "_" + uuid
        return {
            "sample": {"@NX_class": "NXsample", "name": name, "uuid": uuid},
            "instrument": {
                "@NX_class": "NXinstrument",
                "sample_change": {
                    "@NX_class": "NXpositioner",
                    "value": setup_globals.streamline_sc.sc_axis.position,
                },
                "nanodac": {
                    "@NX_class": "NXdetector",
                    "value": setup_globals.nanodac4.output.read(),
                },
            },
        }

    elif experiment == "basf_tryout":
        name = "basf_streamline_tryout_" + response.rstrip().split(" ")[-1]
        return {
            "sample": {"@NX_class": "NXsample", "name": name},
            "instrument": {
                "@NX_class": "NXinstrument",
                "sample_change": {
                    "@NX_class": "NXpositioner",
                    "value": setup_globals.streamline_sc.sc_axis.position,
                },
                "nanodac": {
                    "@NX_class": "NXdetector",
                    "value": setup_globals.nanodac4.output.read(),
                },
            },
        }
    elif experiment == "noqr_rack":
        name = "noqr_rack_" + response
        return {
            "sample": {"@NX_class": "NXsample", "name": name},
            "instrument": {
                "@NX_class": "NXinstrument",
                "sample_change": {
                    "@NX_class": "NXpositioner",
                    "value": setup_globals.streamline_sc.sc_axis.position,
                },
                "nanodac": {
                    "@NX_class": "NXdetector",
                    "value": setup_globals.nanodac4.output.read(),
                },
            },
        }
    else:
        raise RuntimeError(f"Experiment {experiment} is not known: {response}")


def _streamline_job_arguments(
    calib_collection_name: str = None,
    calib_dataset_name: str = None,
    calib_scan_number: int = None,
    metadata=None,
    experiment=None,
):
    """Arguments for the workflow execution"""
    # Data to be integrated
    uri, out_dir = _get_locations()
    image = f"silx://{uri}/measurement/p3&slice=0"

    # Calibration data
    calib_uri, calib_out_dir = _get_locations(
        collection_name=calib_collection_name,
        dataset_name=calib_dataset_name,
        scan_number=calib_scan_number,
    )
    calib_image = f"silx://{calib_uri}/measurement/p3&slice=0"

    # We don't actually do a ct for testing
    if experiment == "test":
        image = calib_image

    # Location of results
    transient_dir = os.path.join(_get_results_root(), "transient_results")
    calib_2d_diagnostics = os.path.join(calib_out_dir, "calib_2d_diagnostics.png")
    calib_1d_diagnostics = os.path.join(calib_out_dir, "calib_1d_diagnostics.png")
    results = os.path.join(out_dir, "results.nx")
    workflow_with_inputs = os.path.join(out_dir, "workflow.json")

    user_print(f"\nCalibration URI:     {calib_uri}")
    user_print(f"Calibration results: {calib_out_dir}")
    user_print(f"Data URI:            {uri}")
    user_print(f"Results:             {out_dir}")

    # Workflow calibration parameters
    inputs = [
        {"label": "calib_singledistance", "name": "image", "value": calib_image},
        {
            "label": "calib_singledistance",
            "name": "energy",
            "value": setup_globals.energy.position,
        },
        {"label": "calib_integrate1d", "name": "image", "value": calib_image},
        {"label": "diagnose_singlecalib", "name": "image", "value": calib_image},
        {
            "label": "diagnose_singlecalib",
            "name": "filename",
            "value": calib_2d_diagnostics,
        },
        {
            "label": "diagnose_integrate1d",
            "name": "filename",
            "value": calib_1d_diagnostics,
        },
    ]

    # Workflow integration parameters
    inputs += [
        {"label": "integrate1d", "name": "image", "value": image},
        {"label": "save_nexus", "name": "url", "value": results},
        {"label": "save_nexus", "name": "metadata", "value": metadata},
    ]

    # Save the workflow with inputs in the result directory
    workflow = _get_workflow()
    setup_globals.SCAN_SAVING.writer_object.create_path(out_dir)
    convert_graph(
        workflow,
        workflow_with_inputs,
        inputs=inputs,
        save_options={"indent": 2},
    )

    # Job arguments
    args = (workflow_with_inputs,)
    varinfo = {"root_uri": transient_dir, "scheme": "nexus"}
    kwargs = {"binding": None, "varinfo": varinfo}

    return args, kwargs


def _get_locations(collection_name=None, dataset_name=None, scan_number=None):
    """Scan uri and associated result directory"""
    base_path = setup_globals.SCAN_SAVING.base_path
    proposal_dirname = setup_globals.SCAN_SAVING.proposal_dirname
    if collection_name is None:
        collection_name = setup_globals.SCAN_SAVING.collection_name
    if dataset_name is None:
        dataset_name = setup_globals.SCAN_SAVING.dataset_name
    sub_dir = setup_globals.SCAN_SAVING.template.format(
        base_path=base_path,
        beamline=setup_globals.SCAN_SAVING.beamline,
        proposal_dirname=proposal_dirname,
        collection_name=collection_name,
        dataset_name=dataset_name,
    )
    basename = os.path.basename(sub_dir)
    filename = os.path.abspath(os.path.join(base_path, sub_dir, basename + ".h5"))
    if scan_number is None:
        scan_number = _get_next_scan_number(filename)
    uri = f"{filename}?path=/{scan_number}.1"
    out_dir = os.path.join(
        _get_results_root(), "results", collection_name, dataset_name
    )
    return uri, out_dir


def _get_results_root():
    """Root directory where all results are saved"""
    return os.path.dirname(setup_globals.SCAN_SAVING.collection.path)


def _get_workflow():
    # return "/users/opid31/xrpd/xrpd_id31.json"
    return "/data/visitor/in1029/id31/workflows/in1029_workflow1.json"


def _get_next_scan_number(filename):
    """Get the next scan number by looking at the file"""
    if not os.path.exists(filename):
        return 1
    return max(int(float(s)) for s in top_level_names(filename)) + 1
