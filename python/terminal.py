from tkinter import *
from tkterminal import Terminal


def bin_bash():
    root = Tk()
    root.title("Terminal")

    terminal = Terminal(pady=5, padx=5)
    terminal.shell = True
    terminal.linebar = True
    terminal.basename = "TEST$"
    #terminal.run_command("docker run -d -p 2022:22 pghoon/ssh_ubuntu")
    #terminal.run_command("ssh test@localhost -p 2022")
    terminal.pack(expand=True, fill='both')

    root.mainloop()

bin_bash()