from addTask import addTask
from removeTask import removeTask
from editTask import editTask
from completeTask import completeTask
from uncompleteTask import uncompleteTask
from listTasks import listTasks

commands = [
    {
        "name": "add",
        "description": "Add a task",
        "alias": ["a", "new"],
        "help": "(string) Task: [name of the task]\n(string) Description: [description of the task]\n(0 <= integer <= 4) Priority: [priority of the task]",
        "function": lambda: addTask(input("Task: "), input("Description: "), input("Priority: ")),
        "source": addTask
    },
    {
        "name": "remove",
        "description": "Remove a task",
        "alias": ["r"],
        "help": "(integer) Id: [id of the task]",
        "function": lambda: removeTask(input("ID: ")),
        "source": removeTask
    },
    {
        "name": "edit",
        "description": "Edit a task",
        "alias": ["e"],
        "help": "(integer) Id: [id of the task]\n(string) Task: [name of the task]\n(string) Description: [description of the task]\n(0 <= integer <= 4) Priority: [priority of the task]",
        "function": lambda: editTask(input("ID: "), input("Task: "), input("Description: "), input("Priority: ")),
        "source": editTask
    },
    {
        "name": "complete",
        "description": "Complete a task",
        "alias": ["c", "resolve"],
        "help": "(integer) Id: [id of the task]",
        "function": lambda: completeTask(input("ID: ")),
        "source": completeTask
    },
    {
        "name": "uncomplete",
        "description": "Uncomplete a task",
        "alias": ["u", "incomplete"],
        "help": "(integer) Id: [id of the task]",
        "function": lambda: uncompleteTask(input("ID: ")),
        "source": uncompleteTask
    },
    {
        "name": "list",
        "description": "List the active tasks",
        "alias": ["l", "ls"],
        "help": "(string) sort by: [(p) priority | (d) date | (n) name]\n(string) direction: [(a) ascending | (d) descending]",
        "function": lambda: listTasks(input("Sort by: "), input("Direction: ")),
        "source": listTasks
    }
]