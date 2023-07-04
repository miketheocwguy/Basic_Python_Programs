

while True:
    user_action = input("Type add, show, edit, completed or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter TODO: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)


        case 'show':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()


            for index,item in enumerate(todos):
                item = item.strip('\n')
                screen = f"{index + 1}-{item.capitalize()}"
                print(screen)

        case 'edit':
            number = int(input("number of the todo you want to edit: "))
            number = number- 1

            with open('todos.txt', 'r') as file:
                 todos = file.readlines()
            print(todos)

            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'completed':
            number = int(input("Number of the completed item: "))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(number - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was completed and removed from the list"
            print(message)
        case 'exit':
            break

print("Thank you ")
