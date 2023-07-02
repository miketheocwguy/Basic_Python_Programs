todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter TODO: ")
            todos.append(todo)
        case 'show':
            for item in todos :
                print(item)
        case 'edit':
            number = int(input("number of the todo you want to edit: "))
            new_todo = input("enter new todo: ")
            todos[number-1] = new_todo
        case 'exit':
            break

print("bye")
