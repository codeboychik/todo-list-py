from modules import *
import PySimpleGUI as psg

label = psg.Text('Type in a to-do')
input_box = psg.InputText(tooltip="Enter Todo", size=20, key='task_name')
add_button = psg.Button('Add')

list_box = psg.Listbox(values=get_task_list(), key='Tasks', enable_events=True, size=[45, 10])
edit_button = psg.Button('Edit')
remove_button = psg.Button('Remove')
update_time = psg.Text(f"Last update: {get_human_readable_time(get_dictionary()['last_update'])}", key='update_time')
window = psg.Window('My Tasks App',
                    layout=[[label], [input_box, add_button], [list_box, [edit_button, remove_button]], [update_time]],
                    font=('Roboto', 20))

while True:
    event, value = window.read()

    if psg.WINDOW_CLOSED or event != 'WIN_CLOSED':
        break

    print(event, value)
    try:
        window['update_time'].update(f"Last update: {get_human_readable_time(get_dictionary()['last_update'])}")
    except KeyError:
        pass

    if event == 'Add':
        print(value)
        add_task(value["task_name"])
        window['Tasks'].update(values=get_task_list())

    if event == 'Edit':
        try:
            edit_task(value['Tasks'][0], value['task_name'])
            window['Tasks'].update(values=get_task_list())
        except IndexError:
            pass

    if event == 'Remove':
        confirm_layout = [
            [psg.Text("Are you sure?")],
            [psg.Button("Yes"), psg.Button("No")]
        ]
        confirm_window = psg.Window("Confirmation", confirm_layout)
        while True:
            confirm_event, confirm_values = confirm_window.read()
            if confirm_event == psg.WINDOW_CLOSED or confirm_event == "No":
                break
            elif confirm_event == "Yes":
                print(f'removing {value}')
                remove_task(value['Tasks'][0])
                window['Tasks'].update(values=get_task_list())
                break

        confirm_window.close()


window.close()
