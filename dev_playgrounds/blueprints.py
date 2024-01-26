from cloudcraftco.cloudcraft import Cloudcraft

# Blueprint record crud operations...
#
# running playground...
# % cd {repo_directory}
# % poetry shell
# % poetry install
# % python3 dev_playgrounds/blueprints.py

cloudcraft = Cloudcraft({"host": "localhost", "port": 3000, "protocol": "http"})

# list blueprints
blueprints = cloudcraft.list_blueprints()
print("original_blueprints ::\n" + str(blueprints))
print("******************************************\n")


# create blueprint
data = {"data": {"grid": "standard", "name": "Playground blueprint"}}
result = cloudcraft.create_blueprint(data)
print("post-blueprint ::\n" + str(result))
print("******************************************\n")


test_blueprint_id = result["id"]
print("test_blueprint_id :: " + test_blueprint_id)
print("******************************************\n")


# update blueprint
data = {
    "data": {
        "grid": "standard",
        "name": "Updated playground blueprint",
        "text": [
            {
                "id": "label1",
                "text": "Hello\nWorld!",
                "type": "isotext",
                "color": "#f5b720",
                "mapPos": [0, 0],
                "textSize": 15,
            }
        ],
    }
}
result = cloudcraft.update_blueprint(test_blueprint_id, data)
print("put-blueprint ::\n" + str(result))
print("******************************************\n")


# read blueprint
blueprint = cloudcraft.read_blueprint(test_blueprint_id)
print("read_blueprint ::\n" + str(blueprint))
print("******************************************\n")


# delete blueprint
result = cloudcraft.delete_blueprint(test_blueprint_id)
print("delete-blueprint ::\n" + str(result))
print("******************************************\n")
