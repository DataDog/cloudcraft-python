import os

import pytest

from cloudcraftco.cloudcraft import Cloudcraft

# Warning: testing against production
# api_key must be assigned to env-variable

# CLOUDCRAFT_TEST_ROLE must be available -- aws account numbers
# are semi-secret, and roles should be kept private

cloudcraft = Cloudcraft()
test_role_arn = os.environ.get("CLOUDCRAFT_TEST_ROLE")


def test_aws_account_api():
    """Test aws account api."""
    # read aws role parameters
    aws_params = cloudcraft.read_aws_role_parameters()
    assert aws_params.get("accountId") != None
    assert aws_params.get("externalId") != None

    # create aws account
    data = {"name": "TEST AWS Account", "roleArn": test_role_arn}
    ccaws_created = cloudcraft.create_aws_account(data)
    assert len(ccaws_created.get("id")) == 36
    assert ccaws_created.get("name") == "TEST AWS Account"

    # assign test aws account id
    test_account_id = ccaws_created.get("id")

    # update aws account
    data = {"name": "UPDATED TEST AWS Account", "roleArn": test_role_arn}
    ccaws_updated = cloudcraft.update_aws_account(test_account_id, data)
    assert ccaws_updated.get("name") == "UPDATED TEST AWS Account"

    # list aws accounts
    ccaws_list = cloudcraft.list_aws_accounts()
    ccaws_ids = [ccaws.get("id") for ccaws in ccaws_list.get("accounts")]
    assert test_account_id in ccaws_ids

    # snapshot aws account
    bytestring = cloudcraft.snapshot_aws_account(test_account_id, "us-west-2", "png")
    assert bytestring[0:5] == b"\x89PNG\r"

    # delete aws account
    ccaws_deleted = cloudcraft.delete_aws_account(test_account_id)
    ccaws_new_list = cloudcraft.list_aws_accounts()
    ccaws_new_ids = [ccaws.get("id") for ccaws in ccaws_new_list.get("accounts")]
    assert ccaws_deleted == None
    assert test_account_id not in ccaws_new_ids
