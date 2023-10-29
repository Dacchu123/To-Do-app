import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a todo")
input_text = Sg.InputText(tooltip="Enter here", key="todo")
button_text = Sg.Button("Add")

windows = Sg.Window("My Todo App",
                    layout=[[label], [input_text, button_text]],
                    font=("Helvetica", 15))
while True:
    event, values = windows.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + '\n'
            todos.append(new_todos)
            functions.write_todos(todos)
        case Sg.WIN_CLOSED:
            break

windows.close()
