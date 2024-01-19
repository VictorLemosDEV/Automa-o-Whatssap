from customtkinter import *

import psutil

from PIL import Image

from utils.transition import *

import colour

from excel import *

from utils.file import *


import time


from threading import Thread


from selenium import webdriver
from selenium.common.exceptions import WebDriverException

def is_chrome_open():
    for process in psutil.process_iter(['pid', 'name']):
        if 'chromedriver' in process.info['name'].lower():
            return True
    return False

# Exemplo de uso






cwd = os.path.abspath(os.getcwd())

class App(CTk):
    def __init__(self):
        super().__init__()

        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        height = height - (height / 10)

        self.title("Sparta")
        self.resizable(False,False)
        self.geometry(f"{width}x{height}")
        self.configure(fg_color = "#232323")
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=1)
    

        self.Sidebar = CTkFrame(self,250,height * 2,fg_color="#000000")
        self.Sidebar.grid(row=1,column=1,sticky="sw")

        image = Image.open(cwd + rf"\utils\gui\assets\frame0\image_1.png")

        self.Image = CTkImage(image,image,(100,100))

        self.Logo = CTkLabel(self.Sidebar,100,100,image=self.Image,text="")
        self.Logo.place(x=75,y=10)

        self.Mensagens = CTkButton(self.Sidebar,250,75,fg_color="#121212",hover_color="#2b2b2b",text="Mensagens")
        self.Mensagens.place(x=0,y=200)

        

        def LerTelefones():
            DataFile = OpenFileDialog()

            if DataFile:
                lista = GetPhoneList(DataFile,"Telefone")
                print(lista)
        
        
        self.Contatos = CTkButton(self.Sidebar,250,75,fg_color="#121212",hover_color="#2b2b2b",text="Contatos",command=LerTelefones)
        self.Contatos.place(x=0,y=300)



        #self.Contatos.bind("<Enter>",lambda e: Transition((self.Contatos,start_color,end_color)), add="+")





   

class MyCheckboxFrame(CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            checkbox = CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes


def Init(Trigger):
    app = App()
    app.mainloop()



Init(False)