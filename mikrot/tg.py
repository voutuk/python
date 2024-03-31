import paramiko, subprocess, telebot
from secrets import username, token

bot = telebot.TeleBot(token)

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

def BlockIP(message):
    # Отримання списку IP-адрес з DHCP
    message_text = "DHCP LIST:\n============================\n"
    stdin, stdout, stderr = ssh_client.exec_command('ip dhcp-server/lease/print')
    for line in stdout:
        message_text += line.strip('\n') + "\n"
    message_text += "\n============================\n"

    # Надсилання списку IP-адрес у чат
    bot.send_message(message.chat.id, message_text)

    # Отримання IP-адреси для блокування
    bot.send_message(message.chat.id, "Enter IP address [10.10.13.123]: ")
    
    # Очікування введення користувача
    @bot.message_handler(func=lambda m: True)
    def get_user_input(message):
        user_input = message.text
        
        # Виконання команди для блокування IP-адреси
        command = "/ip/firewall/address-list add address={} list=block".format(user_input)
        print(command)
        stdin, stdout, stderr = ssh_client.exec_command(command)
        
        # Отримання результату виконання команди
        message_text = ""
        for line in stdout:
            message_text += line.strip('\n') + "\n"

        if message_text:
            bot.send_message(chat_id=message.chat.id, text=message_text)
        else:
            bot.send_message(chat_id=message.chat.id, text="Blocked IP")


def UNBlockIP(message):
    message_text = "RULE LIST:\n============================\n"
    stdin, stdout, stderr = ssh_client.exec_command('/ip/firewall/address-list print')
    for line in stdout:
        message_text += line.strip('\n') + "\n"
    message_text += "\n============================\n"

    bot.send_message(message.chat.id, message_text)
    bot.send_message(message.chat.id, "Enter #[0-1-2]: ")
    
    @bot.message_handler(func=lambda m: True)
    def get_user_input(message):
        user_input = message.text
        
        # Виконання команди для блокування IP-адреси
        stdin, stdout, stderr = ssh_client.exec_command("/ip/firewall/address-list remove numbers={}".format(user_input))
        message_text = ""
        for line in stdout:
            message_text += line.strip('\n') + "\n"

        if message_text:
            bot.send_message(chat_id=message.chat.id, text=message_text)
        else:
            bot.send_message(chat_id=message.chat.id, text="Unblocked IP")

def addDNS():
    addDNS = input("Enter dns ip[1.1.1.1]: ")
    stdin, stdout, stderr = ssh_client.exec_command("ip dns/set servers="+addDNS)
    for line in stdout:
        print(line.strip('\n'))
    input("-ENTER-")
    subprocess.run("cls", shell=True) 

def RuleOFF(chat_id):
    stdin, stdout, stderr = ssh_client.exec_command("/ip/firewall/nat/ disable numbers=0")
    output_lines = [line.strip('\n') for line in stdout]
    output_message = "\n".join(output_lines)
    if output_message:
        bot.send_message(chat_id=chat_id, text=output_message)
    else:
        bot.send_message(chat_id=chat_id, text="Firewall OFF")

def RuleON(chat_id):
    stdin, stdout, stderr = ssh_client.exec_command("/ip/firewall/nat/ enable numbers=0")
    output_lines = [line.strip('\n') for line in stdout]
    output_message = "\n".join(output_lines)
    if output_message:
        bot.send_message(chat_id=chat_id, text=output_message)
    else:
        bot.send_message(chat_id=chat_id, text="Firewall ON")

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

    @bot.message_handler(commands=['firewallON'])
    def firewallonn(message):
        RuleON(message.chat.id)
    @bot.message_handler(commands=['firewallOFF'])
    def firewallofff(message):
        RuleOFF(message.chat.id)
    @bot.message_handler(commands=['blockip'])
    def handle_blockip(message):
        BlockIP(message)
    @bot.message_handler(commands=['unblockip'])
    def handle_ubblockip(message):
        UNBlockIP(message)
    bot.polling()
