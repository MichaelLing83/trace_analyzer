#!/usr/bin/env python3

import logging

class TraceEntry:
    '''
    Representing one trace entry. Initialized with one regular expression and a string.
    '''
    def __init__(self, data=None):
        self._d = dict()
        if isinstance(data, list) or isinstance(data, tuple):
            assert len(data) %2 == 0, "input list/tuple must contain pairs of key, value, but its length is {}".format(len(data))
            for i in range(int(len(data)/2)):
                self._d[data[2 * i]] = data[2 * i + 1]
        elif isinstance(data, dict):
            self._d = dict(data)
    def __getitem__(self, name):
        assert name in self._d.keys(), "Attribute {} doesn't exist, all attributes are {}".format(name, self._d.keys())
        return self._d[name]

class Condition:
    '''
    Representing the codition used to match one trace entry.
    '''
    def __init__(self):
        self._coditions = list()
    def __and__(self, condition):
        pass

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser("TraceEntry.py")
    parser.add_argument("-v", "--verbosity", help="verbosity of logging output [0..4]", action="count", default=0)
    args = parser.parse_args()
    if args.verbosity > 4:
        args.verbosity = 4
    log_lvl = (logging.CRITICAL, logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG)[args.verbosity]
    logging.basicConfig(level=log_lvl, format='%(filename)s:%(levelname)s:%(message)s')
