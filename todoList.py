from task import Task

class TodoList:

    def __init__(self):
        self.tasks = []

    def __str__(self):
        out = ""
        for i, task in enumerate(self.tasks):
            task_str = (f"{i+1}: [{"x" if task.complete else " "}] " +
            f"{task.name}{"\n" if i != len(self.tasks)-1 else ""}")
            out = out + task_str
        return out

    def __len__(self):
        return len(self.tasks)

    @property
    def number_of_tasks(self):
        return len(self.tasks) + 1

    def add_task(self, name: str):
        self.tasks.append(Task(name))

    def mark_complete(self, task_num: int):
        if task_num < 1 or task_num > len(self.tasks):
            raise(IndexError(f"Task number {task_num} was given but the" +
                             f"todo list has {len(self.tasks)} tasks"))
        if not self.tasks[task_num -1].complete:
            self.tasks[task_num -1].toggle()

    def mark_incomplete(self, task_num: int):
            if task_num < 1 or task_num > len(self.tasks):
                raise(IndexError(f"Task number {task_num} was given but the" +
                                 f"todo list has {len(self.tasks)} tasks"))
            if self.tasks[task_num -1].complete:
                self.tasks[task_num -1].toggle()

    def remove(self, task_num: int):
        if task_num < 1 or task_num > len(self.tasks):
            raise(IndexError(f"Task number {task_num} was given but the" +
                f"todo list has {len(self.tasks)} tasks"))
        del self.tasks[task_num -1]

    def remove_complete(self):
        incomplete = []
        for task in self.tasks:
            if not task.complete:
                incomplete.append(task)
        self.tasks = incomplete
