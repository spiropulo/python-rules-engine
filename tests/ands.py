from engine.pipeline import Engine
from tests.parent import TestParent


class TestAndConditions(TestParent):
    def test_FalseAndCondition_fail(self):
        a1 = self.a1().addAndCondition(self.f())
        a2 = self.a2().addAndCondition(self.f())
        data = self.d()
        Engine(actions=[a1, a2], data=data).execute()
        assert data.get("key1") is None
        assert data.get("key2") is None

    def test_TrueAndCondition_pass(self):
        a1 = self.a1().addAndCondition(self.t())
        a2 = self.a2().addAndCondition(self.t())
        data = self.d()
        Engine(actions=[a1, a2], data=data).execute()
        assert data.get("key1") == "one"
        assert data.get("key2") == "two"

    def test_TrueFalseAndCondition_fail(self):
        a1 = self.a1().addAndCondition(self.f()).addAndCondition(self.t())
        a2 = self.a2().addAndCondition(self.f()).addAndCondition(self.t())
        data = self.d()
        Engine(actions=[a1, a2], data=data).execute()
        assert data.get("key1") is None
        assert data.get("key2") is None

    def test_TrueFalseAndCondition_2actions_1pass_2fail(self):
        a1 = self.a1().addAndCondition(self.t()).addAndCondition(self.t())
        a2 = self.a2().addAndCondition(self.f()).addAndCondition(self.t())
        data = self.d()
        Engine(actions=[a1, a2], data=data).execute()
        assert data.get("key1") == "one"
        assert data.get("key2") is None
