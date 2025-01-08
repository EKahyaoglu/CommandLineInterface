# Command Line Interface Program
# Built with Python 3.11

import sys, os, subprocess

def main():   
    # ----- VALID COMMANDS -----
    valid_commands = ["echo", "exit 0", "exit", "type"]
    
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
            # Split the command and arguments
            command_parts = command.split()
            program = command_parts[0]
            args = command_parts[1:]

            found = False
            for path_dir in os.environ.get("PATH", "").split(":"):
                potential_path = os.path.join(path_dir, program)
                if os.path.isfile(potential_path) and os.access(potential_path, os.X_OK):
                    try:
                        res = subprocess.run([potential_path] + args, check=True, capture_output=True, text=True)
                        print(res.stdout.strip())
                        found = True
                    except subprocess.CalledProcessError as e:
                        print(e.stderr.strip())
                    break
            if not found:
                print(f"{command}: command not found")
        
if __name__ == "__main__":
    main()