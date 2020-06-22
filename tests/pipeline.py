from engine.pipeline import Engine
from tests.parent import TestParent


class TestPipelineEngine(TestParent):
    def test_engine_pipeline_False_fail(self):
        d = self.d()
        Engine(actions=[self.a1()], data=d, ands=[self.f()]).execute()
        assert d.get("key1") is None

    def test_engine_pipeline_TrueFalse_fail(self):
        d = self.d()
        Engine(actions=[self.a1()], data=d, ands=[self.f(), self.t()]).execute()
        assert d.get("key1") is None

    def test_engine_pipeline_True_pass(self):
        d = self.d()
        Engine(actions=[self.a1()], data=d, ands=[self.t()]).execute()
        assert d.get("key1") == "one"

    def test_engine_pipeline_TrueFalse_2actions_fail(self):
        d = self.d()
        Engine(actions=[self.a1(), self.a2()], data=d, ands=[self.f(), self.t()]).execute()
        assert d.get("key1") is None
        assert d.get("key2") is None

    def test_engine_pipeline_pass(self):
        d = self.d()
        Engine(actions=[self.a1(), self.a2(), self.a3()], data=d, ands=[self.f(), self.t()]).execute()
        assert d.get("key1") is None
        assert d.get("key2") is None
        assert d.get("key3") is None

    def test_engine_pipeline_fail_pass_fail(self):
        d = self.d()
        a2 = self.a2().addOrCondition(self.t())
        Engine(actions=[self.a1(), a2, self.a3()], data=d, ors=[self.f()], ands=[self.t()]).execute()
        assert d.get("key1") is None
        assert d.get("key2") == "two"
        assert d.get("key3") is None

    def test_engine_pipeline_fail_pass_pass(self):
        d = self.d()
        a2 = self.a2().addOrCondition(self.t())
        a3 = self.a3().addOrCondition(self.t())
        Engine(actions=[self.a1(), a2, a3], data=d, ors=[self.f()], ands=[self.t()]).execute()
        assert d.get("key1") is None
        assert d.get("key2") == "two"
        assert d.get("key3") == "three"

    def test_engine_pipeline_fail_fail_pass(self):
        d = self.d()
        a1 = self.a1().addOrCondition(self.t()).addAndCondition(self.f())
        a2 = self.a2().addOrCondition(self.t()).addAndCondition(self.f())
        a3 = self.a3().addOrCondition(self.t())
        Engine(actions=[a1, a2, a3], data=d, ors=[self.f()], ands=[self.t()]).execute()
        assert d.get("key1") is None
        assert d.get("key2") is None
        assert d.get("key3") == "three"

    def test_engine_pipeline_TrueFalseOr_TrueTrueAnd_2actions_pass(self):
        d = self.d()
        Engine(actions=[self.a1(), self.a2()], data=d, ors=[self.f(), self.t()], ands=[self.t(), self.t()]).execute()
        assert d.get("key1") == "one"
        assert d.get("key2") == "two"

    def test_engine_pipeline_FalseFalseOr_TrueTrueAnd_2actions_fail(self):
        d = self.d()
        Engine(actions=[self.a1(), self.a2()], data=d, ors=[self.f(), self.f()], ands=[self.t(), self.t()]).execute()
        assert d.get("key1") is None
        assert d.get("key2") is None

    def test_engine_pipeline_TrueTrueOr_TrueFalseAnd_2actions_fail(self):
        d = self.d()
        Engine(actions=[self.a1(), self.a2()], data=d, ors=[self.t(), self.t()], ands=[self.f(), self.t()]).execute()
        assert d.get("key1") is None
        assert d.get("key2") is None

    def test_TrueOr_general_FalseOr_TrueAnd_pass(self):
        d = self.d()
        a1 = self.a1().addOrCondition(self.t())
        Engine(actions=[a1], data=d, ors=[self.f()], ands=[self.t()]).execute()
        assert d.get("key1") == "one"

    def test_FalseAnd_general_TrueOr_TrueAnd_fail(self):
        d = self.d()
        a1 = self.a1().addAndCondition(self.f())
        Engine(actions=[a1], data=d, ors=[self.t()], ands=[self.t()]).execute()
        assert d.get("key1") is None

    def test_engine_pipeline_False_fail(self):
        d = self.d()
        Engine(actions=[self.a1()], data=d, ors=[self.f()]).execute()
        assert d.get("key1") is None

    def test_engine_pipeline_TrueFalse_pass(self):
        d = self.d()
        Engine(actions=[self.a1()], data=d, ors=[self.f(), self.t()]).execute()
        assert d.get("key1") == "one"

    def test_engine_pipeline_True_pass(self):
        d = self.d()
        Engine(actions=[self.a1()], data=d, ors=[self.t()]).execute()
        assert d.get("key1") == "one"

    def test_engine_pipeline_TrueFalse_2actions_fail(self):
        d = self.d()
        Engine(actions=[self.a1(), self.a2()], data=d, ors=[self.f(), self.t()]).execute()
        assert d.get("key1") == "one"
        assert d.get("key2") == "two"

