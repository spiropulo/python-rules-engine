from typing import List

from engine.action import EngineAction
from engine.condition import EngineCondition
from engine.data import EngineData
from engine.exceptions import EngineException


class Engine:
    def __init__(self, actions: List[EngineAction], data: EngineData, ors: List[EngineCondition] = None,
                 ands: List[EngineCondition] = None):
        if actions is None or len(actions) <= 0:
            raise EngineException("At least one action must be provided.")

        self.actions = actions

        if data is None:
            raise EngineException("EngineData cannot be null.")
        else:
            self.data = data

        if ors is not None:
            for a in self.actions:
                for c in ors:
                    a.addOrCondition(c)

        if ands is not None:
            for a in self.actions:
                for c in ands:
                    a.addAndCondition(c)

    def execute(self):
        for a in self.actions:
            if self._passConditions(a):
                a.execute(self.data)

    def _passConditions(self, action: EngineAction) -> bool:
        and_result: bool = True
        or_result: bool = False
        if not action.get_or_conditions() and not action.get_and_conditions():
            return True

        or_conditions: List[EngineCondition] = action.get_or_conditions()
        if len(or_conditions) == 0:
            or_result = True
        else:
            for r in or_conditions:
                if r.execute(data=self.data):
                    or_result = True
                    break

        and_conditions: List[EngineCondition] = action.get_and_conditions()
        for r in and_conditions:
            if r.execute(data=self.data) is False:
                and_result = False
                break

        return and_result and or_result
