tasks = []

while True:
    command = input("Enter command (add/view/complete/exit): ")

    if command == "add":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")

    elif command == "view":
        for i in range(len(tasks)):
            print(i+1, tasks[i])

    elif command == "complete":
        num = int(input("Enter task number: "))
        tasks[num-1] = "[x] " + tasks[num-1]
        print("Task completed")

    elif command == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid command")
