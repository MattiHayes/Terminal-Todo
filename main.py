from todoList import TodoList

OPTIONS = [
    "Add task",
    "Mark task complete",
    "Mark task incomplete",
    "Remove task",
    "Remove all complete tasks",
    "quit"
]

def get_instruction() -> int:
    print("Select option:")
    while True:
        for i, opt in enumerate(OPTIONS):
            print(f"{i+1}: {opt}")
        try:
            option = int(input("> "))
            if 1 <= option <= len(OPTIONS):
                return option
            print("Please select a Valid option")    
        except ValueError:
            print("Please input a whole number")


def get_task_num(num_tasks: int) -> int:
    print("Select Task")
    while True:
        try:
            task_num = int(input("> "))
            if 0 < task_num <=  num_tasks:
                return task_num
            print("invalid task")
        except ValueError:
            print("Please input the number of the task")

def main():
    todo = TodoList()
    while True:
        print("To DO:")
        print("---------------------")
        print(todo)
        print("---------------------")
        option = get_instruction()

        if len(todo) == 0 and (1 < option < len(OPTIONS)):
            print("Todo list is empty")
            continue

        match option:
            case 1:
                print("Input task")
                task_name = input("> ")
                todo.add_task(task_name)
            case 2:
                task_num = get_task_num(len(todo))
                todo.mark_complete(task_num)
            case 3:
                task_num = get_task_num(len(todo))
                todo.mark_incomplete(task_num)
            case 4:
                task_num = get_task_num(len(todo))
                todo.remove(task_num)
            case 5:
                todo.remove_complete()
            case 6:
                print("Bye :)")
                break
            case _:
                raise(ValueError("Input option out of range"))
        
if __name__ == "__main__":
    main()