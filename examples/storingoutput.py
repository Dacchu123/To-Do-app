
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'

            file = open('files/todo output.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('files/todo output.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('files/todo output.txt', 'r')
            todos = file.readlines()
            file.close()

            # new_todos = [(item.strip('\n'))for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit : "))
            number = number - 1
            new_todo = input("Enter your todo : ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete : "))
            todos.pop(number - 1)
        case 'exit':
            exit1 = input("press enter to exit>>")
            break
print("Bye!!")
