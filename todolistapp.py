# this is a to do list app 
tasks = []

def show_menu():
    """Display the main menu options"""
    print("\n" )
    print("        TO-DO LIST APPLICATION")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Mark task as complete")
    print("6. Exit")
    print("="*40)

def view_tasks():
    """Display all tasks with their status"""
    if not tasks:
        print("\nYour to-do list is empty!")
        return
    
    print("\nYOUR TASKS:")
    print("-" * 40)
    for index, task in enumerate(tasks, start=1):
        status = "Complete" if task['completed'] else "Pending"
        print(f"{index}. {status} - {task['title']}")
    print("-" * 40)

def add_task():
    """Add a new task to the list"""
    task_title = input("\nEnter task description: ").strip()
    
    if not task_title:
        print("Task cannot be empty!")
        return
    
    task = {
        'title': task_title,
        'completed': False
    }
    tasks.append(task)
    print(f"Task '{task_title}' added successfully!")

def update_task():
    """Update an existing task"""
    if not tasks:
        print("\nNo tasks to update!")
        return
    
    view_tasks()
    try:
        task_num = int(input("\nEnter task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_title = input("Enter new task description: ").strip()
            if new_title:
                tasks[task_num-1]['title'] = new_title
                print("Task updated successfully!")
            else:
                print("Task description cannot be empty!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    """Delete a task from the list"""
    if not tasks:
        print("\nNo tasks to delete!")
        return
    
    view_tasks()
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num-1)
            print(f"Task '{deleted_task['title']}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def mark_complete():
    """Mark a task as complete"""
    if not tasks:
        print("\nNo tasks to mark as complete!")
        return
    
    view_tasks()
    try:
        task_num = int(input("\nEnter task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num-1]['completed'] = True
            print(f"Task '{tasks[task_num-1]['title']}' marked as complete!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main program loop"""
    print("Welcome to your To-Do List Manager!")
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            mark_complete()
        elif choice == '6':
            print("\nThank you for using the To-Do List Application!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
