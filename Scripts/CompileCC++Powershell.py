#!/usr/bin/env python3
import os
import subprocess

# Check if the terminal is PowerShell
if os.environ.get('TERM') == 'xterm-256color':
    # Set the execution policy to allow local scripts
    subprocess.run(['powershell', '-Command', 'Set-ExecutionPolicy', 'RemoteSigned', '-Scope', 'CurrentUser', '-Force'])

    # Call the compile script
    subprocess.run(['Python', 'Compile.py'])

    # Set the execution policy back to its default value
    subprocess.run(['powershell', '-Command', 'Set-ExecutionPolicy', 'Restricted', '-Scope', 'CurrentUser', '-Force'])
else:
    # Call the compile script
    subprocess.run(['Python', 'Compile.py'])