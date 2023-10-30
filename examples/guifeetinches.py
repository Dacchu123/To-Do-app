import PySimpleGUI as Sg
from feet import feet_inches

label1 = Sg.Text("Enter feet")
input_text = Sg.InputText(tooltip="Enter here", key="todo")
label2 = Sg.Text("Enter inches")
input_text2 = Sg.InputText(tooltip="Enter here", key="todos")
button_text = Sg.Button("convert")
text = Sg.Text(key="ok")

windows = Sg.Window("Converter",
                    layout=[[label1, input_text], [label2, input_text2], [button_text, text]], font=("Helvetica", 15))
while True:
    events, values = windows.read()
    print(events, values)
    feet = float(values['todo'])
    inches = float(values['todos'])
    result = feet_inches(feet, inches)
    windows['ok'].update(value=f'{result}', text_color="green")
windows.close()
