def get_todos(filepath='files/todo output.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='files/todo output.txt'):
    with open(filepath, 'w') as files_local:
        files_local.writelines(todos_arg)


text = '''
hi my name is documentation:
what is your name :
ok bye
'''
# It is a documentation of the file 
print(text)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = (user_action[4:] + '\n')

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)
    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()

            new_todo = input("Enter your new todo : ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid!")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f'Todo {todo_to_remove} was removed from the list'
            print(message)
        except IndexError:
            print("Your index value is out of range!!")
        except ValueError:
            print("You enter wrong value!!")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid!!")
print("Bye!!")
