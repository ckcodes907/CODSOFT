# Define an empty task list
tasks = []

# Function to add a task to the list
def add_task_to_list():
    new_task = input("Enter the task: ")
    tasks.append(new_task)
    print("Task added successfully!")

# Function to view all tasks
def display_tasks():
    if not tasks:
        print("Your task list is empty.")
    else:
        print("Task List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Function to update a task
def update_task_in_list():
    display_tasks()
    task_index = int(input("Enter the index of the task to update: ")) - 1
    if 0 <= task_index < len(tasks):
        updated_task = input("Enter the updated task: ")
        tasks[task_index] = updated_task
        print("Task updated successfully!")
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task_from_list():
    display_tasks()
    task_index = int(input("Enter the index of the task to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f"{deleted_task} has been deleted.")
    else:
        print("Invalid task index.")

while True:
    print("\nTask List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    user_choice = input("Select an option (1/2/3/4/5): ")

    if user_choice == "1":
        add_task_to_list()
    elif user_choice == "2":
        display_tasks()
    elif user_choice == "3":
        update_task_in_list()
    elif user_choice == "4":
        delete_task_from_list()
    elif user_choice == "5":
        break
    else:
        print("Invalid choice. Please choose a valid option.")
