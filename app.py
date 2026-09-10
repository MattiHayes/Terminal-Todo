from textual.app import App, ComposeResult
from textual.widgets import Input, ListView, Checkbox, Header

from todoList import TodoList


class TaskList(ListView):

    def on_mount(self) -> None:
        self.border_title = "To Do"
        self.border_subtitle = "n-New Task r-Remove Task ^r-Remove Complete Tasks"

    
class NewTask(Input):

    def on_mount(self) -> None:
        self.placeholder = ">"
        self.border_title = "New Task"        

    def compose(self) -> ComposeResult:
        return super().compose()

class TodoApp(App):

    CSS_PATH = "app.tcss"
    BINDINGS = [
        ("n", "new_task", "New Task"),
        ("r", "remove_task", "Remove Task"),
        ("^r", "remove_complete", "Remove Complete Tasks")
    ]

    def __init__(self,
                 todo : TodoList,
                 driver_class = None, 
                 css_path = None, 
                 watch_css = False, 
                 ansi_color = None
        ):
        self._todo_list = todo
        super().__init__(driver_class, css_path, watch_css, ansi_color)

    def compose(self) -> ComposeResult:
        yield Header()
        yield TaskList(id="tasks")

    def on_mount(self) -> None:
        task_list = self.query_one("TaskList")
        for task in self._todo_list:
            task_list.append(
                Checkbox(task.name, task.complete) 
            )
        
    def action_new_task(self):
        raise NotImplementedError

    def action_remove_task(self):
        raise NotImplementedError

    def action_remove_complete(self):
        raise NotImplementedError



if __name__ == "__main__":

    todo = TodoList()
    # load tasks
    try: 
        todo.load_json("todo.json") 
    except FileNotFoundError:
        pass

    app = TodoApp(todo)
    app.run()
    