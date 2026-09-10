from textual.app import App, ComposeResult
from textual.screen import  ModalScreen
from textual.widgets import Input, ListView, ListItem, Checkbox, Header

from todoList import TodoList


class TaskList(ListView):

    def on_mount(self) -> None:
        self.border_title = "To Do"
        self.border_subtitle = "n-New Task r-Remove Task ^r-Remove Complete Tasks"

    def display_tasks(self, todo: TodoList) -> None:
        self.clear()
        self.extend(
                ListItem(Checkbox(task.name, task.complete))
                for task in todo    
            )
    
class NewTask(Input):

    def on_mount(self) -> None:
        self.placeholder = ">"
        self.border_title = "New Task"        


class NewTaskScreen(ModalScreen):

    BINDINGS = [
        ("ctrl+z", "cancel", "Cancel New Task")
    ]

    def compose(self) -> ComposeResult:
        yield NewTask()

    def action_cancel(self) -> None:
        self.app.pop_screen()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.dismiss(event.value)

class TodoApp(App):

    CSS_PATH = "app.tcss"
    BINDINGS = [
        ("n", "new_task", "New Task"),
        ("r", "remove_task", "Remove Task"),
        ("^r", "remove_complete", "Remove Complete Tasks")
    ]

    def __init__(
            self,
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
        yield TaskList()

    def on_mount(self) -> None:
        self.refresh_tasks()
        
        
    def action_new_task(self):
        def add(task_name: str) -> None:
            self._todo_list.add_task(task_name)
            self.refresh_tasks()

        self.push_screen(NewTaskScreen(), add)

    def action_remove_task(self):
        raise NotImplementedError

    def action_remove_complete(self):
        raise NotImplementedError

    def refresh_tasks(self):
        task_list = self.query_one("TaskList")
        task_list.display_tasks(self._todo_list)


if __name__ == "__main__":

    todo = TodoList()
    # load tasks
    try: 
        todo.load_json("todo.json") 
    except FileNotFoundError:
        pass

    app = TodoApp(todo)
    app.run()
    