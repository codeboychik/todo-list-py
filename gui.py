from modules import *
import PySimpleGUI as psg

label = psg.Text('Type in a to-do')
input_box = psg.InputText(tooltip="Enter Todo", size=20, key='task_name')
add_button = psg.Button('Add')

window = psg.Window('My Tasks App',
                    layout=[[label], [input_box, add_button]],
                    font=('Roboto', 20))

while True:
    event, value = window.read()
    if event == 'Add':
        add_task(value)

    if psg.WINDOW_CLOSED:
        break

window.close()
