import subprocess


# Pop up a new terminal window on macOS
subprocess.run(["open", "-a", "Terminal"])


# Pop up a new xterm terminal window on Linux
#subprocess.run(["xterm"])


# Pop up a new gnome-terminal window on Linux
#subprocess.run(["gnome-terminal"])

# Pop up a new terminal window on Windows
#subprocess.run(["start", "cmd"], shell=True)