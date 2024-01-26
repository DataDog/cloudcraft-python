# define cloudcraft exception classes


class CloudcraftMalformed(Exception):
    pass


class CloudcraftUnauthorized(Exception):
    pass


class CloudcraftForbidden(Exception):
    pass


class CloudcraftMissingResource(Exception):
    pass


class CloudcraftOutdatedResource(Exception):
    pass


class CloudcraftUnexpected(Exception):
    pass


class CloudcraftRateLimiting(Exception):
    pass
