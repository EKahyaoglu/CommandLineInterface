# Command Line Interface Program
# Built with Python 3.11

import sys

def main():   
    
    valid_commands = ["echo", "exit 0", "type"]
    
    # ----- GETTING USER INPUT -----
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input().strip()
        
        if command.startswith("type"):
            type_cmd = command[len("type "):].strip()
            if type_cmd.startswith("echo"):
                print("echo is a shell builtin")
            elif type_cmd.startswith("exit"):
                print("exit is a shell builtin")
            elif type_cmd.startswith("type"):
                print("type is a shell builtin")
            else:
                print(f"type {type_cmd}: not found")
            continue
        elif command.startswith("echo"):
            echo_parts = command.split()
            echo_output = " ".join(echo_parts[1:])
            print(echo_output)    
        elif command == "exit 0":
            break
        else:
            print(f"{command}: command not found")
            continue
        
if __name__ == "__main__":
    main()