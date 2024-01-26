import os

from cloudcraftco.cloudcraft import Cloudcraft

# Blueprint budget exporting
#
# running playground...
# % cd {repo_directory}
# % poetry shell
# % poetry install
# % python3 dev_playgrounds/budgets.py

cloudcraft = Cloudcraft({"host": "localhost", "port": 3000, "protocol": "http"})
script_dir = os.path.dirname(os.path.realpath(__file__)) + os.sep

# list blueprints
blueprints = cloudcraft.list_blueprints()
bp_id = blueprints["blueprints"][0]["id"]
print("bp_id :: " + str(bp_id))
print("script_dir :: " + script_dir)
print("******************************************\n")


# check export formats (no optional parameters)
# expected: [200, 202, 401, 403, 404]
# format in ["csv", "xlsx"]
bp_format = "csv"
bp_file = script_dir + bp_id + "." + bp_format
export = cloudcraft.export_blueprint_budget(bp_id, bp_format)
print("export :: " + str(export))
with open(bp_file, "wb") as binary_file:
    binary_file.write(export)
print("export saved to file: " + bp_file)
print("******************************************\n")


# check snapshot formats with optional parameters
# expected: [200, 202, 401, 403, 404]
bp_options = {"period": "h"}
bp_format = "csv"
bp_file = script_dir + bp_id + "-opts." + bp_format
export = cloudcraft.export_blueprint_budget(bp_id, bp_format, bp_options)
with open(bp_file, "wb") as binary_file:
    binary_file.write(export)
print("customized-export saved to file: " + bp_file)
print("******************************************\n")
