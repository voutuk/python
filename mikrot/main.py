import paramiko, subprocess, telebot
from secrets import username, token
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

def BlockIP():
    print("DHCP LIST: \n============================")
    stdin, stdout, stderr = ssh_client.exec_command('ip dhcp-server/lease/print')
    for line in stdout:
        print(line.strip('\n'))
    print("\n============================")
    blockIP = input("Enter ip[10.10.13.123]: ")
    stdin, stdout, stderr = ssh_client.exec_command("/ip/firewall/address-list add address="+blockIP+" list=block")
    for line in stdout:
        print(line.strip('\n'))
    input("-ENTER-")
    subprocess.run("cls", shell=True) 

def UNBlockIP():
    print("RULE LIST: \n============================")
    stdin, stdout, stderr = ssh_client.exec_command('/ip/firewall/address-list print')
    for line in stdout:
        print(line.strip('\n'))
    print("\n============================")
    UNblockIP = input("Enter #[0-1-2]: ")
    stdin, stdout, stderr = ssh_client.exec_command("/ip/firewall/address-list remove numbers="+UNblockIP)
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

def RuleOFF():
    stdin, stdout, stderr = ssh_client.exec_command("/ip/firewall/nat/ disable numbers=0")
    for line in stdout:
        print(line.strip('\n'))
    input("-ENTER-")
    subprocess.run("cls", shell=True) 

def RuleON():
    stdin, stdout, stderr = ssh_client.exec_command("/ip/firewall/nat/ enable numbers=0")
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

def saveLOG():
    stdin, stdout, stderr = ssh_client.exec_command('log/print')
    with open('mikrot.log', 'w') as f:
        for line in stdout:
            f.write(line.strip('\n') + '\n')
    f.close()
    input("-ENTER-")
    subprocess.run("cls", shell=True) 

if __name__ == '__main__':
    subprocess.run("cls", shell=True) 
    while (True):
        print("1. Check internet\n2. Print user\n3. Add IP\n4. Add Gateway\n5. Enable Internet\n6. Add DNS\n7. Block IP")
        print("8. Unblock IP")
        print("9. Firewall Internet ON")
        print("10. Firewall Internet OFF")
        print("11. Save log file")
        print("12. Exit")
        temp = input("Виберіть опцію: ")
        if(temp == "1"): ping()
        elif(temp == "2"): user()
        elif(temp == "3"): addIP()
        elif(temp == "4"): addGateway()
        elif(temp == "5"): EnableInt()
        elif(temp == "6"): addDNS()
        elif(temp == "7"): BlockIP()
        elif(temp == "8"): UNBlockIP()
        elif(temp == "9"): RuleON()
        elif(temp == "10"): RuleOFF()
        elif(temp == "11"): saveLOG()
        elif(temp == "12"): 
            ssh_client.close()
            exit()