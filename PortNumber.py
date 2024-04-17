import pandas as pd
import matplotlib.pyplot as plt

Ports = []
IPs = []
Usernames = []

def Add():
    toAdd = int(input("What do you want to add to the list?\n1: Port\n2: IP\n3: Username"))
    if toAdd == 1:
        portAdd = int(input("Enter Port number"))
        Ports.append(portAdd)
    elif toAdd == 2:
        Remove()
    elif toAdd == 3:
        loop = False
        print("Exiting the program...")
    else:
        print("Invalid option. Please enter 1, 2, or 3.")

loop = True
while loop:
    print("What do you want to do\n1: Add Port Number To Be Banned\n2: Unban Port Number")
    num = input()
    if num == "1":
        Add()
    elif num == "2":
        Remove()
    elif num == "3":
        loop = False
        print("Exiting the program...")
    else:
        print("Invalid option. Please enter 1, 2, or 3.")
