import os
import json
from glob import glob
from ewoksjob.client import submit


if __name__ == "__main__":
    os.environ["BEACON_HOST"] = "id31:25000"
    root_dir = "/data/visitor/in1029/id31/20221115/processed/"

    workflows = glob(os.path.join(root_dir, "streamline/*/*.json"))
    for wffilename in workflows:
        with open(wffilename, "r") as f:
            workflow = json.load(f)

        kwargs = dict()
        kwargs["varinfo"] = varinfo = {
            "root_uri": os.path.join(root_dir, "_nobackup/"),
            "scheme": "nexus",
        }

        # Define new processing
        old_processed = os.path.join("processed", "streamline")
        new_processed = os.path.join("processed", "streamline_2th")
        kwargs["convert_destination"] = wffilename.replace(old_processed, new_processed)
        for nodeattrs in workflow["nodes"]:
            for idict in nodeattrs.get("default_inputs", list()):
                if idict["name"] == "integration_options":
                    idict["value"]["unit"] = "2th_deg"
                elif (
                    isinstance(idict["value"], str)
                    and old_processed in idict["value"]
                    and "ring_detection" not in idict["value"]
                ):
                    idict["value"] = idict["value"].replace(
                        old_processed, new_processed
                    )

        submit(args=(workflow,), kwargs=kwargs)
