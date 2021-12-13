import paramiko 
import sys

def main():
    hostname = str(sys.argv[1])
    username = str(sys.argv[2]) 
    password = str(sys.argv[3])

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)

    command = "ls -la"
    stdin, stdout, stderr = client.exec_command(command)
    lines = stdout.readlines()
    lines2 = stderr.readlines()
    print(lines,lines2)
   
if __name__ == "__main__":
    main()