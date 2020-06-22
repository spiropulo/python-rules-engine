from engine.pipeline import Engine
from tests.parent import TestParent


class TestOrConditions(TestParent):
    def test_FalseOrCondition_fail(self):
        a1 = self.a1().addOrCondition(self.f())
        a2 = self.a2().addOrCondition(self.f())
        data = self.d()
        Engine(actions=[a1, a2], data=data).execute()
        assert data.get("key1") is None
        assert data.get("key2") is None

    def test_TrueOrCondition_pass(self):
        a1 = self.a1().addOrCondition(self.t())
        a2 = self.a2().addOrCondition(self.t())
        data = self.d()
        Engine(actions=[a1, a2], data=data).execute()
        assert data.get("key1") == "one"
        assert data.get("key2") == "two"

    def test_TrueFalseOrs_pass(self):
        a1 = self.a1().addOrCondition(self.t()).addOrCondition(self.f())
        a2 = self.a2().addOrCondition(self.t()).addOrCondition(self.f())
        data = self.d()
        Engine(actions=[a1, a2], data=data).execute()
        assert data.get("key1") == "one"
        assert data.get("key2") == "two"

    def test_FalseFalseOrs_fail(self):
        a1 = self.a1().addOrCondition(self.f()).addOrCondition(self.f())
        a2 = self.a2().addOrCondition(self.f()).addOrCondition(self.f())
        data = self.d()
        Engine(actions=[a1, a2], data=data).execute()
        assert data.get("key1") is None
        assert data.get("key2") is None

    def test_FalseFalse_FalseTrue_Ors_Condition_2actions_fail_pass(self):
        a1 = self.a1().addOrCondition(self.f()).addOrCondition(self.f())
        a2 = self.a2().addOrCondition(self.f()).addOrCondition(self.t())
        data = self.d()
        Engine(actions=[a1, a2], data=data).execute()
        assert data.get("key1") is None
        assert data.get("key2") == "two"
