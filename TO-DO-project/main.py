from todo import TodoManager

def main():
    manager = TodoManager()

    while True:
        print("\n--- TODO MENU ---")
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            title = input("Enter the task title: ")
            manager.add_task(title)
            print("Task added successfully!")

        elif choice == "2":
            print("\n--- YOUR SAVED TASKS ---")
            if not manager.tasks:
                print("No tasks found.")
            for t in manager.tasks:
                status = "Completed" if t.completed else "Not Completed"
                print(f"ID: {t.task_id} | Title: {t.title} | Status: {status}")

        elif choice == "3":
            try:
                task_id = int(input("Enter Task ID to update: "))
                print("What do you want to change?")
                print("a. Change Title")
                print("b. Mark as Completed")
                print("c. Mark as Not Completed")
                
                sub_choice = input("Select (a/b/c): ").lower()
                
                if sub_choice == 'a':
                    new_title = input("Enter new title: ")
                    manager.update_task(task_id, new_title=new_title)
                elif sub_choice == 'b':
                    manager.update_task(task_id, new_status=True)
                elif sub_choice == 'c':
                    manager.update_task(task_id, new_status=False)
                print("Update successful!")
            except ValueError:
                print("Please enter a valid number for the ID.")

        elif choice == "4":
            try:
                task_id = int(input("Enter Task ID to delete: "))
                manager.delete_task(task_id)
                print("Task removed!")
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            print("Closing application...")
            break

main()