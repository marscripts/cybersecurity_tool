import os
import subprocess
import threading
import datetime
import json

# ANSI Color Codes for Formatting
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

LOG_FILE = "cybersecurity_tool_log.txt"
TOOLS_FILE = "tools.json"

# Load tools from JSON file
def load_tools():
    try:
        with open(TOOLS_FILE, "r") as file:
            return json.load(file)
    except Exception as e:
        error(f"Failed to load {TOOLS_FILE}: {e}")
        exit(1)

TOOLS = load_tools()  # Load tools dynamically

# Utility Functions
def log(message, color=GREEN):
    """ Logs a message to console and file. """
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    formatted_message = f"{timestamp} {message}"
    print(f"{color}[INFO]{RESET} {message}")

    # Append to log file
    with open(LOG_FILE, "a") as log_file:
        log_file.write(formatted_message + "\n")

def error(message):
    """ Prints an error message in red and logs it. """
    print(f"{RED}[ERROR]{RESET} {message}")
    log(f"[ERROR] {message}", RED)

def validate_file_path(file_path):
    """ Validates whether a file exists. """
    if not os.path.exists(file_path):
        error(f"The file '{file_path}' does not exist.")
        return False
    return True

def validate_target(target):
    """ Ensures a valid target is entered. """
    if not target:
        error("Target cannot be empty.")
        return False
    return True

def check_dependencies():
    """ Checks if required tools are installed. """
    missing_tools = []
    for tool in TOOLS.keys():
        if subprocess.run(f"which {tool.split()[0]}", shell=True, stdout=subprocess.DEVNULL).returncode != 0:
            missing_tools.append(tool)
    
    if missing_tools:
        error(f"Missing tools detected: {', '.join(missing_tools)}. Install them before proceeding.")
        exit(1)

def execute_command(command):
    """ Executes a command in a separate thread and logs output. """
    def run():
        log(f"Executing: {command}")
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        if stdout:
            log(f"\n{stdout}")
        if stderr:
            error(stderr)

    thread = threading.Thread(target=run)
    thread.start()

def display_tool_menu():
    """ Displays the available tools menu. """
    print(f"\n{CYAN}Available tools:{RESET}")
    for i, tool in enumerate(TOOLS.keys(), start=1):
        print(f"{YELLOW}{i}. {tool} - {TOOLS[tool]['description']}{RESET}")
    print(f"{YELLOW}{len(TOOLS) + 1}. Exit{RESET}")

def select_tool():
    """ Allows the user to select a tool from the menu. """
    while True:
        display_tool_menu()
        choice = input("Enter your choice: ").strip()
        try:
            choice = int(choice)
            if 1 <= choice <= len(TOOLS):
                return list(TOOLS.keys())[choice - 1]
            elif choice == len(TOOLS) + 1:
                return "exit"
            else:
                raise ValueError
        except ValueError:
            error("Invalid choice. Please try again.")

def run_tool(tool):
    """ Executes the selected tool with user-specified options. """
    tool_config = TOOLS[tool]
    command_template = tool_config["command"]

    # Special handling for hashcat
    if tool == "hashcat":
        hash_file = input("Enter path to hash file: ").strip()
        if not validate_file_path(hash_file):
            return
        wordlist = input("Enter path to wordlist: ").strip()
        if not validate_file_path(wordlist):
            return
        options = input("Enter options or press Enter for default (-O): ").strip() or "-O"
        command = command_template.format(hash_file=hash_file, wordlist=wordlist, options=options)

    # Special handling for Hydra
    elif tool == "hydra":
        target = input("Enter target (IP/domain): ").strip()
        if not validate_target(target):
            return
        service = input("Enter service (e.g., ssh, ftp, http): ").strip()
        username = input("Enter username: ").strip()
        wordlist = input("Enter path to password list: ").strip()
        if not validate_file_path(wordlist):
            return
        command = command_template.format(target=target, service=service, username=username, wordlist=wordlist)

    # Handle tools with profiles
    elif "profiles" in tool_config:
        target = input("Enter target (IP or domain): ").strip()
        if not validate_target(target):
            return
        print("\nChoose a profile:")
        for key, value in tool_config["profiles"].items():
            print(f"{YELLOW}{key}. {value}{RESET}")
        choice = input("Enter your choice: ").strip()
        options = tool_config["profiles"].get(choice, tool_config["profiles"]["1"])
        command = command_template.format(target=target, options=options)

    # Tools that just run (like Metasploit)
    else:
        command = command_template

    log(f"Running {tool} with command: {command}")
    execute_command(command)

if __name__ == "__main__":
    check_dependencies()
    while True:
        tool = select_tool()
        if tool == "exit":
            print(f"{CYAN}Exiting the script. Goodbye!{RESET}")
            break
        try:
            run_tool(tool)
        except Exception as e:
            error(f"An error occurred: {e}")
