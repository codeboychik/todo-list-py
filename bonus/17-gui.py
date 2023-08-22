import os.path

import PySimpleGUI as psg
import zipfile as zf

label1 = psg.Text("Select files to compress: ")
input1 = psg.Input()
choose_button1 = psg.FilesBrowse('Choose')

label2 = psg.Text("Select destination folder: ")
input2 = psg.Input()
choose_button2 = psg.FolderBrowse('Choose')

input3 = psg.Input('compressed')

label3 = psg.Text("Archive name: ")
compress_button = psg.Button("Compress")

window = psg.Window('File Compressor',
                    layout=[[label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [label3, input3, compress_button],
                            [psg.Text(key='Successful')]])


def get_files(input_val):
    return input_val.get().split(';')


def is_valid_filepaths(input_val):
    code = 0
    paths = input_val.get().split(';')
    for path in paths:
        try:
            code = code if not os.path.isfile(path) else code +1
        except FileNotFoundError:
            pass
    return True if code == len(paths) else False


def is_valid_folder(input_val):
    return FileNotFoundError if not os.path.isfile(input_val.get().strip()) else True


def resolve_filename(input_val):
    return input_val.get() \
        if input_val.get().strip().endswith('.zip') \
        else f'{input_val.get().strip().split("/")[-1]}.zip'


while True:
    event, values = window.read()

    if event == psg.WIN_CLOSED:
        break

    if event == 'Compress' \
            and is_valid_folder(input2) \
            and is_valid_filepaths(input1):
        with zf.ZipFile(f'{input2.get().strip()}/{resolve_filename(input3)}', 'w') as myzip:
            [myzip.write(item, arcname=item.split('/')[-1]) for item in get_files(input1)]
            window['Successful'].update('Compression completed')

window.close()
