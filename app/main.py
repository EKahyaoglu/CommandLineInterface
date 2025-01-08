# Command Line Interface Program
# Built with Python 3.11

import sys, os, subprocess

# ----- VALID COMMANDS -----
def is_builtin(command):
    return command in ["echo", "exit 0", "exit", "type"]

def find_executable(command):
    for path_dir in os.environ.get("PATH", "").split(":"):
        potential_path = os.path.join(path_dir, command)
        if os.path.isfile(potential_path) and os.access(potential_path, os.X_OK):
            return potential_path
    return None

def handle_type(command):
    type_cmd = command[len("type "):].strip()
    if is_builtin(type_cmd):
        print(f"{type_cmd} is a shell builtin")
    else:
        executable_path = find_executable(type_cmd)
        if executable_path:
            print(f"{type_cmd} is {executable_path}")
        else:
            print(f"{type_cmd}: not found")

def handle_echo(command):
    echo_parts = command.split()
    echo_output = " ".join(echo_parts[1:])
    print(echo_output)

def run_command(command):
    command_parts = command.split()
    program = command_parts[0]
    args = command_parts[1:]

    executable_path = find_executable(program)
    if executable_path:
        try:
            res = subprocess.run([executable_path] + args, check=True, capture_output=True, text=True)
            print(res.stdout.strip())
        except subprocess.CalledProcessError as e:
            print(e.stderr.strip())
    else:
        print(f"{command}: command not found")

def main():   
    # ----- GETTING USER INPUT -----
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input().strip()
        
        if command.startswith("type"):
            handle_type(command)
        elif command.startswith("echo"):
            handle_echo(command)
        elif command == "exit 0":
            break
        else:
            run_command(command)

if __name__ == "__main__":
    main()