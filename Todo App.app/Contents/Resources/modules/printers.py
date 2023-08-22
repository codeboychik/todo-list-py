from .pretty_time import *


def print_document(dictionary):
    print("\n\n=================================")
    print_task_list(dictionary)
    print("\n\n=================================")
    print(f"Last update: " + get_human_readable_time(dictionary["last_update"]))


def print_task_list(dictionary):
    print(dictionary["list_name"], "\n")
    if len(dictionary['tasks_list']) == 0:
        print("No items.")
    else:
        for index, task in enumerate(dictionary['tasks_list']):
            print(f"{index + 1}. {task['task_name']}")
