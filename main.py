from task_manager import TaskManager
from api_module import save_to_cloud

def main():
    manager = TaskManager()
    
    print("="*45)
    print(" STUDENT TASK MANAGEMENT SYSTEM: CLOUD SYNC ")
    print("="*45)
    
    while True:
        print("\n--- MENU ---")
        print("1. View Tasks")
        print("2. Add Task (Save to Cloud)")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("\nSelect an option: ")

        if choice == '1':
            print("\n--- YOUR CURRENT TASKS ---")
            tasks = manager.get_all_tasks()
            if not tasks:
                print("[The list is empty]")
            else:
                for num, t in enumerate(tasks, 1):
                    # Updated format: 1. Mango
                    print(f"{num}. {t['title']}")
        
        elif choice == '2':
            title = input("Enter manual task: ")
            if title.strip():
                # 1. Add Locally
                new_task = manager.add_task(title)
                
                # 2. Save to Cloud (API Integration)
                print("Sending task to cloud...")
                if save_to_cloud(new_task):
                    print(f"Success: '{title}' added locally and synced to Cloud.")
                else:
                    print(f"Note: '{title}' added locally, but Cloud sync failed.")
            else:
                print("Error: Task cannot be empty.")

        elif choice == '3':
            try:
                target_id = int(input("Enter number to delete: "))
                if manager.delete_task(target_id):
                    print(f"Task {target_id} removed. Numbers rearranged.")
                else:
                    print(f"Error: Number {target_id} not found.")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == '4':
            print("System closing. Goodbye!")
            break
        
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
    