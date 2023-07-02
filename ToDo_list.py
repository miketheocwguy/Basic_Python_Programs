todos = []

while True:
    user_action = input("Type add, show, edit, completed or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter TODO: ")
            todos.append(todo)
        case 'show':
            for index , item in enumerate(todos) :
                print(index+1,": ",item)
        case 'edit':
            number = int(input("number of the todo you want to edit: "))
            new_todo = input("enter new todo: ")
            todos[number-1] = new_todo
        case 'completed':
            number = int(input("Number of the completed item: "))
            todos.pop(number-1)

        case 'exit':
            break

print("Thank you ")
