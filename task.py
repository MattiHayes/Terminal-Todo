class Task:

    def __init__(self, name: str, complete: bool = False):
        self.name = name
        self.complete = complete

    def to_dict(self):
        return {
            "name": self.name,
            "complete": self.complete
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["name"], data["complete"])
