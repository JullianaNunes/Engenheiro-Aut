import paramiko 
import sys

def main():
    hostname = str(sys.argv[1]) 
    username = str(sys.argv[2])
    password = str(sys.argv[3])

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)

    command = "echo {pwd} | sudo -S /etc/init.d/mysql restart; echo {pwd} |  sudo -S /etc/init.d/mysql status ".format(pwd=password)
    stdin, stdout, stderr = client.exec_command(command)
    lines = stdout.readlines()
    client.close()
    print(lines)

if __name__ == "__main__":
    main()