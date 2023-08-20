from modules import *
import PySimpleGUI as psg


theme = psg.theme('DarkPurple')

label = psg.Text('Type in a to-do')
input_box = psg.InputText(tooltip="Enter Todo", size=20, key='task_name')
add_button = psg.Button('Add')

list_box = psg.Listbox(values=get_task_list(), key='Tasks', enable_events=True, size=[45, 10])
edit = psg.Button('Edit')
complete = psg.Button('Complete')
last_update = psg.Text(f"Last update: {get_human_readable_time(get_dictionary()['last_update'])}", key='last_update')
buttons = [[edit], [complete]]
right_column_layout = [[list_box]]
left_column = psg.Column(right_column_layout)
right_column = psg.Column(buttons)
window = psg.Window('My Tasks App',
                    layout=[[label], [input_box, add_button], [[left_column, right_column]], [last_update]],
                    font=('Roboto', 20))

while True:
    event, value = window.read(timeout=1000)

    if psg.WINDOW_CLOSED or event == 'WIN_CLOSED':
        break

    # print(event, value)
    try:
        window['last_update'].update(f"Last update: {get_human_readable_time(get_dictionary()['last_update'])}")
    except KeyError:
        pass

    if event == 'Add':
        if len(input_box.get().strip()) > 1:
            print(value)
            add_task(value["task_name"])
            window['Tasks'].update(values=get_task_list())
        else:
            psg.popup("Enter to-do title first.")

    if event == 'Edit':
        try:
            edit_task(value['Tasks'][0], value['task_name'])
            window['Tasks'].update(values=get_task_list())
        except IndexError:
            psg.popup("Select to-do first.")

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
