class Task:

    def __init__(self, name: str, complete: bool = False):
        self.name = name
        self._complete = complete

    def to_dict(self):
        return {
            "name": self.name,
            "complete": self.complete
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["name"], data["complete"])

    @property
    def complete(self):
        return self._complete

    @complete.setter
    def complete(self, state: bool):
        if type(state) != bool:
            raise ValueError(
                f"Expecting type 'bool' for state but got {type(state)}"
                )
        self._complete = state

    def is_complete(self):
        self._complete = True

    def is_incomplete(self):
        self._complete = False