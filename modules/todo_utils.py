import re
from datetime import datetime
import json


def get_dictionary(file_name='tasks.json'):
    validate_json(file_name)
    with open(file_name, "r") as file:
        dictionary = json.load(file)
        if not validate_json(file_name=file_name):
            raise ValueError
        else:
            return dictionary


def get_first_not_zero_value(*delta_data):
    for index, data in enumerate(delta_data):
        if data != 0:
            return (index, data) if data < 2 else (index + 10, data)
    return -1, None


def is_valid_command(command="", option=""):
    return (
        True
        if (option.startswith(command) and len(option.replace(command, "")) > 0)
        else False
    )


def write_to_json(file_name, tasks, update_timestamp=False):
    if update_timestamp:
        tasks["last_update"] = str(datetime.now().isoformat())
    with open(file_name, "w") as json_file:
        json.dump(tasks, json_file, indent=4)


def validate_json(file_name='tasks.json'):
    if not file_name.endswith(".json"):
        raise ValueError
    with open(file_name, "r") as file:
        dictionary = json.load(file)
    return (
        True
        if "list_name" in dictionary
           and "last_update" in dictionary
           and "tasks" in dictionary
        else ValueError
    )


def get_task_list(file_name='tasks.json'):
    validate_json(file_name)
    tasks = []
    dictionary = get_dictionary(file_name)
    for task in dictionary['tasks_list']:
        task.append(task["task_name"])
    return tasks


def check_password(password):
    criteria = list()
    for pattern in ['[0-9]', '[a-z]', '[A-Z]', '\W']:
        find = re.findall(pattern, password)
        criteria.append(True) if \
            (True if len(find) > 0 else False) \
            and len(sorted(find, reverse=True)[0]) > 0 \
            else criteria.append(False)
    criteria = criteria.count(True)
    return "Weak Password" if criteria <= 2 else ("Normal Password" if criteria == 3 else "Strong Password")


def add_task(value):
    try:
        tasks = get_dictionary()
        tasks_list = tasks['tasks_list'] if tasks['tasks_list'] is not None else []
        tasks_list.append(value)
        tasks['tasks_list'] = tasks_list
        write_to_json(file_name='tasks.json', tasks=tasks, update_timestamp=True)
    except OSError or NameError or PermissionError:
        print("Error occured while writing into file.")
