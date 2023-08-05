#!/usr/bin/env python
from public import public
import write
import this_is
import recursion_detect


# https://pypi.org/pypi?%3Aaction=list_classifiers


def _valid(value):
    return this_is.string(value) and " :: " in value


def _prop_values(value):
    if this_is.string(value):
        if _valid(value):
            return [value]
        return []
    values = list(value)
    for value in values:
        if not _valid(value):
            return []
    return values


@public
class Classifiers:
    custom_classifiers = []

    def __init__(self, path=None, classifiers=None):
        if path:
            self.load(path)
        if classifiers:
            self.custom_classifiers = classifiers

    def load(self, path):
        for line in open(path).read().splitlines():
            if _valid(line):
                self.append(line)

    def save(self, path):
        write.write(path, "\n".join(sorted(self.classifiers)))

    def append(self, value):
        for line in value.splitlines():
            if line:
                self.custom_classifiers.append(line)
        self.custom_classifiers = list(sorted(self.custom_classifiers))

    def search(self, search):
        result = []
        for item in self.classifiers:
            if str(search).lower() in item.lower():  # case insensitive
                result.append(item)
        return list(sorted(result))

    @property
    def properties(self):
        result = []
        for key in dir(self.__class__):
            if isinstance(getattr(self.__class__, key), property):
                result.append(key)
        return result

    @property
    def prop_classifiers(self):
        if recursion_detect.depth():
            return []
        result = []
        for prop in self.properties:
            result += _prop_values(getattr(self, prop))
        return result

    @property
    def classifiers(self):
        return list(sorted(filter(None, self.custom_classifiers + self.prop_classifiers)))

    def __contains__(self, key):
        return bool(self.search(key))

    def __getitem__(self, key):
        return self.search(key)

    def __str__(self):
        return "\n".join(sorted(set(filter(None, self.classifiers))))

    def __repr__(self):
        return "<Classifiers (%s)>" % self.count
