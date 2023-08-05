# -*- coding: utf-8 -*-

import collections
import decimal

def get_object_dict(object, params=None):
    if params is not None and params['fields']:
        fields = params['fields']
    else:
        fields = [attr for attr in object.__dict__.keys() if not attr.startswith('_')]
    result = {}
    for field in fields:
        value = getattr(object, field)
        if field.startswith('date') and value is not None:
            result.update({field: value.strftime('%Y-%m-%d %H:%M:%S')})
        else:
            result.update({field: parse_value(value)})
    return result


def parse_value(value):
    return float(value) if isinstance(value, decimal.Decimal) else value


def get_multi_objects_dict(*args, params=None):
    object_group = []
    result = {}
    for object in args:
        if params is not None and params['fields']:
            fields = params['fields']
        else:
            fields = [attr for attr in object.__dict__.keys() if not attr.startswith('_')]
        row = {}
        for field in fields:
            value = getattr(object, field)
            if field.startswith('date') and value is not None:
                row.update({field: value.strftime('%Y-%m-%d %H:%M:%S')})
            else:
                row.update({field: parse_value(value)})
        object_group.append(row)

    for object in object_group:
        result.update(**object)

    return result

def dict_merge(dct, merge_dct):
    for k, v in merge_dct.items():
        if (k in dct and isinstance(dct[k], dict)
                and isinstance(merge_dct[k], collections.Mapping)):
            dict_merge(dct[k], merge_dct[k])
        else:
            dct[k] = merge_dct[k]
