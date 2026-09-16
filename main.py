import json
import atexit
import signal
from todoList import TodoList
from app import TodoApp


def exit_handler(todo: TodoList):
    if len(todo) > 0:
        with open("todo.json", "w") as f:
            json.dump(todo.jsonify(), f, indent=4)

def ctrl_c_handler(signum, frame):
    print("\nCTRL-c was pressed. Exiting")
    exit(1)

if __name__ == "__main__":
    todo = TodoList()
    # load tasks
    try: 
        todo.load_json("todo.json") 
    except FileNotFoundError:
        pass
    # register exit handler
    atexit.register(exit_handler, todo)
    # register handler for CTRL-c
    signal.signal(signal.SIGINT, ctrl_c_handler)

    app = TodoApp(todo)
    app.run()