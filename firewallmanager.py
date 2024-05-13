import subprocess

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
    with open("ufw.txt", "a") as file:
        for port in Ports:
            file.write(f"ufw allow {port}\n")
        for ip in IPs:
            file.write(f"ufw allow from {ip}\n")

def SaveDenied():
    with open("ufw.txt", "a") as file:
        for port in DeniedPorts:
            file.write(f"ufw deny {port}\n")
        for ip in DeniedIPs:
            file.write(f"ufw deny from {ip}\n")

def Load():
    global Ports, IPs
    with open("ufw.txt", "r") as file:
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

def Check():
    try:
        result = subprocess.run(['python3', 'logger.py'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return
    else:
        print("Successfully checked activity.")
        with open("activity_log.txt", "w") as file:
            file.write(output)

def Recon():
    try:
        result = subprocess.run(['bash', 'recon.sh'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return
    else:
        print("Successfully checked activity.")
        
def Update():
    try:
        subprocess.run(['bash', 'cmds.sh'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("stderr:", e.stderr.decode())
        return
    else:
        print("Successfully checked activity.")

Load()
loop = True
while loop:
    print("What do you want to do\n1: Add to Access List\n2: Deny from Access List\n3: Check activity\n4: Do recon\n5: Save and Exit")
    num = input()
    if num == "1":
        Add()
    elif num == "2":
        Deny()
    elif num == "3":
        Check()
    elif num == "4":
    	Recon()
    elif num == "5":
        Save()
        SaveDenied()
        Update()
        loop = False
    else:
        print("Invalid option. Please enter 1, 2, 3, or 4")
