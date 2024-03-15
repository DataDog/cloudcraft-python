import os

import pytest

from cloudcraftco.cloudcraft import Cloudcraft

# Warning: testing against production
# api_key must be assigned to env-variable

# required testing environment variables...
# - CLOUDCRAFT_TEST_SUBSCRIPTION
# - CLOUDCRAFT_TEST_DIRECTORY
# - CLOUDCRAFT_TEST_APPLICATION
# - CLOUDCRAFT_TEST_SECRET

cloudcraft = Cloudcraft()
test_subscription = os.environ.get("CLOUDCRAFT_TEST_SUBSCRIPTION")
test_directory = os.environ.get("CLOUDCRAFT_TEST_DIRECTORY")
test_application = os.environ.get("CLOUDCRAFT_TEST_APPLICATION")
test_secret = os.environ.get("CLOUDCRAFT_TEST_SECRET")


def test_azure_account_api():
    """Test azure account api."""
    # create azure account
    data = {
        "name": "TEST Azure Account",
        "subscriptionId": test_subscription,
        "directoryId": test_directory,
        "applicationId": test_application,
        "clientSecret": test_secret,
    }
    ccazure_created = cloudcraft.create_azure_account(data)
    assert len(ccazure_created.get("id")) == 36
    assert ccazure_created.get("name") == "TEST Azure Account"

    # assign test azure account id
    test_account_id = ccazure_created.get("id")

    # update azure account
    data = {
        "name": "UPDATED TEST Azure Account",
        "subscriptionId": test_subscription,
        "directoryId": test_directory,
        "applicationId": test_application,
    }
    ccazure_updated = cloudcraft.update_azure_account(test_account_id, data)
    assert ccazure_updated.get("name") == "UPDATED TEST Azure Account"

    # list azure accounts
    ccazure_list = cloudcraft.list_azure_accounts()
    ccazure_ids = [ccazure.get("id") for ccazure in ccazure_list.get("accounts")]
    assert test_account_id in ccazure_ids

    # snapshot azure account
    bytestring = cloudcraft.snapshot_azure_account(test_account_id, "canadaeast", "png")
    assert bytestring[0:5] == b"\x89PNG\r"

    # delete azure account
    ccazure_deleted = cloudcraft.delete_azure_account(test_account_id)
    ccazure_new_list = cloudcraft.list_azure_accounts()
    ccazure_new_ids = [
        ccazure.get("id") for ccazure in ccazure_new_list.get("accounts")
    ]
    assert ccazure_deleted == None
    assert test_account_id not in ccazure_new_ids
