import threading
import time
import paramiko, subprocess
from secrets import username, password
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='10.10.13.123', port=2255, username=username, key_filename="paramiko")

def task1():
    while (True):
        stdin, stdout, stderr = ssh_client.exec_command('tool/flood-ping address=10.10.13.33 size=1500 count=1000')
        for line in stdout:
            print(line.strip('\n'))


if __name__ == "__main__":
    # Створюємо два потоки для виконання різних завдань
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task1)

    # Запускаємо обидва потоки
    thread1.start()
    thread2.start()

    # Очікуємо завершення обох потоків
    thread1.join()
    thread2.join()

    print("Both threads have finished execution")
