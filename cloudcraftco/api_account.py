import requests


def list_aws_accounts_hander(cloudcraft):
    """List AWS account records via Cloudcraft api."""
    # /aws/account
    # method: get
    api_route = "/aws/account"
    url = cloudcraft.url_base.format(api_route)
    return requests.get(
        url, headers=cloudcraft.headers, timeout=cloudcraft.timeout_seconds
    )


def create_aws_account_handler(cloudcraft, data):
    """Create AWS account record via Cloudcraft api."""
    # /aws/account
    # method: post
    api_route = "/aws/account"
    url = cloudcraft.url_base.format(api_route)
    return requests.post(
        url, json=data, headers=cloudcraft.headers, timeout=cloudcraft.timeout_seconds
    )


def update_aws_account_handler(cloudcraft, account_id, data):
    """Update AWS account record via Cloudcraft api."""
    # /aws/account/{id}
    # method: put
    api_route = "/aws/account/" + account_id
    url = cloudcraft.url_base.format(api_route)
    return requests.put(
        url, json=data, headers=cloudcraft.headers, timeout=cloudcraft.timeout_seconds
    )


def delete_aws_account_handler(cloudcraft, account_id):
    """Delete AWS account record via Coudcraft api."""
    # /aws/account/{id}
    # method: delete
    api_route = "/aws/account/" + account_id
    url = cloudcraft.url_base.format(api_route)
    return requests.delete(
        url, headers=cloudcraft.headers, timeout=cloudcraft.timeout_seconds
    )


def read_aws_role_parameters_handler(cloudcraft):
    """Request AWS role parameters via Cloudcraft api."""
    # /aws/account/iamParameters
    # method: get
    api_route = "/aws/account/iamParameters"
    url = cloudcraft.url_base.format(api_route)
    return requests.get(
        url, headers=cloudcraft.headers, timeout=cloudcraft.timeout_seconds
    )


def snapshot_aws_account_handler(
    cloudcraft, account_id, region, ss_format, options=None
):
    """Request AWS account snapshot via Cloudcraft api."""
    # /aws/account/{id}/{region}/{format}
    # with: optional query parameters
    # method: get
    # region: aws region, e.g. "us-east-2"
    # format in ["json", "svg", "png", "pdf", "mxGraph"]
    # options is dist of optional parameters
    if options is None:
        options = {}
    api_route = "/aws/account/{}/{}/{}".format(account_id, region, ss_format)
    url = cloudcraft.url_base.format(api_route)
    return requests.get(
        url,
        headers=cloudcraft.headers,
        timeout=cloudcraft.timeout_seconds,
        params=options,
    )


def list_azure_accounts_handler(cloudcraft):
    """List Azure account records via Cloudcraft api."""
    # /azure/account
    # method: get
    api_route = "/azure/account"
    url = cloudcraft.url_base.format(api_route)
    return requests.get(
        url, headers=cloudcraft.headers, timeout=cloudcraft.timeout_seconds
    )


def create_azure_account_handler(cloudcraft, data):
    """Create Azure account record via Cloudcraft api."""
    # /azure/account
    # method: post
    api_route = "/azure/account"
    url = cloudcraft.url_base.format(api_route)
    return requests.post(
        url, json=data, headers=cloudcraft.headers, timeout=cloudcraft.timeout_seconds
    )


def update_azure_account_handler(cloudcraft, account_id, data):
    """Update Azure account record via Cloudcraft api."""
    # /azure/account/{id}
    # method: put
    api_route = "/azure/account/" + account_id
    url = cloudcraft.url_base.format(api_route)
    return requests.put(
        url, json=data, headers=cloudcraft.headers, timeout=cloudcraft.timeout_seconds
    )


def delete_azure_account_handler(cloudcraft, account_id):
    """Delete Azure account record via Coudcraft api."""
    # /azure/account/{id}
    # method: delete
    api_route = "/azure/account/" + account_id
    url = cloudcraft.url_base.format(api_route)
    return requests.delete(
        url, headers=cloudcraft.headers, timeout=cloudcraft.timeout_seconds
    )


def snapshot_azure_account_handler(
    cloudcraft, account_id, location, ss_format, options=None
):
    """Request Azure account snapshot via Cloudcraft api."""
    # /azure/account/{id}/{location}/{format}
    # with: optional query parameters
    # method: get
    # location: azure location, e.g. "eastus"
    # format in ["json", "svg", "png", "pdf", "mxGraph"]
    # options is dist of optional parameters
    if options is None:
        options = {}
    api_route = "/azure/account/{}/{}/{}".format(account_id, location, ss_format)
    url = cloudcraft.url_base.format(api_route)
    return requests.get(
        url,
        headers=cloudcraft.headers,
        timeout=cloudcraft.timeout_seconds,
        params=options,
    )
