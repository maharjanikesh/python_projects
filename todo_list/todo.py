tasks = []
def AddTask():
    task = input("Enter Tasks:\n")
    tasks.append(task)
    print(f"your {task} has been added in your todo list.")

def RemoveTask():
    try:
        task_number = int(input("Enter the number of the task to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def ListTask():
    if tasks:
        print("Tasks in your list.")
        for index, task in enumerate(tasks, start=1):
            print(f'#{index}. {task}')
    else:
        print("No tasks in your todo list.")

while True:
    print("Choose your Operation.")
    print("----------------------")
    print("1. Enter tasks in todo list.")
    print("2. Delete tasks in todo list.")
    print("3. List tasks in todo list.")
    print("4. Quit.")

    choice = input("Enter your choice: ")

    if choice == '1':
        AddTask()
    elif choice == '2':
        ListTask()
        RemoveTask()
    elif choice == '3':
        ListTask()
    elif choice == '4':
        print("GoodBye!")
        break
    else:
        print("Invalid number. Enter a number between 1 to 4.")