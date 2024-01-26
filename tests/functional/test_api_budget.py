import os

import pytest

from cloudcraftco.cloudcraft import Cloudcraft

# Warning: testing against production
# api_key must be assigned to env-variable

cloudcraft = Cloudcraft()


def test_budget_api():
    """Test api response for export_blueprint_budget."""
    # setup - create blueprint
    data = {
        "data": {
            "grid": "standard",
            "projection": "isometric",
            "theme": {"base": "light"},
            "name": "UPDATED HACK blueprint",
            "nodes": [
                {
                    "id": "bf74f99c-7133-4091-bc9c-99ccdc624acc",
                    "type": "ec2",
                    "mapPos": [2, 8],
                    "region": "us-east-1",
                    "transparent": False,
                    "platform": "linux",
                    "instanceType": "r6id",
                    "instanceSize": "large",
                }
            ],
            "text": [],
            "edges": [],
            "icons": [],
            "groups": [],
            "images": [],
            "surfaces": [],
            "connectors": [],
        }
    }
    bp_created = cloudcraft.create_blueprint(data)
    test_blueprint_id = bp_created.get("id")

    # export blueprint
    bytestring = cloudcraft.export_blueprint_budget(test_blueprint_id, "csv")
    budget = bytestring.decode("utf-8")
    assert budget[0:42] == "category,type,region,count,unitPrice,cost,"

    # cleanup - remove blueprint
    bp_deleted = cloudcraft.delete_blueprint(test_blueprint_id)
