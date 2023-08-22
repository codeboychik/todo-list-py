import PySimpleGUI as psg
from extract import extract

arcpath = psg.Input()
choose_arc = psg.FileBrowse('Choose', key='arcpath')

destpath = psg.Input()
choose_dest = psg.FolderBrowse('Choose', key='destpath')

unzip = psg.Button('unzip', key='unzip')
complete = psg.Text(key='complete', text_color='green')
window = psg.Window(title='Unzip your archive', layout=[[arcpath, choose_arc], [destpath, choose_dest], [unzip]])

while True:
    event, value = window.read(timeout=1000)

    if psg.WINDOW_CLOSED or event == psg.WIN_CLOSED:
        break

    if event == 'unzip':
        try:
            extract(arcpath.get(), destpath.get())
            window['complete'].update('Extraction completed.')
        except FileNotFoundError:
            psg.popup('File not found.')
        except NotADirectoryError:
            psg.popup('Not a folder.')


window.close()
