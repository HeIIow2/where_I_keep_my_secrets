import FilesManager
# custom script to manage the files

print("help for a list of all commands")

current_file = None


def show_commands():
    print("help: prints a list, of all commands\n"
          "open <name> <password>: opens a file and creates it if there isn't a file named that way\n"
          "write: you can append text to an opened file\n"
          "exit: closes the programm")


def exec_command(raw_command: str):
    global current_file

    arguments = raw_command.split(" ")
    command = arguments[0]
    arguments = arguments[1:]

    if command == "help":
        show_commands()
        return

    if command == "open":
        if len(arguments) != 2:
            return "password or name is missing"

        name, password = arguments
        current_file = FilesManager.File(name, password)
        return

    if command == "write":
        if current_file is None:
            return "open a file first"

        current_file.write_to_file()
        return

    if command == "exit":
        exit()

    return f"couldn't find command {command}"


while True:
    command = input("> ")
    success = exec_command(command)
    if type(success) == str:
        print(success)
