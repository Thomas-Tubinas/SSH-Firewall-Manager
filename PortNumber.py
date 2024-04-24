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
    toRemove = int(input("What do you want to remove from the list?\n1: Port\n2: IP\n3: Username\n4: Exit"))
    if toRemove == 1:
        portAdd = int(input("Enter Port number"))
        Ports.append(portAdd)
        Remove()
    elif toRemove == 2:
        ipAdd = input("Enter IP Address")
        IPs.append(ipAdd)
        Remove()
    elif toRemove == 3:
        usersAdd = input("Enter the user's name")
        Usernames.append(usersAdd)
        Remove()
    elif toRemove == 4:
        Print()
    else:
        print("Invalid option. Please enter 1, 2, or 3.")

def Save():
    with open("acl.txt", "w") as file:
        file.write("Ports:\n")
        file.write('\n'.join(map(str, Ports)))
        file.write("\n\nIPs:\n")
        file.write('\n'.join(IPs))
        file.write("\n\nUsernames:\n")
        file.write('\n'.join(Usernames))

def Load():
    global Ports, IPs, Usernames
    with open("acl.txt", "r") as file:
        lines = file.readlines()
        mode = None
        for line in file:
            line = line.strip()
            if line == "Ports:":
                mode = "Ports"
            elif line == "IPs:":
                mode = "IPs"
            elif line == "Usernames:":
                mode = "Usernames"
            elif mode == "Ports" and line:
                Ports.append(int(line))
            elif mode == "IPs" and line:
                IPs.append(line)
            elif mode == "Usernames" and line:
                Usernames.append(line)


Load()
loop = True
while loop:
    print("What do you want to do\n1: Add to Access List\n2: Remove from Access List\n3: Check activity\n4: Save and Exit")
    num = input()
    if num == "1":
        Add()
    elif num == "2":
        Remove()
    elif num == "3":
        #report()
        print("Checking")
    elif num == "4":
        Save()
        loop = False
    else:
        print("Invalid option. Please enter 1, 2, 3, or 4")
