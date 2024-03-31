import paramiko, subprocess
from secrets import username, password
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='10.10.13.123', port=2255, username=username, key_filename="paramiko")

def user():
    stdin, stdout, stderr = ssh_client.exec_command('user/print')
    print("\nРезультат:\n=====================================================================")
    for line in stdout:
        print(line.strip('\n'))
    print("=====================================================================\n")
    input("-ENTER-")
    subprocess.run("cls", shell=True) 

def addIP():
    print("Interface: \n============================")
    stdin, stdout, stderr = ssh_client.exec_command('interface/print')
    for line in stdout:
        print(line.strip('\n'))
    print("\n============================")
    addIP = input("Enter ip[10.10.13.123/24]: ")
    addInterface = input("Enter interface[ether1]: ")
    stdin, stdout, stderr = ssh_client.exec_command("ip address/add address="+addIP+" interface="+addInterface)
    for line in stdout:
        print(line.strip('\n'))
    input("-ENTER-")
    subprocess.run("cls", shell=True) 

def addGateway():
    addGateway = input("Enter gateway[10.10.13.254]: ")
    stdin, stdout, stderr = ssh_client.exec_command("ip route/add dst-address=0.0.0.0/0 gateway="+addGateway)
    for line in stdout:
        print(line.strip('\n'))
    input("-ENTER-")
    subprocess.run("cls", shell=True) 

def EnableInt():
    stdin, stdout, stderr = ssh_client.exec_command("ip firewall/filter/add chain=forward action=accept")
    for line in stdout:
        print(line.strip('\n'))
    stdin, stdout, stderr = ssh_client.exec_command("ip firewall/nat/add chain=srcnat action=masquerade")
    for line in stdout:
        print(line.strip('\n'))
    input("-ENTER-")
    subprocess.run("cls", shell=True) 

def addDNS():
    addDNS = input("Enter dns ip[1.1.1.1]: ")
    stdin, stdout, stderr = ssh_client.exec_command("ip dns/set servers="+addDNS)
    for line in stdout:
        print(line.strip('\n'))
    input("-ENTER-")
    subprocess.run("cls", shell=True) 

def ping():
    print("\nРезультат:\n=====================================================================")
    stdin, stdout, stderr = ssh_client.exec_command('ping github.com count=5')
    for line in stdout:
        print(line.strip('\n'))
    print("=====================================================================\n")
    input("-ENTER-")
    subprocess.run("cls", shell=True) 


def menu():
    subprocess.run("cls", shell=True) 
    while (True):
        print("1. Check internet")
        print("2. Print user")
        print("3. Add IP")
        print("4. Add Gateway")
        print("5. Enable Internet")
        print("6. Add DNS")
        print("7. Exit")
        temp = input("Виберіть опцію: ")
        if(temp == "1"): ping()
        elif(temp == "2"): user()
        elif(temp == "3"): addIP()
        elif(temp == "4"): addGateway()
        elif(temp == "5"): EnableInt()
        elif(temp == "6"): addDNS()
        elif(temp == "7"): 
            ssh_client.close()
            exit()

if __name__ == '__main__':
    menu()
