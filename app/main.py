#
#
#

import sys

def main():   
    
    valid_commands = ["echo", "exit 0"]
    
    # ----- EXPECT USER INPUT -----
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input().strip()

        if command.startswith("echo"):
            echo_parts = command.split()
            echo_output = " ".join(echo_parts[1:])
            print(echo_output)    
        elif command == "exit 0":
            break
        elif command not in valid_commands:
            print(f"{command}: command not found")
            continue
        
if __name__ == "__main__":
    main()