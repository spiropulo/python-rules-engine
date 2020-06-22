# Python Rules Engine

This ultra-light-weight rules engine provides an **alternative computational** model and not the usual imperative structures. These structures make it easy to follow a consistent and well understood execution strategy. Development teams can then speak in common terms building **ubiquitous language** around software constitution.

The spirit of this artifact is to assist engineering teams with a common pattern that can be leverage across the enterprise. It is **completely** unopinionated, in terms of frameworks. It introduces no new dependencies to an application stack.


## Hello World Example (without conditions)

This is a simple example to show how the Engine executes EngineActions.

```diff
+ This simple action will be added to our execution pipeline.
```
```python
from engine.action import EngineAction
from engine.data import EngineData

class SampleOutAction(EngineAction):
    def __init__(self, content: str):
        super().__init__()
        self.content = content

    def execute(self, data: EngineData):
        print(self.content)
```
```diff
+ Now we put it all together
```
```python
from unittest import TestCase

from engine.data import EngineData
from engine.pipeline import Engine
from tests.sample import SampleOutAction


class TestHelloWorld(TestCase):

    def test_helloWorld(self):
        Engine(actions=[SampleOutAction(content="Hello World!")], data=EngineData()).execute()

```
```diff
+ After running this test your output should look something like this:
  Hello World!
```

## Hello World Example (with AND conditions)

This example shows how an EngineAction executes with AND conditions. All of the AND conditions must pass for an action to execute. We can attach an unlimited number of AND conditions to any action (You should consider performance!). We can also pass AND conditions to an ExecutionPipeline. These conditions will be invoked before each action in the pipeline is executed, and they will adhere to the statute of AND conditions execution. 

```diff
+ Here is our sample condition.
```
```python
from engine.condition import EngineCondition
from engine.data import EngineData


class SampleCondition(EngineCondition):
    def __init__(self, result: bool):
        super().__init__()
        self.result = result

    def execute(self, data: EngineData):
        return self.result
```
We are going to first set the condition to return true, so Hello World! will execute. Then we'll set it to false to prevent execution. Then we'll set back to true and pass a **general** ExecutionPipeline condition, we'll set this condition to false to prevent execution.
```python
from unittest import TestCase

from engine.data import EngineData
from engine.pipeline import Engine
from tests.sample import SampleOutAction, SampleCondition


class TestHelloWorld(TestCase):
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
```
# Hello World Example (with OR conditions)
This example shows how an EngineAction executes with OR conditions. At least one of the OR conditions must pass for a action to execute. We can attach an unlimited number of OR conditions to any action (You should consider performance!). We can also pass OR conditions to an ExecutionPipeline. These conditions will be invoked before each action in the pipeline is executed, and they will adhere to the statute of OR conditions execution.

```python
from unittest import TestCase

from engine.data import EngineData
from engine.pipeline import Engine
from tests.sample import SampleOutAction, SampleCondition


class TestHelloWorld(TestCase):
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
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

