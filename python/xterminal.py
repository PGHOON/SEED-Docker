from tkinter import *
import os

window = Tk()
window.title("TEST")
window.attributes("-topmost",True)
window.geometry("480x320")

ubuntu = PhotoImage(file = "./ubuntu.png")
#ubuntu_exec = PhotoImage(file = "./ubuntu_exec.png")

label1 = Label(window, image = ubuntu, borderwidth = "2")
label1.pack()

def bin_bash():
    termf = Frame(window, height=400, width=500)

    termf.pack(fill=BOTH, expand=YES)
    wid = termf.winfo_id()
    os.system("docker run -d -p 2022:22 pghoon/ssh_ubuntu")
    os.system('xterm -into %d -geometry 100x30-0+0 -sb -e "sshpass -p "test" ssh -p 2022 test@localhost" &' % wid)
    os.system("clear")

b1 = Button(window, text = "connect", borderwidth = "2", relief="ridge", command = bin_bash)
b1.pack()


"""
b2 = Button(window, text = "Stop container",  borderwidth = "2", relief="ridge", command = os.system("docker stop `docker ps -a -q`"))
b2.pack()
os.system("docker rm `docker ps -a -q` &")
"""

window.mainloop()