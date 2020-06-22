from abc import ABC, abstractmethod

from engine.data import EngineData


class EngineCondition(ABC):
    @abstractmethod
    def execute(self, data: EngineData):
        pass
