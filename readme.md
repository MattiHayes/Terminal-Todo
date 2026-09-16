# Terminal Todo

This is a simple terminal based todo list that I used to get back into
programing and learn a bit about TUIs.

A todo list is a basic project but the main point of the project is the TUI.

## How it works ...

The TUI is shown below.
<img src=./assets/normal_view.svg>

When `n` is pressed then we are prompted to add a new task as shown below.
<img src=./assets/new_task.svg>

when `r` is pressed then we can remove tasks by clicking on them or selecting
with arrow keys and pressing enter. The task selected will be highlighed in red
showing that we are removing tasks. Adding new tasks and removing all complete
tasks is disabled in this mode.
<img src=./assets/remove_task.svg>

If we press `ctrl+r` then we will remove all complete tasks.
## Notes
The log may be a little overkill I know but I added it in to figure out
the messages and possibly to help debug if I needed to and so it is there for 
now. I will probably add something to hide it and show it.