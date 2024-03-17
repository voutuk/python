import paramiko
from secrets import username, password

def get_cap():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname='10.10.13.203', port=2255, username=username, password=password)
    stdin, stdout, stderr = ssh_client.exec_command('ping 1.1.1.1')
    
    for line in stdout:
        print(line.strip('\n'))

    ssh_client.close()

if __name__ == '__main__':
    get_cap()