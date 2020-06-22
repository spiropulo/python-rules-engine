from unittest import TestCase

from engine.action import EngineAction
from engine.condition import EngineCondition
from engine.data import EngineData
from engine.pipeline import Engine
from tests.sample import SampleCondition, SampleAction


class TestParent(TestCase):
    def d(self) -> EngineData:
        return EngineData()

    def f(self) -> EngineCondition:
        return SampleCondition(False)

    def t(self) -> EngineCondition:
        return SampleCondition(True)

    def a1(self) -> EngineAction:
        return SampleAction("key1", "one")

    def a2(self) -> EngineAction:
        return SampleAction("key2", "two")

    def a3(self) -> EngineAction:
        return SampleAction("key3", "three")

    def test_NoConditions_pass(self):
        data = EngineData()
        Engine(actions=[self.a1(), self.a2()], data=data).execute()
        assert data.get("key1") == "one"
        assert data.get("key2") == "two"
