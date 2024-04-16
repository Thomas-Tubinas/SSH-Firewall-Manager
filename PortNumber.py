import pandas as pd
import matplotlib.pyplot as plt

badPorts = []

def Add():
    portAdd = True
    print("What port number do you want do ban?\nWhen your done enter Next")
    while portAdd:
        PortNum = input("Enter Port Number: ")
        if PortNum.lower() == "next":
            portAdd = False
        elif PortNum.isdigit():
            badPorts.append(PortNum)
        else:
            print("Invalid Option. Please Enter Port Number")
    print(badPorts)

def Remove():
    portRemove = True
    print("Enter the port number you want to remove\nWhen your done enter Next")
    print(badPorts)
    while portRemove:
        PortNum = input("Enter Port Number: ")
        if PortNum.lower() == "next":
            portRemove = False
        elif PortNum.isdigit():
            badPorts.remove(PortNum)
        else:
            print("Invalid Option. Please Enter Port Number")
    print(badPorts)


loop = True
while loop:
    print("What do you want to do\n1) Add Port Number To Be Banned\n2) Unban Port Number")
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
