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