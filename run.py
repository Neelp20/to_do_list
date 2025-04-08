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


def add_task():
    """
    Allow users to add new tasks directly to Google Sheet.
    """
    while True:
        date_input = input("Enter the date for the task (DD-MM-YEAR): ")
        try:
            date_task = datetime.datetime.strptime(
                date_input, "%d-%m-%Y").date()
        except ValueError:
            print("Invalid date format! Please use DD-MM-YEAR.")
            continue
        break

    valid_tasks = []
    while not valid_tasks:
        task_input = input(
            "Enter your task(s) to be added(separated by comma): ")
        tasks = [
            task.strip() for task in task_input.split(",") if task.strip()]

        for task in tasks:
            if task.isdigit():
                print(f"Error: '{task}' is a number so cannot be added!")
            else:
                valid_tasks.append(task)

    worksheet = SHEET.worksheet('mytasks')
    for task in valid_tasks:
        worksheet.append_row([str(date_task), task])

    print(f"Task(s) {tasks} have been added for {date_task}.")


def show_task():
    """
    Display tasks directly by loading them from the Google Sheet.
    """
    # Fetch data from google sheet
    worksheet = SHEET.worksheet('mytasks')  # Access mytasks worksheet.
    data = worksheet.get_all_records()  # Fetch the records

    if not data:  # check if the sheet is empty
        print("list is empty!")
    else:
        print("task is organized by date: ")
        for row in data:
            print(f"- {row['Date']}: {row['Task']}")


def remove_task():
    """
    Removes a specific task from the Google Sheet if the date and task matches.
    """
    while True:
        date_input = input(
            "Enter the date for the task (DD-MM-YYYY) to be removed: "
        )
    
        try:
            date_task = datetime.datetime.strptime(
                date_input, "%d-%m-%Y").date()
        except ValueError:  # for invalid formats
            print("Invalid date format! Please use DD-MM-YEAR.")
            continue
        break
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
            break

    # Show appropriate message
    if found:
        print(f"'{task_to_remove}' has been removed from {date_task}.")
    else:
        print("Task not found in the sheet")


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
            add_task()
        elif choice == '2':
            show_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            is_open = False
        else:
            print("This is not a valid choice")

    print("Thank you, Enjoy your day!")


main()
