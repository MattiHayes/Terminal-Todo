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
    
    def add_task(self, name: str):
        self.tasks.append(Task(name))

    def _validate_task_num(self, task_num: int):
        if task_num < 1:
            raise IndexError (
                f"The task number shsould be greater than 0"
            )
        if task_num > len(self.tasks):
            raise IndexError (
                f"There are {len(self.tasks)} tasks. {task_num} is out of range"
            )

    def mark_complete(self, task_num: int):
        self._validate_task_num(task_num)
        self.tasks[task_num -1].is_complete()

    def mark_incomplete(self, task_num: int):
        self._validate_task_num(task_num)
        self.tasks[task_num -1].is_incomplete()

    def remove(self, task_num: int):
        self._validate_task_num(task_num)
        del self.tasks[task_num -1]

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
