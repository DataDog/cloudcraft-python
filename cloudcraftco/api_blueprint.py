import requests


def list_blueprints_handler(cloudcraft):
    """List blueprint records via Cloudcraft api."""
    # /blueprint
    # method: get
    api_route = "/blueprint"
    url = cloudcraft.url_base.format(api_route)
    return requests.get(
        url, headers=cloudcraft.headers, timeout=cloudcraft.timeout_seconds
    )


def create_blueprint_handler(cloudcraft, data):
    """Create blueprint record via Cloudcraft api."""
    # /blueprint
    # method: post
    api_route = "/blueprint"
    url = cloudcraft.url_base.format(api_route)
    return requests.post(
        url, json=data, headers=cloudcraft.headers, timeout=cloudcraft.timeout_seconds
    )


def read_blueprint_handler(cloudcraft, blueprint_id):
    """Read blueprint record via Cloudcraft api."""
    # /blueprint/{id}
    # method: get
    api_route = "/blueprint/" + blueprint_id
    url = cloudcraft.url_base.format(api_route)
    return requests.get(
        url, headers=cloudcraft.headers, timeout=cloudcraft.timeout_seconds
    )


def update_blueprint_handler(cloudcraft, blueprint_id, data):
    """Update blueprint record via Cloudcraft api."""
    # /blueprint/{id}
    # method: put
    api_route = "/blueprint/" + blueprint_id
    url = cloudcraft.url_base.format(api_route)
    return requests.put(
        url, json=data, headers=cloudcraft.headers, timeout=cloudcraft.timeout_seconds
    )


def delete_blueprint_handler(cloudcraft, blueprint_id):
    """Delete blueprint record via Cloudcraft api."""
    # /blueprint/{id}
    # method: delete
    api_route = "/blueprint/" + blueprint_id
    url = cloudcraft.url_base.format(api_route)
    return requests.delete(
        url, headers=cloudcraft.headers, timeout=cloudcraft.timeout_seconds
    )


def export_blueprint_handler(cloudcraft, bp_id, bp_format, options=None):
    """Request blueprint export via Cloudcraft api."""
    # /blueprint/{id}/{format}
    # with: optional query parameters
    # method: get
    # format in ["svg", "png", "pdf", "mxGraph"]
    # options is dist of optional parameters
    if options is None:
        options = {}
    api_route = "/blueprint/{}/{}".format(bp_id, bp_format)
    url = cloudcraft.url_base.format(api_route)
    return requests.get(
        url,
        headers=cloudcraft.headers,
        timeout=cloudcraft.timeout_seconds,
        params=options,
    )
