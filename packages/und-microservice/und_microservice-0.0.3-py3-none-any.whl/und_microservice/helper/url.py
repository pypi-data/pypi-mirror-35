# -*- coding: utf-8 -*-


def split_query_string(items):
    params = {'filter': {}, 'fields': [], 'pagination': {}, 'sort': {}, 'filter_in': {}}
    for key, value in items:
        sub_keys = key.split('.')
        if 'fields' in sub_keys:
            params['fields'] = [value] if isinstance(value, str) else value
        elif sub_keys[0] in params:
            params[sub_keys[0]].update({sub_keys[1]: value})

    params['filter_in'] = get_filter_in(params['filter'])
    params['sort'] = ', '.join("{0} {1}".format(key, val.upper()) for (key, val) in params['sort'].items())

    if params['pagination']:
        params['pagination']['page'] = int(params['pagination']['page']) if 'page' in params['pagination'] else 1
        params['pagination']['limit'] = int(params['pagination']['limit']) if 'limit' in params['pagination'] else 100
        params['pagination'].update({'offset': (params['pagination']['page'] * params['pagination']['limit']) - params['pagination']['limit']})
    return params


def join_query_string():
    pass


def get_filter_in(filters):
    filter_in = {}
    for filter, value in list(filters.items()):
        if isinstance(value, list):
            filter_in.update({filter: value})
            del(filters[filter])
    return filter_in
