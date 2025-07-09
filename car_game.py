print("Car Game in python")
command = ""
is_started = False
is_stopped = False
while 1:
    command = input("Enter >> ")
    if command.lower() == 'start':
        if is_started:
            print("Car is already started !")
        else:
            is_started = True
            print("Car stared.... Ready to go")
    elif command.lower() == 'stop':
        if is_stopped:
            print("Car is already stopped !")
        else:
            is_stopped = True
            print("Car stopped.")
    elif command.lower() == 'help':
        print("""
    start -> to start the car
    stop -> to stop the car
    quit -> to end the game
    """)
    elif command.lower() == 'quit':
        print("Game ended.")
        break
    else:
        print("I don't know")