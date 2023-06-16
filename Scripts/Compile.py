#!/Python/python.exe
import os
import subprocess
import sys

# Check if the input file name is provided as a command line argument
if len(sys.argv) > 2 and sys.argv[1] == '-c':
    clear_terminal = False
    input_file = sys.argv[2]
else:
    clear_terminal = True
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        # Get the input file name from the user
        input_file = input("Enter filename: ")

# Determine the appropriate compiler and file extension based on the input file
if input_file.endswith(".cpp") or input_file.endswith(".c++") or input_file.endswith(".cc"):
    compiler = "g++"
    # Generate the output file name with .exe extension
    output_file = os.path.splitext(input_file)[0] + ".exe"
elif input_file.endswith(".c"):
    compiler = "gcc"
    # Generate the output file name with .exe extension
    output_file = os.path.splitext(input_file)[0] + ".exe"
elif input_file.endswith(".java"):
    compiler = "javac"
    # Generate the output file name with .class extension
    output_file = os.path.splitext(input_file)[0] + ".class"
else:
    print("Error: C, C++, and Java Only!")
    exit(1)

# Compile the code using the appropriate compiler
if compiler == "g++" or compiler == "gcc":
    compile_cmd = f"{compiler} -o {output_file} {input_file}"
elif compiler == "javac":
    compile_cmd = f"{compiler} {input_file}"
else:
    print("Error: No Compiler Found!")
    exit(1)

result = subprocess.run(compile_cmd, shell=True,
                        capture_output=True, text=True)

if result.returncode == 0:
    # Compilation successful, delay for 3 seconds, clear the terminal, print success message, and run the output file
    # print("Compilation successful... clearing terminal")
    # time.sleep(1)
    if clear_terminal:
        os.system('cls')

    if compiler == "javac":
        # Run the compiled Java program using the 'java' command
        run_cmd = f"java {os.path.splitext(input_file)[0]}"
        os.system(run_cmd)
    else:
        # Run the output file for C and C++ programs
        run_cmd = output_file
        os.system(run_cmd)
else:
    # Compilation failed, clear the terminal, print error message and compilation errors after a 2-second delay
    if clear_terminal:
        os.system('cls')

    # print("Compilation unsuccessful... printing compilation errors")
    # time.sleep(1)
    print(result.stdout)
    print(result.stderr)

    exit(1)
