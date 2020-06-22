from engine.action import EngineAction
from engine.condition import EngineCondition
from engine.data import EngineData


class SampleAction(EngineAction):
    def __init__(self, key: str, value: str):
        super().__init__()
        self.key = key
        self.value = value

    def execute(self, data: EngineData):
        data.add(self.key, self.value)


class SampleCondition(EngineCondition):
    def __init__(self, result: bool):
        super().__init__()
        self.result = result

    def execute(self, data: EngineData):
        return self.result


class SampleOutAction(EngineAction):
    def __init__(self, content: str):
        super().__init__()
        self.content = content

    def execute(self, data: EngineData):
        print(self.content)