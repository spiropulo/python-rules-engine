from unittest import TestCase

from engine.data import EngineData
from engine.pipeline import Engine
from tests.sample import SampleOutAction, SampleCondition


class TestHelloWorld(TestCase):

    def test_helloWorld(self):
        Engine(actions=[SampleOutAction(content="Hello World!")], data=EngineData()).execute()

    def test_hello_world_and(self):
        # First set the condition to true so we see Hello World! in the out put.
        actionPass = SampleOutAction("I have a true action condition... Hello World!")
        actionPass.addAndCondition(SampleCondition(True))
        Engine(actions=[actionPass], data=EngineData()).execute()

        # output: I have a true action condition... Hello World!

        # Now we set the condition to false to prevent SampleAction from execution.
        actionFail = SampleOutAction("I have a false condition...")
        actionFail.addAndCondition(SampleCondition(False))
        Engine(actions=[actionFail], data=EngineData()).execute()

        # No output.

        # Now back to true but with a EnginePipeline condition set to false.
        actionFailWithGeneralCondition1 = SampleOutAction(
            "I have a true action condition but a false pipeline condition...")
        actionFailWithGeneralCondition1.addAndCondition(SampleCondition(True))
        Engine(actions=[actionFailWithGeneralCondition1], data=EngineData(), ands=[SampleCondition(False)]).execute()

        # No output.

        # Now back to true but with a EnginePipeline condition set to true.
        actionFailWithGeneralCondition2 = SampleOutAction(
            "I have a true action condition and a true pipeline condition... Hello World!")
        actionFailWithGeneralCondition2.addAndCondition(SampleCondition(True))
        Engine(actions=[actionFailWithGeneralCondition2], data=EngineData(), ands=[SampleCondition(True)]).execute()

        # output: I have a true action condition and a true pipeline condition... Hello World!

    def test_hello_world_or(self):
        # First set one condition true and one false...
        actionPass = SampleOutAction("I have 2 conditions true and false... Hello World!")
        actionPass.addOrCondition(SampleCondition(True)).addOrCondition(SampleCondition(True))
        Engine(actions=[actionPass], data=EngineData()).execute()

        # output: I have 2 conditions true and false... Hello World!

        # Then we set both conditions false
        actionFail = SampleOutAction("I have 2 conditions false and false... Hello World!")
        actionFail.addOrCondition(SampleCondition(False)).addOrCondition(SampleCondition(False))
        Engine(actions=[actionFail], data=EngineData()).execute()

        # No output.

        # Then we set both conditions false, and we pass a pipeline true condition...
        actionPassWithGeneralCondition = SampleOutAction(
            "I have 2 conditions false and false, with a true pipeline condition... Hello World!")
        actionPassWithGeneralCondition.addOrCondition(SampleCondition(False)).addOrCondition(SampleCondition(False))
        Engine(actions=[actionPassWithGeneralCondition], data=EngineData(), ors=[SampleCondition(True)]).execute()

        # output: I have 2 conditions false and false, with a true pipeline condition... Hello World!
