# POSIX Compliant Shell / Command Line Interface Program

import sys, os, subprocess


# Check if command is a shell builtin
def is_builtin(command):
    return command in ["echo", "exit 0", "exit", "type", "pwd"]


# Find the executable in the PATH environment variable
def find_executable(command):
    for path_dir in os.environ.get("PATH", "").split(":"):
        potential_path = os.path.join(path_dir, command)
        if os.path.isfile(potential_path) and os.access(potential_path, os.X_OK):
            return potential_path
    return None


# ----- COMMAND DIRECTORY -----
# "type" Command
def handle_type(command):
    type_cmd = command[len("type ") :].strip()
    if is_builtin(type_cmd):
        print(f"{type_cmd} is a shell builtin")
    else:
        executable_path = find_executable(type_cmd)
        if executable_path:
            print(f"{type_cmd} is {executable_path}")
        else:
            print(f"{type_cmd}: not found")


# "echo" Command
def handle_echo(command):
    echo_parts = command.split()
    echo_output = " ".join(echo_parts[1:])
    print(echo_output)


# "pwd" Command
def handle_pwd(command):
    print(os.getcwd())


# Runs external commands with arguments
def run_command(command):
    command_parts = command.split()
    program = command_parts[0]
    args = command_parts[1:]

    executable_path = find_executable(program)
    if executable_path:
        try:
            # Extract program name from the executable path
            program_name = os.path.basename(executable_path)

            # Run the command
            res = subprocess.run(
                [executable_path] + args, check=True, capture_output=True, text=True
            )

            program_signature = res.stdout.strip()

            # Print the expected output
            print(f"Program was passed {len(command_parts)} args (including program name).")
            print(f"Arg #0 (program name): {program_name}")
            for i, arg in enumerate(args):
                print(f"Arg #{i+1}: {arg}")
            print(f"Program Signature: {program_signature}")
        except subprocess.CalledProcessError as e:
            print(e.stderr.strip())
    else:
        print(f"{command}: command not found")


# ----- GET USER INPUT & EXECUTE COMMANDS -----
def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input().strip()

        if is_builtin(command.split()[0]):
            if command.startswith("type"):
                handle_type(command)
            elif command.startswith("echo"):
                handle_echo(command)
            elif command.startswith("pwd"):
                handle_pwd(command)
            elif command == "exit 0":
                break
        else:
            run_command(command)


if __name__ == "__main__":
    main()
