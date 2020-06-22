from unittest import TestCase

from engine.data import EngineData
from engine.exceptions import EngineException
from engine.pipeline import Engine
from tests.sample import SampleAction


class TestExceptions(TestCase):
    def test_EmptyActions_fail(self):
        result = None
        try:
            Engine(actions=[], data=EngineData())
        except Exception as e:
            result = e
        finally:
            assert isinstance(result, EngineException)

    def test_NullActions_fail(self):
        result = None
        try:
            Engine(actions=None, data=EngineData())
        except Exception as e:
            result = e
        finally:
            assert isinstance(result, EngineException)

    def test_NullEngineData_fail(self):
        result = None
        try:
            Engine(actions=SampleAction("key1", "one"), data=None)
        except Exception as e:
            result = e
        finally:
            assert isinstance(result, Exception)
