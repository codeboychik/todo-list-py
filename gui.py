from modules import *
import PySimpleGUI as psg

label = psg.Text('Type in a to-do')
input_box = psg.InputText(tooltip="Enter Todo", size=20, key='task_name')
add_button = psg.Button('Add')

list_box = psg.Listbox(values=get_task_list(), key='Tasks', enable_events=True, size=[45, 10])
edit_button = psg.Button('Edit')
update_time = psg.Text(f"Last update: {get_human_readable_time(get_dictionary()['last_update'])}")
window = psg.Window('My Tasks App',
                    layout=[[label], [input_box, add_button], [list_box, edit_button], [update_time]],
                    font=('Roboto', 20))

while True:
    event, value = window.read()
    print(event, value)
    window['update_time'].update(values=f"Last update: {get_human_readable_time(get_dictionary()['last_update'])}")
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

    if psg.WINDOW_CLOSED:
        break

window.close()
