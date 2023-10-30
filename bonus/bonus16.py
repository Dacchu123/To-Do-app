import PySimpleGUI as Sg
from zip_files import zip_file

label1 = Sg.Text("Select files to compress: ")
input_text1 = Sg.InputText()
choose_button1 = Sg.FilesBrowse("Choose", key="Files")

label2 = Sg.Text("Select destination folder: ")
input_text2 = Sg.InputText()
choose_button2 = Sg.FolderBrowse("Choose", key="Folder")

compress_button = Sg.Button("Compress")
output = Sg.Text(key="compress", text_color="red")

window = Sg.Window("File Compress app", layout=[[label1, input_text1, choose_button1],
                                                [label2, input_text2, choose_button2],
                                                [compress_button, output]])
while True:
    events, values = window.read()
    print(events, values)
    filepaths = values['Files'].split(';')
    Folders = values['Folder']
    zip_file(filepaths, Folders)
    window['compress'].update(value="Compressed successfully")

window.close()
