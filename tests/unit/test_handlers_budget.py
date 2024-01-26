import pytest

from cloudcraftco.cloudcraft import Cloudcraft


@pytest.fixture()
def export_blueprint_budget_fixture():
    fixture = b"category,type,region,count,unitPrice,cost,instanceType,instanceSize,platform\ncompute,ec2,us-east-1,1,110.38,110.38,r6id,large,linux"
    return fixture


def test_export_blueprint_budget(mocker, export_blueprint_budget_fixture):
    """Test export_blueprint_budget handler."""
    fake_resp = mocker.Mock()
    fake_resp.content = mocker.Mock(return_value=export_blueprint_budget_fixture)
    fake_resp.status_code = 200
    mocker.patch("requests.get", return_value=fake_resp)

    cloudcraft = Cloudcraft(
        {"api_key": "ignore", "host": "localhost", "port": 3000, "protocol": "http"}
    )
    result = cloudcraft.export_blueprint_budget(
        "awfda35c-82fe-4edf-b9e9-ffd48f041c22", "csv", {"period": "m"}
    )

    assert result == fake_resp.content
