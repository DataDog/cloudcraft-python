from cloudcraftco.cloudcraft import Cloudcraft

# obtain AWS User properties -- defaults and settings
# assigned while using Cloudcraft app
#
# running playground...
# % cd {repo_directory}
# % poetry shell
# % poetry install
# % export CLOUDCRAFT_API_KEY={{ api-key }}
# % python3 dev_playgrounds/users.py

cloudcraft = Cloudcraft({"host": "localhost", "port": 3000, "protocol": "http"})

# read cloudcraft user properties
profile = cloudcraft.read_user_profile()
print("user-profile ::\n" + str(profile))
print("******************************************\n")
