#!/Python/python.exe
import subprocess
import sys

if len(sys.argv) > 1 and sys.argv[1] == '-p':
    pull_flag = True
    if len(sys.argv) > 2:
        commit_message = sys.argv[2]
    else:
        commit_message = None
else:
    pull_flag = False
    if len(sys.argv) > 1:
        commit_message = sys.argv[1]
    else:
        commit_message = None

if pull_flag:
    subprocess.run(["git", "pull"])
elif commit_message is None:
    commit_message = input("Enter Commit Message: ")

if commit_message is not None:
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "push"])
