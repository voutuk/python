import paramiko, subprocess
from secrets import username, password
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='10.10.13.123', port=2255, username=username, key_filename="paramiko")


stdin, stdout, stderr = ssh_client.exec_command("ip firewall/filter/add chain=forward action=accept")
stdin, stdout, stderr = ssh_client.exec_command("ip firewall/nat/add chain=srcnat action=masquerade")
