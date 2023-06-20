import subprocess
import sys
import os

# Define the command to empty the trash
command = 'osascript -e "tell application \\"Finder\\" to empty trash"'

# Execute the command
subprocess.run(command, shell=True)

os.system("start.py")
os.system("clear")

if sys.platform.startswith('darwin'):
    subprocess.call('osascript -e \'tell application "Terminal" to close (every window whose name contains "Shell")\'', shell=True)