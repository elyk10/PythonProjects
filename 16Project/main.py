def addTask(tasks, newTask = ""):
    tasks.append(newTask)
    return tasks

def removeTask(tasks, oldTask = ""):
    tasks.remove(oldTask)
    return tasks

def viewTasks(tasks):
    for i in tasks:
        print(i)

def saveTasks(tasks):
    file = open("tasks.txt", "w")
    for i in tasks:
        file.write(i + "/n")

def handleFunctionExceptions(func, var):
    try:
        func(var)

    except:
        print("Function failed: " + func)
    