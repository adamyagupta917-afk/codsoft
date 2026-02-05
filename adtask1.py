# CODSOFT - Task 1
# To Do List Application

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        t = input("Enter task: ")
        tasks.append(t)
        print("Task added successfully!")

    elif choice == '2':
        show_tasks()

    elif choice == '3':
        show_tasks()
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted!")
        else:
            print("Invalid number")

    elif choice == '4':
        print("Thank You!")
        break

    else:
        print("Invalid choice")