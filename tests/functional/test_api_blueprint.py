import os

import pytest

from cloudcraftco.cloudcraft import Cloudcraft

# Warning: testing against production
# api_key must be assigned to env-variable

cloudcraft = Cloudcraft()


def test_blueprint_api():
    """Test blueprint api."""
    # create blueprint
    data = {"data": {"grid": "standard", "name": "TEST blueprint"}}
    bp_created = cloudcraft.create_blueprint(data)
    assert len(bp_created.get("id")) == 36
    assert bp_created.get("data").get("name") == "TEST blueprint"

    # assign test blueprint id
    test_blueprint_id = bp_created.get("id")

    # update blueprint
    data = {
        "data": {
            "grid": "standard",
            "name": "UPDATED TEST blueprint",
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
    bp_updated = cloudcraft.update_blueprint(test_blueprint_id, data)
    assert bp_updated == None

    # read blueprint
    bp_read = cloudcraft.read_blueprint(test_blueprint_id)
    assert bp_read.get("id") == test_blueprint_id
    assert bp_read.get("data").get("name") == "UPDATED TEST blueprint"

    # list blueprints
    bp_list = cloudcraft.list_blueprints()
    bp_ids = [bp.get("id") for bp in bp_list.get("blueprints")]
    assert test_blueprint_id in bp_ids

    # export blueprint
    bytestring = cloudcraft.export_blueprint(test_blueprint_id, "svg")
    bp_svg = bytestring.decode("utf-8")
    assert bp_svg[0:51] == '<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg'

    # delete blueprint
    bp_deleted = cloudcraft.delete_blueprint(test_blueprint_id)
    bp_new_list = cloudcraft.list_blueprints()
    bp_new_ids = [bp.get("id") for bp in bp_new_list.get("blueprints")]
    assert bp_deleted == None
    assert test_blueprint_id not in bp_new_ids
