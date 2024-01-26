import os

from cloudcraftco.cloudcraft import Cloudcraft

# AWS Account snapshot exporting...
# aka scanning account, then exporting auto-layout blueprint
#
# running playground...
# % cd {repo_directory}
# % poetry shell
# % poetry install
# % python3 dev_playgrounds/snapshots.py

cloudcraft = Cloudcraft({"host": "localhost", "port": 3000, "protocol": "http"})
script_dir = os.path.dirname(os.path.realpath(__file__)) + os.sep

# list aws accounts
accounts = cloudcraft.list_aws_accounts()
ss_account = accounts["accounts"][1]["id"]
print("ss_account :: " + ss_account)
print("script_dir :: " + script_dir)
print("******************************************\n")


# check snapshot formats (no optional parameters)
# expected: [200, 202, 401, 403, 404]
# region: aws region, e.g. "us-east-2"
# format in ["json", "svg", "png", "pdf", "mxGraph"]
ss_region = "us-west-2"
ss_format = "png"
ss_file = script_dir + ss_region + "." + ss_format
snapshot = cloudcraft.snapshot_aws_account(ss_account, ss_region, ss_format)
# print("snapshot :: " + str(snapshot))
with open(ss_file, "wb") as binary_file:
    binary_file.write(snapshot)
print("snapshot saved to file: " + ss_file)
print("******************************************\n")


# check snapshot formats with optional parameters
# expected: [200, 202, 401, 403, 404]
ss_options = {"filter": "role=bastion OR env=staging", "grid": True, "scale": 1.5}
ss_region = "us-east-1"
ss_format = "png"
ss_file = script_dir + ss_region + "-filtered." + ss_format
snapshot = cloudcraft.snapshot_aws_account(ss_account, ss_region, ss_format, ss_options)
with open(ss_file, "wb") as binary_file:
    binary_file.write(snapshot)
print("filtered-snapshot saved to file: " + ss_file)
print("******************************************\n")
