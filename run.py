# To Do List
import gspread
from google.oauth2.service_account import Credentials
import datetime  # geeksforgeeks.org

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('to_do_list')

"""
To check if the our APIs are working:-
mytasks = SHEET.worksheet('mytasks')

data = mytasks.get_all_values()
print(data)
"""

my_list = []  # list of tasks will be stored in this variable.
datewise_tasks = {}
"""
datewise_tasks is a dictionary to keep tasks for each date separately.
"""


def add_task(datewise_tasks):
    """
    Allow users to add new task in the list.
    """
    date_input = input("Enter the date for the task (DD-MM-YEAR): ")
    try:  # the code should work with no errors, if data is valid.
        # validate the date format
        date_task = datetime.datetime.strptime(date_input, "%d-%m-%Y").date()
    except ValueError:  # print error tothe terminal ifcode doesntwork.
        print("Invalid date format, Please use DD-MM-YEAR.")
        return
    
    task_input = input("Enter your task(s) to be added(separated by comma): ")
    # print("Your tasks are added in the list")
    tasks = [task.strip() for task in task_input.split(",") if task.strip()]

    for task in tasks:
        if task.isdigit():  # isdigit()method by w3schools.
            print(f"Error: '{task}' is a number so cannot be added!")
        else:
            # my_list = SHEET.worksheet("mytasks")
            my_list.append(task)
    
    if tasks:
        if date_task not in datewise_tasks:
            datewise_tasks[date_task] = []
        datewise_tasks[date_task].extend(tasks)
        
        worksheet = SHEET.worksheet('mytasks')
        for task in tasks:
            worksheet.append_row([str(date_task), task])

        print(f"Task(s) {tasks} have been added for {date_task}.")
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
    # Fetch data from google sheet
    worksheet = SHEET.worksheet('mytasks')  # Access mytasks worksheet.
    data = worksheet.get_all_records()  # Fetch the records

    if not data:  # check if the sheet is empty
        print("list is empty!")
    else:
        print("task is organized by date: ")
        for row in data:
            date_task = row["Date"]
            task = row["Task"]
            print(f"- {date_task}: {task}")
        # for date_task, tasks in datewise_tasks.items():
        #     print(f"- {date_task}:")
        #     for task in tasks:
        #         print(f" * {task}")
    # if not my_list:
    #     print("Your list is empty")
    # else:
    #     print("Your tasks are: ")
    #     for task in my_list:


def remove_task(datewise_tasks):
    """
    Removes a specific task from the specified date.
    """
    date_input = input("Enter the date for the task (D-M-Y) to be removed: ")
    try:
        # Validate and parse the date
        date_task = datetime.datetime.strptime(date_input, "%d-%m-%Y").date()
    except ValueError:  # for invalid formats
        print("Invalid date format! Please use DD-MM-YEAR.")
        return
    # Get the task to remove
    task_to_remove = input("Enter the task to be removed: ").strip()

    worksheet = SHEET.worksheet('mytasks')
    data = worksheet.get_all_records()

    # Remove task from the google sheet if it exists
    found = False
    for index, row in enumerate(data, start=2):  # Start at 2 to skip header
        if row["Date"] == str(date_task) and row["Task"] == task_to_remove:
            worksheet.delete_rows(index)  # Delete the row from google sheet
            found = True
            print(f"Deleted row at index {index}: {row}")
            break

    # update datewise_tasks dictionary
    if date_task in datewise_tasks:
        if task_to_remove in datewise_tasks[date_task]:
            datewise_tasks[date_task].remove(task_to_remove)
            if not datewise_tasks[date_task]:
                del datewise_tasks[date_task]

    # Show appropriate message
    if found:
        print(f"'{task_to_remove}' has been removed from {date_task}.")
    else:
        print("Task not found in the sheet")

    # if task_to_remove in datewise_tasks[date_task]:
    #     datewise_tasks[date_task].remove(task_to_remove)
    #     print(f"'{task_to_remove}' has been removed from {date_task}.")
        # if not datewise_tasks[date_task]:
        #     del datewise_tasks[date_task]
    # else:
    #     print(f"'{task_to_remove}' is not in the task list for {date_task}.")
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
