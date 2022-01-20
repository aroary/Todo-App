from todoData import getTodoData, setTodoData, os

def editTask(id, name, description, priority):
    if "-" not in id and "." not in id and id.isdigit():
        id = int(id)
    else:
        return print("Invalid id.")

    if "-" not in priority and "." not in priority and priority.isdigit():
        priority = int(priority)
        
        if priority < 0 or priority > 4:
            return print("Priority must be between 0 and 4.")
    else:
        return print("Invalid priority.")

    index, todoData = getTodoData(os.environ["workspace"])
    
    for i, o in enumerate(todoData.tasks):
        if o.id == id:
            todoData.tasks[i].task = name
            todoData.tasks[i].description = description
            todoData.tasks[i].priority = priority
            break
    
    for i, o in enumerate(todoData.completed):
        if o.id == id:
            todoData.tasks[i].task = name
            todoData.tasks[i].description = description
            todoData.tasks[i].priority = priority
            break

    setTodoData(todoData, index)