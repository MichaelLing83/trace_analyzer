#!/usr/bin/env python3

import logging

class TraceEntry(dict):
    '''
    Representing one trace entry. Initialized with one regular expression and a string.
    '''
    def __init__(self, key=None):
        pass

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
