class Task:
    def __init__(self, title, description, assigned_to):
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.status = 'Pending'

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Assigned To: {self.assigned_to}, Status: {self.status}"


class TaskManagementSystem:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, assigned_to):
        task = Task(title, description, assigned_to)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

    def update_task_status(self, task_index, new_status):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].status = new_status
            print(f"Task '{self.tasks[task_index].title}' status updated to '{new_status}'.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task.title}' deleted successfully.")
        else:
            print("Invalid task index.")

    def run(self):
        while True:
            print("\nTask Assignment and Tracking System")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task Status")
            print("4. Delete Task")
            print("5. Exit")

            choice = input("Choose an option: ")
            if choice == '1':
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                assigned_to = input("Assign task to: ")
                self.add_task(title, description, assigned_to)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                task_index = int(input("Enter task index to update (1-based): ")) - 1
                new_status = input("Enter new status (Pending/In Progress/Completed): ")
                self.update_task_status(task_index, new_status)
            elif choice == '4':
                task_index = int(input("Enter task index to delete (1-based): ")) - 1
                self.delete_task(task_index)
            elif choice == '5':
                print("Exiting the system.")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    tms = TaskManagementSystem()
    tms.run()