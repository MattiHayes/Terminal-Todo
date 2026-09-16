from textual.app import App, ComposeResult
from textual.screen import  ModalScreen
from textual.widgets import Input, ListView, ListItem, Header, Log, Label

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

class CustomLog(Log):

    def on_mount(self):
        self.border_title = "Log"
        return super().on_mount()

    def write_line(self, msg: str):
        super().write_line("> " + msg)


class NewTask(Input):

    def on_mount(self) -> None:
        self.placeholder = ">"
        self.border_title = "New Task"        


class NewTaskScreen(ModalScreen):

    BINDINGS = [
        ("ctrl+z", "cancel", "Cancel New Task")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
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
        self._state = "normal"
        super().__init__(driver_class, css_path, watch_css, ansi_color)

    def compose(self) -> ComposeResult:
        yield Header()
        yield TaskList()
        yield CustomLog()

    def on_mount(self) -> None:
        self.refresh_tasks()
        self._log = self.query_one(CustomLog)
        
        
    def action_new_task(self):
        if self._state == "remove":
            self._log.write_line("Can't add new task in remove mode.")
            return
        
        def add(task_name: str) -> None:
            self._todo_list.add_task(task_name)
            self.refresh_tasks()
            self._log.write_line(f"Added new task: \"{task_name}\"")
        self.push_screen(NewTaskScreen(), add)

    def action_remove_task(self):
        # change the app state
        if self._state == "normal":
            self._state = "remove"
            self.query_one(TaskList).add_class("remove")
            self.query_one(TaskList).border_subtitle = "r-Exit Remove Task"
            self._log.write_line("App state changed to \"remove\"")
        else:
            self._state = "normal"
            self.query_one(TaskList).remove_class("remove")
            self.query_one(TaskList).border_subtitle = "n-New Task r-Remove Task ^r-Remove Complete Tasks"
            self._log.write_line("App state changed to \"normal\"")

    def action_remove_complete(self):
        if self._state == "remove":
            self._log.write_line("Can't remove all complete tasks in remove mode.")
            return

        self._todo_list.remove_complete()
        self.refresh_tasks()
        self._log.write_line(f"Removed all complete tasks")

    def refresh_tasks(self):
        task_list = self.query_one("TaskList")
        task_list.display_tasks(self._todo_list)

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        # check app state
        if self._state == "normal":
            # task status needs changing
            self.toggle_task_state(event.index)
        else:
            # we need to remove tasks
            self.remove_task(event.index)
            
    def remove_task(self, task_idx):
        self._log.write_line(f"Removed task {self._todo_list[task_idx].name}")
        self._todo_list.remove(task_idx)
        self.refresh_tasks()

    def toggle_task_state(self, task_idx: int) -> None:
        task = self._todo_list[task_idx]
        if task.complete:
            task.is_incomplete()
            self._log.write_line(f"Task \"{task.name}\" marked incomplete.")
        else:
            task.is_complete()
            self._log.write_line(f"Task \"{task.name}\" marked complete.")
        self.refresh_tasks()


if __name__ == "__main__":

    todo = TodoList()
    # load tasks
    try: 
        todo.load_json("todo.json") 
    except FileNotFoundError:
        pass

    app = TodoApp(todo)
    app.run()
    