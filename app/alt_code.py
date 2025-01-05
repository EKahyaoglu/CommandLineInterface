import sys

def main():   
    
    valid_commands = []
    
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()
    match command:
        case "hello":
            print("Hello, World!")
        case "exit 0":
            sys.exit()
        case _:
            print(f"{command}: command not found")
    main() # Call recursively

    """ ALTERNATIVE REPL IMPLEMENTATION
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        if command not in valid_commands:
            print(f"{command}: command not found")
            continue
    """

if __name__ == "__main__":
    main()