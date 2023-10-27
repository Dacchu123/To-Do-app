import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a todo")
input_text = Sg.InputText(tooltip="Enter here")
button_text = Sg.Button("Add")

windows = Sg.Window("My Todo App", [[label], [input_text, button_text]])
windows.read()
windows.close()
