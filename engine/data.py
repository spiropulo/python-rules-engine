from typing import Any


class EngineData:
    def __init__(self):
        self.data = dict()

    def add(self, key: str, value: Any):
        self.data.update({key: value})
        return self

    def get(self, key: str) -> Any:
        return self.data.get(key)