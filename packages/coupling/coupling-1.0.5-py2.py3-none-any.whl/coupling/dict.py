# coding: utf-8

import collections
import logging
logger = logging.getLogger(__name__)


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

    def __str__(self):
        return '<{} {}>'.format(self.__class__.__name__, super().__str__())


class AttrOrderedDict(collections.OrderedDict, AttrDict):
    pass
