from modules import *


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
                del tasks['tasks_list'][int(user_input.replace("-", "")) - 1]
            except KeyError:
                print("An error while deleting task occurred.")
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
