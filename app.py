from textual.app import App, ComposeResult
from textual.screen import  ModalScreen
from textual.widgets import Input, ListView, ListItem, Checkbox, Header, Log, Label

from todoList import TodoList


class TaskList(ListView):

    def on_mount(self) -> None:
        self.border_title = "To Do"
        self.border_subtitle = "n-New Task r-Remove Task ^r-Remove Complete Tasks"

    def display_tasks(self, todo: TodoList) -> None:
        self.clear()

        tasks = []
        for task in todo:
            status = " " 
            if task.complete:
                status = "x"

            tasks.append(
                ListItem(
                    Label(f"\[{status}] {task.name}")
                    )
                )
        self.extend(tasks)

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

class CustomLog(Log):

    def on_mount(self):
        self.border_title = "Log"
        return super().on_mount()

class TodoApp(App):

    CSS_PATH = "app.tcss"
    BINDINGS = [
        ("n", "new_task", "New Task"),
        ("r", "remove_task", "Remove Task"),
        ("ctrl+r", "remove_complete", "Remove Complete Tasks")
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
        yield CustomLog()

    def on_mount(self) -> None:
        self.refresh_tasks()
        
        
    def action_new_task(self):
        def add(task_name: str) -> None:
            self._todo_list.add_task(task_name)
            self.refresh_tasks()
            self.log_line(f"Added new task: \"{task_name}\"")
        self.push_screen(NewTaskScreen(), add)

    def action_remove_task(self):
        raise NotImplementedError

    def action_remove_complete(self):
        self._todo_list.remove_complete()
        self.refresh_tasks()
        self.log_line(f"Removed all complete tasks")

    def refresh_tasks(self):
        task_list = self.query_one("TaskList")
        task_list.display_tasks(self._todo_list)

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        # change task complete status
        task = self._todo_list[event.index]
  
        if task.complete:
            task.is_incomplete()
            self.log_line(f"Task \"{task.name}\" marked incomplete.")
        else:
            task.is_complete()
            self.log_line(f"Task \"{task.name}\" marked complete.")
        self.refresh_tasks()

    def log_line(self, msg: str) -> None:
        log = self.query_one(CustomLog)
        log.write_line("> " + msg)



if __name__ == "__main__":

    todo = TodoList()
    # load tasks
    try: 
        todo.load_json("todo.json") 
    except FileNotFoundError:
        pass

    app = TodoApp(todo)
    app.run()
    