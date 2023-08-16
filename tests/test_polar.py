import sys
import unittest 
import tomlkit

from pathlib import Path
from collections.abc import Iterable
from types import GeneratorType
sys.path.append(str(Path(__file__).resolve().parents[1]))
from utility import PolarFlowClient
from config import PATHS


class TestPolorFlowClient(unittest.TestCase):

    def setUp(self):
        self.flow = PolarFlowClient()
        with open(PATHS.CONFIG/'credentials.toml', 'r') as f:
            credential = tomlkit.load(f)
        self.flow.login(credential['user'], credential['pw'])

    def test_iterable(self):
        self.assertIsInstance(self.flow, Iterable)
        self.assertIsInstance(iter(self.flow), GeneratorType)
        self.assertTrue(bool(next(self.flow)))

if __name__ == '__main__':
    unittest.main()
