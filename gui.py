import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a todo")
input_text = Sg.InputText(tooltip="Enter here", key="todo")
button_text = Sg.Button("Add")
list_box = Sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = Sg.Button("Edit")

complete_button = Sg.Button("Complete")
exit_button = Sg.Button("Exit")

windows = Sg.Window("My Todo App",
                    layout=[[label], [input_text, button_text],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=("Helvetica", 15))
while True:
    event, values = windows.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + '\n'
            todos.append(new_todos)
            functions.write_todos(todos)
            windows['todos'].update(values=todos)
        case "Edit":
            todo_edit = values['todos'][0]
            new_todos = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_edit)
            todos[index] = new_todos
            functions.write_todos(todos)
            windows['todos'].update(values=todos)
        case "Complete":
            todo_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_complete)
            functions.write_todos(todos)
            windows["todos"].update(values=todos)
            windows["todo"].update(value="")
        case "Exit":
            break
        case "todos":
            windows['todo'].update(value=values['todos'][0])
        case Sg.WIN_CLOSED:
            break

windows.close()
