import os


def get_dataset_dir(dataset_filename: str) -> str:
    return os.path.dirname(dataset_filename)


def get_collection_dir(dataset_filename: str) -> str:
    return _abs_join(get_dataset_dir(dataset_filename), "..")


def get_raw_dir(dataset_filename: str) -> str:
    return _abs_join(get_collection_dir(dataset_filename), "..")


def get_proposal_dir(dataset_filename: str) -> str:
    dirname = get_raw_dir(dataset_filename)
    if os.path.basename(dirname) == "raw":
        # version 2
        return _abs_join(dirname, "..")
    # version 1: proposal == raw
    return dirname


def get_processed_dir(dataset_filename: str) -> str:
    return _abs_join(get_proposal_dir(dataset_filename), "processed")


def get_session_dir(dataset_filename: str) -> str:
    return _abs_join(get_proposal_dir(dataset_filename), "..")


def _abs_join(*args):
    return os.path.abspath(os.path.join(*args))
