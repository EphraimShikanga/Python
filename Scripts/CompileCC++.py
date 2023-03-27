#!/usr/bin/env python3
import os
import subprocess
import platform
import time

# Get the input file name from the user
input_file = input("Enter the name of the input file: ")

# Get the output file name from the user
output_file = input("Enter the name of the output file: ")

# Determine the appropriate compiler and file extension based on the input file
if input_file.endswith(".cpp") or input_file.endswith(".c++") or input_file.endswith(".cc"):
    compiler = "g++"
    extension = ".exe" if platform.system() == "Windows" else ""
elif input_file.endswith(".c"):
    compiler = "gcc"
    extension = ".exe" if platform.system() == "Windows" else ""
else:
    print("Error: No such File Found!")
    exit(1)

# Compile the code using the appropriate compiler
compile_cmd = f"{compiler} -o {output_file}{extension} {input_file}"
result = subprocess.run(compile_cmd, shell=True, capture_output=True, text=True)

# Determine the appropriate command to clear the terminal based on the operating system and terminal being used
terminal = os.environ.get("TERM_PROGRAM")
if platform.system() == "Windows":
    clear_cmd = "cls" if terminal == "PowerShell" or "WT" in terminal else "clear"
else:
    clear_cmd = "clear"

if result.returncode == 0:
    # Compilation successful, delay for 3 seconds, clear the terminal and print success message
    time.sleep(3)
    print("Compilation successful... clearing terminal")
    os.system(clear_cmd)
else:
    # Compilation failed, clear the terminal, print error message and compilation errors after a 2-second delay
    os.system(clear_cmd)
    print("Compilation unsuccessful... printing compilation errors")
    print(result.stdout)
    print(result.stderr)
    time.sleep(2)

    exit(1)
