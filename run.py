# To Do List
import datetime  # geeksforgeeks.org

my_list = []  # list of tasks will be stored in this variable.
datewise_tasks = {}
"""
datewaise_tasks is a dictionary to keep tasks for each date separately.
"""


def add_task(datewise_tasks):
    """
    Allow users to add new task in the list.
    """
    date_input = input("Enter the date for the task (DD-MM-YEAR): ")
    try:
        # validate the date format
        task_date = datetime.datetime.strptime(date_input, "%d-%m-%Y").date()
    except ValueError:
        print("Invalid date format! Please use DD-MM-YEAR.")
        return
    
    task_input = input("Enter your task(s) to be added(separated by comma): ")
    # print("Your tasks are added in the list")
    tasks = [task.strip() for task in task_input.split(",") if task.strip()]

    for task in tasks:
        if task.isdigit():  # isdigit()method by w3schools.
            print(f"Error: '{task}' is a number so cannot be added!")
        else:
            my_list.append(task)
    
    if my_list:
        if task_date not in datewise_tasks:
            datewise_tasks[task_date] = []
        datewise_tasks[task_date].extend(tasks)
        print(f"Task(s) {tasks} have been added for {task_date}.")
    else:
        print("No valid tasks were added.") 
      
    # if my_list:
    #     print("Your task(s) have been added.")
        # return my_list
    # else:
    #     print("No valid tasks were added.")
        # return None
    

def show_task(datewise_tasks):
    """
    Allow users to see the list of tasks.
    """
    if not datewise_tasks:  # check if the dictionary is empty
        print("list is empty!")
    else:
        print("task is organized by date: ")
        for task_date, tasks in datewise_tasks.items():
            print(f"- {task_date}:")
            for task in tasks:
                print(f" * {task}")
    # if not my_list:
    #     print("Your list is empty")
    # else:
    #     print("Your tasks are: ")
    #     for task in my_list:
    #         print(f"- {task}")
    

def remove_task(datewise_tasks):
    """
    Removes a specific task from the specified date.
    """
    date_input = input("Enter the date for the task (D-M-Y) to be removed: ")
    try:
        # Validate and parse the date
        task_date = datetime.datetime.strptime(date_input, "%d-%m-%Y").date()
    except ValueError:  # for invalid formats
        print("Invalid date format! Please use DD-MM-YEAR.")
        return

    if task_date not in datewise_tasks:
        print(f"No tasks found for {task_date}.")
        return

    task_to_remove = input("Enter the task to be removed: ").strip()
    if task_to_remove in datewise_tasks[task_date]:
        datewise_tasks[task_date].remove(task_to_remove)
        print(f"'{task_to_remove}' has been removed from {task_date}.")
        # Remove date key if it becomes empty
        if not datewise_tasks[task_date]:
            del datewise_tasks[task_date]
    else:
        print(f"'{task_to_remove}' is not in the task list for {task_date}.")
    # """
    # Allow the users to remove a particular task from the list
    # """
    # task_to_remove = input("Enter the task to be removed: ")

    # if task_to_remove in my_list:
    #     my_list.remove(task_to_remove)
    #     print(f"'{task_to_remove}' has been removed.")
    # else:
    #     print(f"'{task_to_remove}' is not in the list.")


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
            tasks = add_task(datewise_tasks)
            if tasks:
                my_list.extend(tasks)
        elif choice == '2':
            show_task(datewise_tasks)
        elif choice == '3':
            remove_task(datewise_tasks)
        elif choice == '4':
            is_open = False
        else:
            print("This is not a valid choice")

    print("Thank you, Enjoy your day!")


main()
