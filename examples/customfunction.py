def get_todos():
    with open('files/todo output.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = (user_action[4:] + '\n')

        todos = get_todos()

        todos.append(todo)

        # write todos in the file or create a text file
        with open('files/todo output.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith("show"):
        # check your output or storing value or item or etc
        todos = get_todos()

        # new_todos = [(item.strip('\n'))for item in todos]
        # show outputs  with number with good and proper order we use this code
        for index, item in enumerate(todos):
            # remove lines or backslash "\n"
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            # this method to edit your items
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()

            new_todo = input("Enter your new todo : ")
            todos[number] = new_todo + '\n'

            with open('files/todo output.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid!")
            continue
    elif user_action.startswith("complete"):
        try:
            # this method to delete or complete code
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            # print removed element using this line code
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todo output.txt', 'w') as file:
                file.writelines(todos)

            message = f'Todo {todo_to_remove} was removed from the list'
            print(message)
        except IndexError:
            print("Your index value is out of range!!")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid!!")
print("Bye!!")
