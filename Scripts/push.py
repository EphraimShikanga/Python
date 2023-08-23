#!\C:\Python\python.exe

import subprocess
import sys

# try to get the commit message from the first command line argument
try:
    commit_message = sys.argv[1]
# if there is no command line argument, ask for the commit message
except IndexError:
    commit_message = input("Enter your commit message: ")

# execute the git add command
subprocess.run(["git", "add", "."])

# execute the git commit command with the commit message
subprocess.run(["git", "commit", "-m", commit_message])

# execute the git push command
subprocess.run(["git", "push"])