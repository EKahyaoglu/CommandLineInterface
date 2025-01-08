# Command Line Interface Program
# Built with Python 3.11

import sys, os

def main():   
    # ----- VALID COMMANDS -----
    valid_commands = ["echo", "exit 0", "type"]
    
    # ----- GETTING USER INPUT -----
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input().strip()
        
        # Implementing type builtin command
        if command.startswith("type"):
            type_cmd = command[len("type "):].strip()
            if type_cmd in valid_commands:
                print(f"{type_cmd} is a shell builtin")
            else:
                found = False
                for path_dir in os.environ.get("PATH", "").split(":"):
                    potential_path = os.path.join(path_dir, type_cmd)
                    if os.path.isfile(potential_path) and os.access(potential_path, os.X_OK):
                        print(f"{type_cmd} is {potential_path}")
                        found = True
                        break
                if not found:
                    print(f"{type_cmd}: not found")
            continue

        # Implementing echo and exit 0 builtin commands
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