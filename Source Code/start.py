import os
import pygame

while True:
    print("""
███████╗██████╗░███████╗███████╗
██╔════╝██╔══██╗██╔════╝██╔════╝
█████╗░░██████╔╝█████╗░░█████╗░░
██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░
██║░░░░░██║░░██║███████╗███████╗
╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝

░█████╗░██╗░░░░░███████╗░█████╗░███╗░░██╗███████╗██████╗░
██╔══██╗██║░░░░░██╔════╝██╔══██╗████╗░██║██╔════╝██╔══██╗
██║░░╚═╝██║░░░░░█████╗░░███████║██╔██╗██║█████╗░░██████╔╝
██║░░██╗██║░░░░░██╔══╝░░██╔══██║██║╚████║██╔══╝░░██╔══██╗
╚█████╔╝███████╗███████╗██║░░██║██║░╚███║███████╗██║░░██║
░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
""")
    print()
    print("""🄲 🄻 🄴 🄰 🄽 🄴 🅁

[1] . . . . . . . . . . [Empty Trash]

[2] . . . . . . . . . . [Quit Large Programs/Websites]
""")

    # Get user input
    choice = input("Enter your choice (1 or 2): ")

    # Perform actions based on the chosen option
    if choice == "1":
        # Execute empty.py
        os.system("python3 Source\ Code/empty.py")
    elif choice == "2":
        # Execute end_task.py
        os.system("python3 Source\ Code/end_tasks.py")
    else:
        print("Invalid choice. Please try again.")