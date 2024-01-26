import requests


def export_blueprint_budget_handler(cloudcraft, bp_id, bp_format, options=None):
    """Request blueprint budget via Cloudcraft api."""
    # /blueprint/{id}/budget/{format}
    # with: optional query parameters
    # method: get
    if options is None:
        options = {}
    api_route = "/blueprint/{}/budget/{}".format(bp_id, bp_format)
    url = cloudcraft.url_base.format(api_route)
    return requests.get(
        url,
        headers=cloudcraft.headers,
        timeout=cloudcraft.timeout_seconds,
        params=options,
    )
