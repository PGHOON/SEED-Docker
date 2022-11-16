from tkinter import *
from tkterminal import Terminal
import os

window = Tk()
window.title("TEST")
window.attributes("-topmost",True)
window.geometry("960x640")

ubuntu = PhotoImage(file = "./ubuntu.png")
#ubuntu_exec = PhotoImage(file = "./ubuntu_exec.png")

label1 = Label(window, image = ubuntu, borderwidth = "2")
label1.pack()

def bin_bash():
    terminal = Terminal(pady=5, padx=5)
    terminal.shell = True
    terminal.basename = "TEST$"
    #terminal.run_command("docker run -d -p 2022:22 pghoon/ssh_ubuntu")
    #terminal.run_command("ssh test@localhost -p 2022")
    terminal.pack(expand=True, fill='both')

b1 = Button(window, text = "connect", borderwidth = "2", relief="ridge", command = bin_bash)
b1.pack()


"""
b2 = Button(window, text = "Stop container",  borderwidth = "2", relief="ridge", command = os.system("docker stop `docker ps -a -q`"))
b2.pack()
os.system("docker rm `docker ps -a -q` &")
"""

window.mainloop()