Ports = []
IPs = []
AccessList = [Ports, IPs]
DeniedPorts = []
DeniedIPs = []
DeniedList = [DeniedPorts, DeniedIPs]

def Print():
    print(f"Ports: {AccessList[0]}")
    print(f"IPs: {AccessList[1]}")
    print(f"Denied Ports: {DeniedList[0]}")
    print(f"Denied IPs: {DeniedList[1]}")

def Add():
    toAdd = int(input("What do you want to add to the list?\n1: Port\n2: IP\n3: Exit"))
    if toAdd == 1:
        portAdd = int(input("Enter Port number: "))
        Ports.append(portAdd)
        Add()
    elif toAdd == 2:
        ipAdd = input("Enter IP Address: ")
        IPs.append(ipAdd)
        Add()
    elif toAdd == 3:
        Print()
    else:
        print("Invalid option. Please enter 1, 2, or 3")

def Deny():
    toDeny = int(input("What do you want to deny?\n1: Port\n2: IP\n3: Exit"))
    if toDeny == 1:
        portDeny = int(input("Enter Port number: "))
        DeniedPorts.append(portDeny)
        Deny()
    elif toDeny == 2:
        ipDeny = input("Enter IP Address: ")
        DeniedIPs.append(ipDeny)
        Deny()
    elif toDeny == 3:
        Print()
    else:
        print("Invalid option. Please enter 1, 2, or 3")

def Save():
    with open("acl.txt", "a") as file:
        for port in Ports:
            file.write(f"ufw allow {port}\n")
        for ip in IPs:
            file.write(f"ufw allow from {ip}\n")

def SaveDenied():
    with open("acl.txt", "a") as file:
        for port in DeniedPorts:
            file.write(f"ufw deny {port}\n")
        for ip in DeniedIPs:
            file.write(f"ufw deny from {ip}\n")

def Load():
    global Ports, IPs
    with open("acl.txt", "r") as file:
        lines = file.readlines()
        mode = None
        for line in lines:
            line = line.strip()
            if line == "Ports:":
                mode = "Ports"
            elif line == "IPs:":
                mode = "IPs"
            elif mode == "Ports" and line:
                Ports.append(int(line))
            elif mode == "IPs" and line:
                IPs.append(line)


Load()
loop = True
while loop:
    print("What do you want to do\n1: Add to Access List\n2: Deny from Access List\n3: Check activity\n4: Save and Exit")
    num = input()
    if num == "1":
        Add()
    elif num == "2":
        Deny()
    elif num == "3":
        #report()
        print("Checking")
    elif num == "4":
        Save()
        SaveDenied()
        loop = False
    else:
        print("Invalid option. Please enter 1, 2, 3, or 4")
