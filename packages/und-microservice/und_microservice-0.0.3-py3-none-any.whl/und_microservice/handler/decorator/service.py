# -*- coding: utf-8 -*-
import falcon
from functools import wraps


def service_validator(method):
    @wraps(method)
    def method_wrapper(*args, **kwargs):
        if args[0].service is None:
            raise falcon.HTTPError('Application Services is Null')
        return method(*args, **kwargs)
    return method_wrapper
