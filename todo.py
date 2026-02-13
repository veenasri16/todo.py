# File name: todo.py

TASK_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add a new task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print(" No tasks available.\n")
    else:
        print("\n Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print()

# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}\n")
        else:
            print(" Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main program loop
def main():
    tasks = load_tasks()

    while True:
        print("TO-DO LIST MENU")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("EXIT")
            break
        else:
            print("⚠ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
