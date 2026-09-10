class Task:

    def __init__(self, name: str, complete: bool = False):
        self._name = name
        self._complete = complete

    def to_dict(self):
        return {
            "name": self._name,
            "complete": self._complete
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

    @property
    def name(self):
        return self._name

    def is_complete(self):
        self._complete = True

    def is_incomplete(self):
        self._complete = False