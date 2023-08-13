from modules import *
import PySimpleGUI as psg

label = psg.Text('Type in a to-do')
input_box = psg.InputText(tooltip="Enter Todo")
add_button = psg.Button('Add')

window = psg.Window('My Tasks App', layout=[[label, [input_box, add_button]]])
window.read()
window.close()