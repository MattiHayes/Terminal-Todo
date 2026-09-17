# Terminal To Do

A todo list is a basic project but the main point of the project is the TUI.

Well that is it on the surface, but when you actually think about it there is much
more to a To Do application: tasks need to be stored somewhere so they persist
when the app is opened and closed.

Then you may want to add sub tasks, you want to edit the tasks, remove them, maybe even undo removing one ... Will the TUI have states depending on what you are doing? Or will there be separate screens for everything? Where will I store the tasks, how do I manage multiple lists? 

So yes a simple project in general, but there is still a lot to do to get a 'properly functioning' application. So yes the project is simple, but that allows me to focus on so much more for this side project. 

Maybe I'm just over thinking this.  

*TL;DR* Yes a To Do list is a simple programming project but that is the point because there is so much more to do.

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