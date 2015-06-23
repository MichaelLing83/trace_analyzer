import unittest
from ..TraceEntry import TraceEntry
from ..TraceEntry import Condition as C

class TestTraceEntry(unittest.TestCase):
    def test_create_empty_TraceEntry(self):
        trace_entry = TraceEntry()
    def test_create_non_empty_TraceEntry(self):
        trace_entry = TraceEntry(('word', 'ability'))
        trace_entry = TraceEntry(('word', 'ability', 'count', '2011'))
        trace_entry = TraceEntry({'word': 'ability', 'count': '2011'})
    def test_access_TraceEntry(self):
        trace_entry = TraceEntry(('word', 'ability'))
        assert trace_entry['word'] == 'ability'
        trace_entry = TraceEntry(('word', 'ability', 'count', '2011'))
        assert trace_entry['word'] == 'ability'
        assert trace_entry['count'] == '2011'
        trace_entry = TraceEntry({'word': 'ability', 'count': '2011'})
        assert trace_entry['word'] == 'ability'
        assert trace_entry['count'] == '2011'

class TestCondition(unittest.TestCase):
    #def test_create_empty_Condition(self):
        #c = Condition()
    def test_create_non_empty_Condition(self):
        c = C('word', 'contain', 'ty')
        c = C('word', 'match', '.*ty$')
        c = C('count', 'gt', 2000)
        c = C('count', 'eq', 2000)
        c = C('count', 'lt', 2000)
        c = C('count', 'ge', 2000)
        c = C('count', 'le', 2000)
    def test_condition(self):
        t = TraceEntry({'word': 'ability', 'count': '2011'})
        c = C('word', 'contain', 'ty')
        assert c.test(t) == True
        c = C('word', 'match', '.*ty$')
        assert c.test(t) == True
        c = C('count', 'gt', 2000)
        assert c.test(t) == True
        c = C('count', 'eq', 2000)
        assert c.test(t) == False
        c = C('count', 'lt', 2000)
        assert c.test(t) == False
        c = C('count', 'ge', 2000)
        assert c.test(t) == True
        c = C('count', 'le', 2000)
        assert c.test(t) == False
    def test_combine_Condition(self):
        assert isinstance(C('word', 'contain', 'ty') & C('word', 'match', '.*ty$'), C)
        assert isinstance(C('count', 'gt', 2000) | C('count', 'eq', 2000), C)
    def test_use_combine_Condition(self):
        t = TraceEntry({'word': 'ability', 'count': '2011'})
        c = C('word', 'contain', 'ty') & C('word', 'match', '.*ty$')
        assert c.test(t) == True
        c = C('count', 'gt', 2000) | C('count', 'eq', 2000)
        assert c.test(t) == True
        assert (C('word', 'contain', 'xx') & C('count', 'lt', 3000)).test(t) == False
        assert (C('word', 'contain', 'xx') | C('count', 'lt', 100)).test(t) == False