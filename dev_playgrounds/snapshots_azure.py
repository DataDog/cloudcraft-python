import os

from cloudcraftco.cloudcraft import Cloudcraft

# Azure Account snapshot exporting...
# aka scanning account, then exporting auto-layout blueprint
# snapshots_azure.py requires existing azure accounts
#
# running playground...
# % cd {repo_directory}
# % poetry shell
# % poetry install
# % export CLOUDCRAFT_API_KEY={{ api-key }}
# % python3 dev_playgrounds/snapshots_azure.py

cloudcraft = Cloudcraft({"host": "localhost", "port": 3000, "protocol": "http"})
script_dir = os.path.dirname(os.path.realpath(__file__)) + os.sep

# list azure accounts
accounts = cloudcraft.list_azure_accounts()
ss_account = accounts["accounts"][0]["id"]
print("ss_account :: " + ss_account)
print("script_dir :: " + script_dir)
print("******************************************\n")


# check snapshot formats (no optional parameters)
# expected: [200, 202, 401, 403, 404]
# location: azure location, e.g. "canadaeast"
# format in ["json", "svg", "png", "pdf", "mxGraph"]
ss_location = "canadaeast"
ss_format = "png"
ss_file = script_dir + ss_location + "." + ss_format
snapshot = cloudcraft.snapshot_azure_account(ss_account, ss_location, ss_format)
# print("snapshot :: " + str(snapshot))
with open(ss_file, "wb") as binary_file:
    binary_file.write(snapshot)
print("snapshot saved to file: " + ss_file)
print("******************************************\n")


# check snapshot formats with optional parameters
# expected: [200, 202, 401, 403, 404]
ss_options = {"grid": True, "scale": 1.5}
ss_location = "canadaeast"
ss_format = "png"
ss_file = script_dir + ss_location + "-filtered." + ss_format
snapshot = cloudcraft.snapshot_azure_account(
    ss_account, ss_location, ss_format, ss_options
)
with open(ss_file, "wb") as binary_file:
    binary_file.write(snapshot)
print("filtered-snapshot saved to file: " + ss_file)
print("******************************************\n")
