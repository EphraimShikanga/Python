import subprocess
import sys

# try to get the file names from the command line arguments
try:
    file_names = sys.argv[1:]
    # if there are no file names, raise an IndexError
    if not file_names:
        raise IndexError
# if there is no command line argument, ask for the file names
except IndexError:
    file_names = input("Enter the file names separated by spaces: ").split()

# loop through the file names
for file_name in file_names:
    # execute the chmod u+x command with the file name
    subprocess.run(["chmod", "u+x", file_name])