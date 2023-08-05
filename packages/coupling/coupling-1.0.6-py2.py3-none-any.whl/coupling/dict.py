# coding: utf-8

import collections
import logging
from .jsonpath import search

logger = logging.getLogger(__name__)


def omit(d: dict, *keys):
    new = d.__class__()
    for k, v in d.items():
        if k not in keys:
            new[k] = v
    return new


def pick(d: dict, *keys):
    new = d.__class__()
    for k, v in d.items():
        if k in keys:
            new[k] = v
    return new


class AttrDict(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as err:
            raise AttributeError(err)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as err:
            raise AttributeError(err)

    def omit(self, *keys):
        return omit(self, *keys)

    def pick(self, *keys):
        return pick(self, *keys)

    def find(self, path, *args, **kwargs):
        return search(path, self, *args, **kwargs)


class AttrOrderedDict(collections.OrderedDict, AttrDict):
    pass
