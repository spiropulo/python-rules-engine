from abc import ABC, abstractmethod
from typing import List

from engine.condition import EngineCondition
from engine.data import EngineData
from engine.exceptions import ActionException


class EngineAction(ABC):
    def __init__(self):
        super().__init__()
        self._andConditions: List[EngineCondition] = list()
        self._orConditions: List[EngineCondition] = list()

    def addAndCondition(self, condition: EngineCondition):
        if condition is None:
            raise ActionException("Can't add null condition")
        self._andConditions.append(condition)
        return self

    def addOrCondition(self, condition: EngineCondition):
        if condition is None:
            raise ActionException("Can't add null condition")
        self._orConditions.append(condition)
        return self

    def get_and_conditions(self) -> List[EngineCondition]:
        return self._andConditions

    def get_or_conditions(self) -> List[EngineCondition]:
        return self._orConditions

    @abstractmethod
    def execute(self, data: EngineData):
        pass
