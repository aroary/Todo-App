from todoData import getTodoData, setTodoData, Todo, os

def addTask(task, description, priority):
    if not task:
        return print("Task name can not be empty")
    
    if not priority:
        priority = 0
    elif "-" not in priority and "." not in priority and priority.isdigit():
        priority = int(priority)
        
        if priority < 0 or priority > 4:
            return print("Priority must be between 0 and 4.")
    else:
        return print("Invalid priority.")

    todo = Todo(task, description, priority)

    index, todoData = getTodoData(os.environ["workspace"])
    todoData.tasks.append(todo)
    todoData.id += 1
    setTodoData(todoData, index)
    
    print(f"\n[CREATED] <{todo.createDate}> ({todo.priority}) {todo.task.capitalize()} {todo.description}")