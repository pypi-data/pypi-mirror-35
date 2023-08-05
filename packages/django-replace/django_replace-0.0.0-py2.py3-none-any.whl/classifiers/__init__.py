#!/usr/bin/env python
import cls
from public import public
import recursion_detect
import write
import this_is

# https://pypi.org/pypi?%3Aaction=list_classifiers


def _valid(value):
    return this_is.string(value) and " :: " in value


def _values(value):
    if this_is.string(value):
        if _valid(value):
            return [value]
        return []
    if hasattr(value, "__iter__"):
        value = list(value)  # store generator/list/set/tuple values to variable
        for v in value:
            if not _valid(v):
                return []
        return list(value)
    return []


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
        return self

    def save(self, path):
        write.write(path, "\n".join(self.classifiers()))
        return self

    def append(self, value):
        for line in value.splitlines():
            if line:
                self.custom_classifiers.append(line)
        self.custom_classifiers = list(sorted(self.custom_classifiers))
        return self

    def search(self, search):
        result = []
        for item in self.classifiers():
            if str(search).lower() in item.lower():  # case insensitive
                result.append(item)
        return list(sorted(result))

    def classifiers(self):
        result = list(self.custom_classifiers)  # list() required - copy items
        # print("cls.attrs(self.__class__) = %s" % cls.attrs(self.__class__))
        for key in cls.attrs(self.__class__):  # attrs
            result += _values(getattr(self, key))
        # prevent properties recursion
        if recursion_detect.depth() > 0:
            return result
        for key in cls.properties(self.__class__):  # properties
            result += _values(getattr(self, key))
        return list(sorted(set(filter(None, result))))

    def __contains__(self, key):
        return bool(self.search(key))

    def __iter__(self):
        for classifier in self.classifiers():
            yield classifier

    def __getitem__(self, key):
        return self.search(key)

    def __len__(self):
        return len(self.classifiers())

    def __str__(self):
        return "\n".join(self.classifiers())

    def __repr__(self):
        return "<Classifiers (%s)>" % self.count
