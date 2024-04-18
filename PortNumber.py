import pandas as pd
import matplotlib.pyplot as plt

Ports = []
IPs = []
Usernames = []
AccessList = [Ports, IPs, Usernames]

def Print():
    print(f"Ports: {AccessList[0]}")
    print(f"IPs: {AccessList[1]}")
    print(f"Users: {AccessList[2]}")

def Add():
    toAdd = int(input("What do you want to add to the list?\n1: Port\n2: IP\n3: Username\n4: Exit"))
    if toAdd == 1:
        portAdd = int(input("Enter Port number"))
        Ports.append(portAdd)
        Add()
    elif toAdd == 2:
        ipAdd = input("Enter IP Address")
        IPs.append(ipAdd)
        Add()
    elif toAdd == 3:
        usersAdd = input("Enter the user's name")
        Usernames.append(usersAdd)
        Add()
    elif toAdd == 4:
        Print()
    else:
        print("Invalid option. Please enter 1, 2, 3, or 4")

def Remove():
    toRemove = int(input("What do you want to remove from the list?\n1: Port\n2: IP\n3: Username"))
    if toRemove == 1:
        portAdd = int(input("Enter Port number"))
        Ports.append(portAdd)
    elif toRemove == 2:
        ipAdd = input("Enter IP Address")
        IPs.append(ipAdd)
    elif toRemove == 3:
        usersAdd = input("Enter the user's name")
        Usernames.append(usersAdd)
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
