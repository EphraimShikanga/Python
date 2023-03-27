import os
import subprocess
import time

# Determine the appropriate command to clear the terminal based on the operating system
if os.name == "nt":
    # Windows-based system, use cls or clear depending on the terminal being used
    term = os.environ.get("TERM")
    if term is not None and "powershell" in term.lower():
        clear_cmd = "clear"
    else:
        clear_cmd = "cls"
else:
    # Unix-based system, use clear command
    clear_cmd = "clear"

# Get the input file name from the user
input_file = input("Enter the name of the input file (without extension): ")

# Get the output file name from the user
output_file = input("Enter the name of the output file (without extension): ")

# Check if the input file exists and get the file extension
input_file_ext = None
for ext in (".cpp", ".c++", ".cc", ".c"):
    if os.path.exists(f"{input_file}{ext}"):
        input_file_ext = ext
        break

# Check if a valid file extension was found
if input_file_ext is None:
    print(f"Error: could not find file with supported extension (.cpp, .c++, .cc, .c)")
    exit(1)

# Determine the compiler command based on the file extension
if input_file_ext in (".cpp", ".c++", ".cc"):
    compiler_cmd = f"g++ -o {output_file} {input_file}{input_file_ext}"
else:
    compiler_cmd = f"gcc -o {output_file} {input_file}{input_file_ext}"

# Compile the code using the appropriate compiler
result = subprocess.run(compiler_cmd, shell=True, capture_output=True, text=True)
if result.returncode == 0:
    # Compilation successful, display message and wait 3 seconds before clearing the terminal
    print("Compilation successful... clearing terminal in 3 seconds.")
    time.sleep(3)
    os.system(clear_cmd)
else:
    # Compilation unsuccessful, display message and wait 2 seconds before printing the errors
    print("Compilation unsuccessful... printing compilation errors in 2 seconds.")
    time.sleep(2)
    print(result.stdout)
    print(result.stderr)
    exit(1)
