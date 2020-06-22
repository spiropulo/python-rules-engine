from engine.pipeline import Engine
from tests.parent import TestParent


class TestAndOrConditions(TestParent):

    def test_FalseOr_TrueAnd_fail(self):
        d = self.d()
        a1 = self.a1()
        a1.addOrCondition(self.t()).addAndCondition(self.f())
        Engine(actions=[a1], data=d).execute()
        assert d.get("key1") is None;

    def test_TrueOr_FalseAnd_fail(self):
        d = self.d()
        a1 = self.a1()
        a1.addOrCondition(self.f()).addAndCondition(self.t())
        Engine(actions=[a1], data=d).execute()
        assert d.get("key1") is None;

    def test_TrueFalseOrs_TrueAnd_pass(self):
        d = self.d()
        a1 = self.a1()
        a1.addOrCondition(self.t()).addOrCondition(self.f()).addAndCondition(self.t())
        Engine(actions=[a1], data=d).execute()
        assert d.get("key1") == "one"

    def test_TrueFalseOrs_TrueFalseAnds_fails(self):
        d = self.d()
        a1 = self.a1()
        a1.addOrCondition(self.t()).addOrCondition(self.f()).addAndCondition(self.t()).addAndCondition(self.f())
        Engine(actions=[a1], data=d).execute()
        assert d.get("key1") is None

    def test_TrueTrueOrs_TrueFalseAnds_fails(self):
        d = self.d()
        a1 = self.a1()
        a1.addOrCondition(self.t()).addOrCondition(self.t()).addAndCondition(self.t()).addAndCondition(self.f())
        Engine(actions=[a1], data=d).execute()
        assert d.get("key1") is None

    def test_allTogether(self):
        d = self.d()
        a1 = self.a1()
        a1 = self.a1().addOrCondition(self.t()).addOrCondition(self.t()).addAndCondition(self.t()).addAndCondition(
            self.f());
        a2 = self.a2().addOrCondition(self.t()).addOrCondition(self.f()).addAndCondition(self.t());
        a3 = self.a3().addAndCondition(self.f());
        Engine(actions=[a1, a2, a3], data=d).execute()
        assert d.get("key1") is None
        assert d.get("key2") == "two"
        assert d.get("key3") is None
