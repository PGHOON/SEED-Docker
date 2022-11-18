import tkinter as tk
from tkinter import ttk
import os
import webbrowser

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #root window
        self.title('GUI Chooser')
        self.geometry('480x320')
        self.resizable(False, False)

        #label

        #button
        self.button = tk.Button(self, text='Ubuntu:SSH')
        self.button['command'] = self.Xterm
        self.button.pack()

        #option menu
        self.OSs = ('Ubuntu', 'Fedora Linux', 'Arch Linux', 'Mint Linux')
        self.var = tk.StringVar(value=self.OSs)
        self.option = ttk.OptionMenu(self, self.var, "Select OS",*self.OSs)
        self.option.pack()

        #menu
        menubar = Menu(self)
        self.config(menu=menubar)

    def Xterm(self):
        wid = self.winfo_id()
        os.system('docker run -d -p 2022:22 pghoon/ssh_ubuntu')
        os.system('xterm -into %d -geometry 100x30-0+0 -sb -e "sshpass -p "test" ssh -p 2022 test@localhost" &' % wid)
        os.system("clear")




class Menu(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        #file
        file = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=file)
        file.add_command(label="Exit", underline=1, command=self.exit)

        #help
        hellp = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Help",underline=0, menu=hellp)
        hellp.add_command(label="Github", underline=1, command=self.PGHOON_Github)
    
    def exit(self):
        app.destroy()

    def PGHOON_Github(url):
        webbrowser.open_new_tab("https://github.com/PGHOON/SEED-Docker.git")


######################################################################################################################################


if __name__ == "__main__":
    app = App()
    app.mainloop()