import tkinter as tk
import subprocess
import webbrowser
import os

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Root window
        self.title('GUI Chooser')
        self.geometry('480x320')
        self.resizable(False, False)

        # Button
        self.button = tk.Button(self, text='Ubuntu:SSH')
        self.button['command'] = self.Xterm
        self.button.pack()

        # Option menu
        self.OSs = ('Ubuntu', 'Fedora Linux', 'Arch Linux', 'Mint Linux')
        self.var = tk.StringVar(value=self.OSs)
        self.option = tk.OptionMenu(self, self.var, "Select OS",*self.OSs)
        self.option.pack()

        # Menu
        menubar = Menu(self)
        self.config(menu=menubar)

    #The & at the end of the command will run the process in the background, so the Python script will continue to execute.
    def Xterm(self):
        subprocess.run(["docker", "run", "-d", "-p", "22:22", "ssh_test:1.0"])
        os.system('xterm -geometry 100x30-0+0 -sb -e "ssh -p 22 test@localhost" &')

    def GnomeTerminal(self):
        subprocess.run(["docker", "run", "-d", "-p", "22:22", "ssh_test:1.0"])
        os.system('gnome-terminal -- ssh -p 22 test@localhost &')

    def ITerm2(self):
        subprocess.run(["docker", "run", "-d", "-p", "22:22", "ssh_test:1.0"])
        os.system('open -a iTerm "ssh -p 22 test@localhost" &')

    def Terminal(self):
        subprocess.run(["docker", "run", "-d", "-p", "22:22", "ssh_test:1.0"])
        subprocess.run(["open", "-a", "Terminal", "ssh", "-p", "22", "test@localhost", "&"])



class Menu(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        # File
        file = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File", underline=0, menu=file)
        file.add_command(label="Exit", underline=1, command=self.exit)

        # Help
        help = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Help", underline=0, menu=help)
        help.add_command(label="Github", underline=1, command=self.PGHOON_Github)

    def exit(self):
        app.destroy()

    def PGHOON_Github(self):
        webbrowser.open_new_tab("https://github.com/PGHOON/SEED-Docker.git")


if __name__ == "__main__":
    app = App()
    app.mainloop()
