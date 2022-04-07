import sys
import unittest 
from pathlib import Path
from collections.abc import Iterable
from types import GeneratorType
root = Path(__file__).resolve().parents[1]
sys.path.append(str(root))
from utility import PolarFlowClient


class TestPolorFlowClient(unittest.TestCase):

    def setUp(self):
        self.flow = PolarFlowClient()

    def test_iterable(self):
        self.assertIsInstance(self.flow, Iterable)
        self.assertIsInstance(iter(self.flow), GeneratorType)
        self.assertTrue(bool(next(self.flow)))
