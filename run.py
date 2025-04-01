# To Do List
my_list = []  # data will be stored in this variable.


def add_task():
    """
    Allow users to add new task in the list.
    """
    task_input = input("Enter your task(s) to be added(separated by comma): ")
    print("Your tasks are added in the list")

    tasks = [task.strip() for task in task_input.split(",")]
    if tasks:
        return tasks
    else:
        print("Invalid task.")
        return None
    

def show_task():
    """
    Allow users to see the list of tasks.
    """
    if not my_list:
        print("Your list is empty")
    else:
        print("Your tasks are: ")
        for task in my_list:
            print(f"- {task}")
    

def remove_task():
    """
    Allow the users to remove a particular task from the list
    """


def main():
    """
    The menu/user choices are written here.
    """
    is_open = True

    while is_open:
        print("My To Do List")
        print("1.Add Task(s)")
        print("2.Show Task(s)")
        print("3.Remove Task(s)")
        print("4.Close")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            tasks = add_task()
            if tasks:
                my_list.extend(tasks)
        elif choice == '2':
            show_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            is_open = False
        else:
            print("This is not a valid choice")


main()