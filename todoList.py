import json
from task import Task

class TodoList:

    def __init__(self):
        self.tasks = []

    def __str__(self):
        lines = []
        for i, task in enumerate(self.tasks):
            lines.append(f"{i+1}: [{"x" if task.complete else " "}] {task.name}")
        return "\n".join(lines)

    def __len__(self):
        return len(self.tasks)

    def __iter__(self):
        return iter(self.tasks)

    def __getitem__(self, key):
        return self.tasks[key]
    
    def add_task(self, name: str):
        self.tasks.append(Task(name))

    def _validate_task_idx(self, task_idx: int):
        if task_idx < 0:
            raise IndexError (
                f"The task number shsould be >= 0"
            )
        if task_idx >= len(self.tasks):
            raise IndexError (
                f"There are {len(self.tasks)} tasks. Index {task_idx} is out of range"
            )

    def mark_complete(self, task_idx: int):
        self._validate_task_idx(task_idx)
        self.tasks[task_idx].is_complete()

    def mark_incomplete(self, task_idx: int):
        self._validate_task_idx(task_idx)
        self.tasks[task_idx].is_incomplete()

    def remove(self, task_idx: int):
        self._validate_task_idx(task_idx)
        del self.tasks[task_idx]

    def remove_complete(self):
        self.tasks = [task for task in self.tasks if not task.complete]

    def load_json(self, file: str):
        with open(file) as f:
            try:
                task_dics = json.load(f)
            except json.decoder.JSONDecodeError:
                print("Error loading tasks from json file")
                return
            
            for t in task_dics:
                self.tasks.append(Task.from_dict(t))

    def jsonify(self):
        return [task.to_dict() for task in self.tasks]
