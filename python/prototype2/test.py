import tkinter as tk
import subprocess

def run_image():
    subprocess.run(["docker", "run", "-d", "-p", "22:22", "ssh_test:1.0"])\
    
    subprocess.run(["open", "-a", "Terminal", "ssh", "test@localhost"])


    # Start a Docker container in the new terminal window
    #subprocess.run(["docker", "run", "-it", "-name", "test3", "-p", "22:22", "ssh_test:1.0", "/bin/bash"])

    "docker run -d --name mycontainer -p 22:22 myimage:1.0"
    "docker run -it --name mycontainer -p 22:22 myimage:1.0 /bin/bash"



# Create the GUI window
root = tk.Tk()
root.title("Docker Image Runner")

# Add a button to the window
button = tk.Button(root, text="Run Image", command=run_image)
button.pack()

# Start the GUI event loop
root.mainloop()
