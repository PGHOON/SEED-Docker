import subprocess
import os

subprocess.run(["docker", "run", "-d", "-p", "22:22", "ssh_test:1.3"])
subprocess.run(["open", "-a", "Terminal"])

## ssh -v test@localhost
## sudo unminimize

"""docker install for Ubuntu20.04
https://docs.docker.com/engine/install/ubuntu/

sudo systemctl status docker
"""

##service --status-all

