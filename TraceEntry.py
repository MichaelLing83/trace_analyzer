#!/usr/bin/env python3

import logging
import re

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
    OPS = ('contain', 'match', 'gt', 'lt', 'eq', 'ge', 'le')
    BIAS = 0.000000001
    def __init__(self, key, op, value):
        assert isinstance(key, str), "key must be a string, but '{}' is of type {}".format(key, type(key))
        assert op in Condition.OPS, "op={} is not one of the supported: {}".format(op, Condition.OPS)
        self.key = str(key)
        self.op = op
        self.value = str(value)
    def test(self, trace_entry):
        assert isinstance(trace_entry, TraceEntry), "must use an TraceEntry, get {} instead".format(type(trace_entry))
        value = str(trace_entry[self.key])
        if self.op == 'contain':
            return self.value in value
        elif self.op == 'match':
            if re.search(self.value, value):
                return True
            else:
                return False
        elif self.op == 'gt':
            return float(value) > float(self.value)
        elif self.op == 'lt':
            return float(value) < float(self.value)
        elif self.op == 'eq':
            return abs(float(self.value) - float(value)) < Condition.BIAS
        elif self.op == 'ge':
            return float(value) >= float(self.value)
        elif self.op == 'le':
            return float(value) <= float(self.value)
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
