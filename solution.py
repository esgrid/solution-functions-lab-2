tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def completed_tasks(tasks):
    completed = []
    for task in tasks:
        if task["completed"]:
            completed.append(task["description"])

    print(f"Completed tasks: {completed}.")

def incomplete_tasks(tasks):
    incomplete = []
    for task in tasks:
        if not task["completed"]:
            incomplete.append(task["description"])
    print(f"Incomplete tasks: {incomplete}.")

def print_descriptions(tasks):
    for task in tasks:
        print("Description:" + task["description"])
        print("Completed: " + str(task["completed"]))
        print("Time Taken: " + str(task["time_taken"]))

def time_taken(tasks, time):
    tasks_time = []
    for task in tasks:
        if task["time_taken"] >= time:
            tasks_time.append(task["description"])
    print (f"The tasks that took {time} or more are: {tasks_time}")

def given_description(tasks, description):
    result = None
    for task in tasks:
        if description.lower() == task["description"].lower():
            result = task
    if result == None:
        result = "That description doesn't correspond to a task."
    print (result)
    
def update_description(tasks, description):
    u_task = None
    for task in tasks:
        if (description.lower() == task["description"].lower()):
            task["completed"] = True
            u_task = task
    print(f"{u_task['description']} is completed")

def add_task(tasks, new_task):
    tasks.append(new_task)
    print(tasks)

def menu():
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")

# Using my functions

# completed_tasks(tasks)

# incomplete_tasks(tasks)

# print_descriptions(tasks)

# time_taken(tasks, 15)

# given_description(tasks, "feed cat")

# update_description(tasks, "clean windows")

# new_task = {"description": "Read", "completed": True, "time_taken": 60}

# add_task(tasks, new_task)

menu()
option = input("Please enter the desired option: ").lower()

while option != "q":
    if option == "1":
        print_descriptions(tasks)
    elif option == "2":
        incomplete_tasks(tasks)
    elif option == "3":
        completed_tasks(tasks)
    elif option == "4":
        update_description(tasks, input("Enter task to update to completed: "))
    elif option == "5":
        time_taken(tasks, int(input("Enter Time: ")))
    elif option == "6":
        given_description(tasks, input("Enter description: "))
    elif option == "7":
        task = {"description": input("Enter name of new task: "), 
                "completed": True if (input("Enter status of completion (True/False)): ").lower() == "true") else False, 
                "time_taken": int(input("Enter time taken: "))}
        add_task(tasks, task)
    elif option == "m":
        menu()
    option = input("Please enter the desired option: ").lower()