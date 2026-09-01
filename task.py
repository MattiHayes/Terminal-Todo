class Task:

    def __init__(self, name: str):
        self.name = name
        self.complete = False

    def toggle(self):
        self.complete= not self.complete
    