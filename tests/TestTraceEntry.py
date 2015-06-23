import unittest
from ..TraceEntry import TraceEntry, Condition

class TestTraceEntry(unittest.TestCase):
    def test_create_empty_TraceEntry(self):
        trace_entry = TraceEntry()
    def test_create_non_empty_TraceEntry(self):
        trace_entry = TraceEntry(('word', 'ability'))
        trace_entry = TraceEntry(('word', 'ability', 'count', '2011'))
        trace_entry = TraceEntry({'word': 'ability', 'count': '2011'})