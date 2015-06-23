import unittest
from ..TraceEntry import TraceEntry, Condition

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
        c = Condition('word', 'contain', 'ty')
        c = Condition('word', 'match', '.*ty$')
        c = Condition('count', 'gt', 2000)
        c = Condition('count', 'eq', 2000)
        c = Condition('count', 'lt', 2000)
        c = Condition('count', 'ge', 2000)
        c = Condition('count', 'le', 2000)
    def test_condition(self):
        t = TraceEntry({'word': 'ability', 'count': '2011'})
        c = Condition('word', 'contain', 'ty')
        assert c.test(t) == True
        c = Condition('word', 'match', '.*ty$')
        assert c.test(t) == True
        c = Condition('count', 'gt', 2000)
        assert c.test(t) == True
        c = Condition('count', 'eq', 2000)
        assert c.test(t) == False
        c = Condition('count', 'lt', 2000)
        assert c.test(t) == False
        c = Condition('count', 'ge', 2000)
        assert c.test(t) == True
        c = Condition('count', 'le', 2000)
        assert c.test(t) == False
    def test_combine_Condition(self):
        assert isinstance(Condition('word', 'contain', 'ty') & Condition('word', 'match', '.*ty$'), Condition)
        assert isinstance(Condition('count', 'gt', 2000) | Condition('count', 'eq', 2000), Condition)