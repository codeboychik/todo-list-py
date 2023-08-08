from datetime import datetime, timedelta
import json
import configparser


def get_config():
    c = configparser.ConfigParser()
    c.read("important_names_and_constants.ini")
    return c


config = get_config()


def is_conversion_ok(item):
    try:
        int(item)
        return True
    except:
        return False


def get_first_not_zero_value(*delta_data):
    for index, data in enumerate(delta_data):
        if data != 0:
            return (index, data) if data < 2 else (index + 10, data)
    return -1, None


def get_pretty_time_string(delta_data):
    measure = {
        -1: "Less than minute ago",
        0: "day",
        1: "hour",
        2: "minute",
        10: "days",
        11: "hours",
        12: "minutes",
    }
    measure_value, data = get_first_not_zero_value(*delta_data)
    return (
        measure[-1] if measure_value == -1 else f"{data} {measure[measure_value]} ago"
    )


def substract_two_dates(date_given):
    diff = datetime.now() - datetime.fromisoformat(date_given)
    days = diff.days
    seconds = diff.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return get_pretty_time_string([days, hours, minutes])


def get_human_readable_time(date_given):
    return substract_two_dates(date_given)


def print_task_list(dictionary):
    print(dictionary["list_name"], "\n")
    if len(dictionary['tasks_list']) == 0:
        print("No items.")
    else:
        for index, task in enumerate(dictionary['tasks_list']):
            print(f"{index + 1}. {task['task_name']}")


def print_document(dictionary):
    print("\n\n=================================")
    print_task_list(dictionary)
    print("\n\n=================================")
    print(f"Last update: " + get_human_readable_time(dictionary["last_update"]))


def permission_error():
    raise PermissionError


def validate_json(file_name=config["PROPERTIES"]["DEFAULT_FILE"]):
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


def get_task_list(file_name=config["PROPERTIES"]["DEFAULT_FILE"]):
    validate_json(file_name)
    tasks = []
    dictionary = get_dictionary(file_name)
    for task in dictionary[config["PROPERTIES"]["TASKS"]]:
        task.append(task["task_name"])
    return tasks


def get_dictionary(file_name=config["PROPERTIES"]["DEFAULT_FILE"]):
    import json

    validate_json(file_name)
    with open(file_name, "r") as file:
        dictionary = json.load(file)
        if not validate_json(file_name=file_name):
            raise ValueError
        else:
            return dictionary


def write_to_json(file_name, tasks, update_timestamp=False):
    if update_timestamp:
        tasks["last_update"] = str(datetime.now().isoformat())
    with open(file_name, "w") as json_file:
        json.dump(tasks, json_file, indent=4)


def is_valid_command(command="", option=""):
    return (
        True
        if (option.startswith(command) and len(option.replace(command, "").strip()) > 0)
        else False
    )


# '+' = add, '-' = remove, '*' = print,'>' = change, 'x' = exit
def todoApp(file_name="tasks.json"):
    tasks = get_dictionary(file_name)
    task_list = tasks["tasks_list"]
    while True:
        [print(item, end=", ") for item in ["+", "-", '*', ">", "x"]]
        user_input = input("\nEnter option: ").strip()
        if is_valid_command("+", user_input):
            try:
                task_list.append({"task_name": user_input.replace("+", "").strip()})
                write_to_json(file_name, tasks, True)
            except OSError or NameError or PermissionError:
                print("Error occured while writing into file.")
        elif user_input.strip() == '*':
            print_document(tasks)
        elif is_valid_command("-", user_input):
            try:
                del tasks['tasks_list'][int(user_input.replace("-", "").strip()) - 1]
            except KeyError:
                print("An error while changing task occurred.")
        elif is_valid_command(">", user_input):
            task = int(user_input.replace(">", "").strip()) - 1
            try:
                print_task_list(tasks)
                try:
                    tasks['tasks_list'][task]['task_name'] = input("New task is: ")
                    tasks["last_update"] = str(datetime.now().isoformat())
                    write_to_json(file_name, tasks, True)
                    json.dumps(tasks, indent=4)
                except KeyError:
                    format("Item with name %s does not exist.", str(task))
            except TypeError:
                print("An error while changing task occurred.")
            print_task_list(tasks)
        elif is_valid_command("x", user_input):
            break
        else:
            print("Invalid operation.")


todoApp()
