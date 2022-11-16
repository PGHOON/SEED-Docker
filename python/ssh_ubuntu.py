import os

def ssh_ubuntu():
    os.system("docker run -d -p 2022:22 pghoon/ssh_ubuntu")
    os.system("ssh test@localhost -p 2022")

ssh_ubuntu()