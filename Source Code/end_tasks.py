import psutil
import os
import sys
import subprocess

# Get running processes and their memory usage
running_processes = psutil.process_iter(attrs=['pid', 'memory_info', 'name'])

# Iterate through each process
for process in running_processes:
    try:
        pid = process.info['pid']
        memory_info = process.info['memory_info']
        process_name = process.info['name']
        rss = memory_info.rss

        # Convert memory usage to GB
        rss_gb = rss / (1000 ** 3)  # Convert from bytes to gigabytes

        if rss_gb > 1:
            print(f"Terminating process: {process_name} (PID: {pid})")
            process.terminate()

    except psutil.NoSuchProcess:
        # Handle the case when the process no longer exists
        pass

    except psutil.AccessDenied:
        # Handle the case when access to process information is denied
        pass

    except Exception as e:
        # Print any other exceptions that occur during the termination process
        print(f"Exception occurred: {e}")

os.system("start.py")
os.system("clear")

if sys.platform.startswith('darwin'):
    subprocess.call('osascript -e \'tell application "Terminal" to close (every window whose name contains "Shell")\'', shell=True)