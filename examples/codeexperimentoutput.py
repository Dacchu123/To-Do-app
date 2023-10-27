
while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        # check if user action is "add"
        case 'add':
            todo = input("Enter a todo: ") + '\n'

            file = open('files/todo output.txt', 'r')
            todos = file.readlines() # it's a type of list
            file.close()

            todos.append(todo)

            # write todos in the file or create a text file
            file = open('files/todo output.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            # check your output or storing value or item or etc
            file = open('files/todo output.txt', 'r')
            todos = file.readlines() #list define
            file.close()

            # new_todos = [(item.strip('\n'))for item in todos]
            # show outputs  with number with good and proper order we use this code
            for index, item in enumerate(todos):
                # remove lines or backslash "\n"
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            # this method to edit your items
            number = int(input("Number of the todo to edit : "))
            number = number - 1
            new_todo = input("Enter your new todo : ")
            todos[number] = new_todo


        case 'complete':
            # this method to delete or complete code
            number = int(input("Number of the todo to complete : "))
            todos.pop(number - 1)
        case 'exit':
            # exit the output we use this code
            exit1 = input("press enter to exit>>")
            break
print("Bye!!")
