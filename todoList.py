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
        self.tasks[task_num -1].complete = True

    def mark_incomplete(self, task_num: int):
        self._validate_task_num(task_num)
        self.tasks[task_num -1].complete = False

    def remove(self, task_num: int):
        self._validate_task_num(task_num)
        del self.tasks[task_num -1]

    def remove_complete(self):
        self.tasks = [task for task in self.tasks if not task.complete]
