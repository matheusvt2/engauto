import paramiko 
import sys
from scp import SCPClient

def main():
    hostname = str(sys.argv[1])
    username = str(sys.argv[2]) 
    password = str(sys.argv[3])

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)  

    sftp = client.open_sftp() 
    sftp.put("remediacao/config/docker-compose.yml", "/home/matheus/docker-compose.yml")
    sftp.close()
    client.close()


    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)  
    command = "echo {pwd} | sudo -S docker-compose -f /home/matheus/docker-compose.yml up -d".format(pwd=password)
    stdin, stdout, stderr = client.exec_command(command)
   
    lines = stdout.readlines()
    lines2 = stderr.readlines()
    
    print(lines,lines2)

if __name__ == "__main__":
    main()