from customtkinter import *
import tkinter as tk

import psutil

from PIL import Image, ImageTk

from utils.transition import *

import colour

from excel import *

from utils.file import *

import app


import time

from threading import Thread



from selenium import webdriver
from selenium.common.exceptions import WebDriverException

cwd = os.path.abspath(os.getcwd())

def is_chrome_open():
    for process in psutil.process_iter(['pid', 'name']):
        if 'chromedriver' in process.info['name'].lower():
            return True
    return False

# Exemplo de uso
import random

def gerar_numero():
    return "55 " + str(random.randint(10, 99)) + " " + str(random.randint(1000, 9999)) + "-" + str(random.randint(1000, 9999))




class App(CTk):
    def __init__(self,Trigger):
        super().__init__()

        self.Trigger = Trigger

        self.CurrentMenu = "None"

        self.SidebarMenu = {
    "Default" : self.mostrar_mensagem,
    "Mensagens" : self.mostrar_mensagem,
    "Contatos" : self.mostrar_contatos
}

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

        image = tk.PhotoImage("Logo",master=self,file=cwd + rf'\utils\gui\assets\frame0\image_1.png')
       
        


        self.Logo = CTkLabel(self.Sidebar,100,100,image=image,text="")
        self.Logo.place(x=50,y=10)


        self.Mensagens = CTkButton(self.Sidebar, text="Mensagens", command=self.SidebarMenu["Mensagens"], bg_color="#111111", fg_color="#121212", height=75, width=250,hover_color="#121111",font=CTkFont("Helvetica",30,"normal"))
        #self.Mensagens = CTkButton(self.Sidebar,250,75,fg_color="#121212",hover_color="#2b2b2b",text="Mensagens",font=CTkFont("Helvetica",30,"normal"))
        self.Mensagens.place(x=0,y=200)

        #self.Contatos = CTkButton(self.Sidebar,250,75,fg_color="#121212",hover_color="#2b2b2b",text="Contatos",command=self.LerTelefones,font=CTkFont("Helvetica",30,"normal"))
        self.Contatos = CTkButton(self.Sidebar, text="Contatos", command=self.SidebarMenu["Contatos"], bg_color="#111111", fg_color="#121212", height=75, width=250,hover_color="#2b2b2b",font=CTkFont("Helvetica",30,"normal"))
        self.Contatos.place(x=0,y=300)

        self.quadrado_direita = CTkFrame(self, width=width - 250, height=height, fg_color="#232323")
        self.quadrado_direita.place(x=250,y=0)
        #self.quadrado_direita.pack(side=RIGHT, fill=BOTH, expand=True)

        


        self.botao_adicionar = CTkButton(self.quadrado_direita, text="+ Adicionar Contatos", command=self.adicionar_contato, fg_color="transparent",  width=38, height=5,hover_color="#121111",font=CTkFont("Helvetica",30,"bold"))  

        self.botao_adicionar.place(relx=0.5,rely=0.5,anchor="center")
        self.botao_enviar = CTkButton(self.quadrado_direita, text="Enviar", fg_color="#343230", bg_color="#343230", width=500, height=100,hover_color="#121111",anchor=CENTER)  
        self.label_enviando = CTkLabel(self.quadrado_direita, text="Enviando 1/20000...", fg_color="#1c1a1b", bg_color="#232323",text_color="white")

        def Cancelar_Envio():
            app.IS_SENDING_ACTIVE = False



        self.quadrado_contatos = CTkFrame(self.quadrado_direita,  width=600, height=300,fg_color="#1c1a1b")  
        self.label_contatos = CTkLabel(self.quadrado_contatos, text="Grupo de Contatos 1", fg_color="#121111",text_color="white")
        self.contacts_text_box = CTkTextbox(self.quadrado_contatos,text_color="white",fg_color="#121111",width=500,height=150)

        def LerTelefones():
            DataFile = OpenFileDialog()

            if DataFile:
                lista = GetPhoneList(DataFile,"Telefone")
                Contatos = ""
                for x in lista:
                    Contatos = Contatos + x + "\n"
            
                self.contacts_text_box.insert("0.0",Contatos)
                try:
                    replace_file(cwd+ rf"\_internal\assets\contacts.txt",Contatos)
                except FileNotFoundError:
                    replace_file(cwd+ rf"\assets\contacts.txt",Contatos)
                

        attach_image_file = CTkImage(Image.open(cwd + rf'\utils\gui\assets\frame0\attach_file.png'),size=(25,25))

        self.label_attach_file = CTkButton(self.quadrado_contatos,width=10,height=10,image=attach_image_file,fg_color="transparent",text="",hover_color="",bg_color="transparent",command=LerTelefones)
        self.label_attach_file.place(relx=0.1,rely=0.9,anchor="center")

        
       
        


        #botao1 = CTkButton(self.Sidebar, text="Mensagens", command=SidebarMenu["Mensagens"], bg_color="#111111", fg_color="#111111", height=2, width=15,hover_color="#121111")
        #botao1.pack(pady=6, padx=(0, 0), fill=X)

        #botao2 = CTkButton(self.Sidebar, text="Contatos", command=SidebarMenu["Contatos"], bg_color="#111111", fg_color="#111111", height=2, width=15,hover_color="#121111")
        #botao2.pack(pady=6, padx=0, fill=X)

        #botao3 = CTkButton(self.Sidebar, text="Registro", command=lambda: print("Botão 3 clicado"), bg_color="#111111", fg_color="#111111", height=2, width=15,hover_color="#121111")
        #botao3.pack(pady=6, padx=0, fill=X)

        #botao4 = CTkButton(self.Sidebar, text="Configurações", command=lambda: print("Botão 4 clicado"), bg_color="#111111", fg_color="#111111", height=2, width=15,hover_color="#121111")
        #botao4.pack(side=BOTTOM, pady=25, padx=0, fill=X)

        self.SidebarMenu["Default"]()

    def Start(self):

        try:
            replace_file(cwd+ rf"\_internal\assets\message.txt",self.label_conteudo.get("1.0",END))
            replace_file(cwd+ rf"\_internal\assets\contacts.txt",self.contacts_text_box.get("1.0",END))
        except FileNotFoundError:
            replace_file(cwd+ rf"\assets\message.txt",self.label_conteudo.get("1.0",END))
            replace_file(cwd+ rf"\assets\contacts.txt",self.contacts_text_box.get("1.0",END))


        def UpdateFilesAndDeploy():

            if is_chrome_open():
                print("Já está aberto")
                #EditLabel(canvas,StatusLabel,"O Navegador já está abrindo, por favor aguarde...")
            else:
                print("Não está aberto")
                #Change_Message(entry_2.get("1.0",tkinter.END))
                #Change_Contacts(entry_1.get("1.0",tkinter.END))

                #EditLabel(canvas,StatusLabel,"Abrindo Navegador...")

                print(self)

                browserThread = Thread(target=self.Trigger,args=[self],name="browser")
                #browserThread.daemon = True
                browserThread.start()

        UpdateFilesAndDeploy()
        

    
    
    
    


    def mostrar_mensagem(self,event=None):
        if self.CurrentMenu == "Mensagens":
            return
        
        self.CurrentMenu = "Mensagens"

        self.esconder_contatos()  
        self.quadrado_mensagem1 = CTkFrame(self.quadrado_direita, fg_color="#1c1a1b", width=1000, height=250)
        self.quadrado_mensagem1.place(relx=0.5,rely=0.3,anchor="s")


        self.label_mensagem1 = CTkLabel(self.quadrado_mensagem1, text="Campo de Mensagem", fg_color="transparent",text_color="white")
        self.label_mensagem1.place(relx=0.5,rely=0.2, anchor="s")
        self.label_conteudo = CTkTextbox(self.quadrado_mensagem1,width=800,height=200, fg_color="#111111",text_color="white",font=CTkFont("Helvetica",15,"normal"))

        
        self.label_conteudo.place(relx=0.5,rely=0.5,anchor="center")
        self.label_conteudo.insert("0.0","Escreva sua mensagem aqui")

        




       

        self.botao_enviar = CTkButton(self.quadrado_direita, text="Enviar",command=self.Start, fg_color="#343230", bg_color="#343230", width=500, height=100,hover_color="#121111",anchor=CENTER)    
        self.botao_enviar.place(relx=0.5,rely=0.5,anchor="center")

        def Cancelar_Envio():
            IS_SENDING_ACTIVE = False


        self.botao_parar = CTkButton(self.quadrado_direita,text="Cancelar Envio",fg_color="#e8201a",width=500,height=100,hover_color="#a60c07",anchor="center", command=Cancelar_Envio)
        self.botao_parar.place(relx=0.5,rely=0.7,anchor="center")


        self.qrcodeLabel = CTkLabel(self.quadrado_direita,100,100,text="")
        #self.qrcodeLabel.place(relx=0.5,rely=0.5,anchor="nw")

    def esconder_mensagem1(self,event=None):
        try:
            self.label_mensagem1.destroy()
            self.label_conteudo.destroy()
            self.quadrado_mensagem1.destroy()
            self.botao_enviar.destroy()
            self.botao_parar.destroy()
            self.label_enviando.destroy() 
        except AttributeError:
            pass

        

    def mostrar_contatos(self,event=None):
        if self.CurrentMenu == "Contatos":
            return
        
        
        
        self.CurrentMenu = "Contatos"

        self.esconder_mensagem1()
        self.quadrado_contatos.place(x=104, y=50)
        self.label_contatos.place(x=105, y=7)
        self.contacts_text_box.place(relx=0.1,rely=0.3)

        
        self.label_enviando.place_forget()


        

    def esconder_contatos(self,event=None):
        try:
            self.label_contatos.place_forget()
            self.quadrado_contatos.place_forget()
            self.label_contato1.place_forget()  
            self.label_numero1.place_forget()  
            self.label_contato2.place_forget()  
            self.label_numero2.place_forget()  
            #label_imagem_contato1.place_forget()  
            #label_imagem_contato2.place_forget()  
        except AttributeError:
            pass

    def adicionar_contato(self):
        
        novo_contato = gerar_numero()
        
        if self.label_contato1.cget("text") == "":
            self.label_contato1.config(text="Novo Contato 1")
            self.label_numero1.config(text=novo_contato)
        elif self.label_contato2.cget("text") == "":
            self.label_contato2.config(text="Novo Contato 2")
            self.label_numero2.config(text=novo_contato)

    def MostrarQrCode(self, image):
        if self.qrcodeLabel:
            image = CTkImage(image,image,(300,300))
            self.qrcodeLabel.configure(image=image)
            self.qrcodeLabel.place(relx=0.1,rely=0.5,anchor="center")
            print("Chegou aqui")














#imagem = tk.PhotoImage(file="./image_1.png")
#imagem = imagem.subsample(3, 3)
#label_imagem = CTkLabel(self.Sidebar, image=imagem, fg_color="black",text="")
#label_imagem.pack(pady=(25, 40))




# Carregar a imagem
#imagem_contato = tk.PhotoImage(file="./green.png")

# Carregar a segunda imagem
#imagem_contato2 = tk.PhotoImage(file="./x.png")

# Redimensionar a imagem
#imagem_contato2 = imagem_contato2.subsample(3, 3)  

# Redimensionar a imagem
#imagem_contato = imagem_contato.subsample(3, 3)  

# Criar um rótulo com a imagem
#label_imagem_contato1 = CTkLabel(self.quadrado_contatos, image=imagem_contato,text="")
#label_imagem_contato2 = CTkLabel(self.quadrado_contatos, image=imagem_contato2,text="")

# Posicionar o rótulo na interface
#label_imagem_contato1.place(x=300, y=30)  
#label_imagem_contato2.place(x=300, y=60)  


app = None

def StartApplication(Trigger):
    global app
    print("----------------------------------------------------------------------")
    print("Atualizou app")
    print("----------------------------------------------------------------------")
    try:
        
        app = App(Trigger)

        print("----------------------------------------------------------------------")
        print("Terminou de atualizar app")
        print("----------------------------------------------------------------------")

        app.mainloop() 
        print(app)
    except KeyboardInterrupt:
        app.destroy()


def DisplayQRCode(image):
    global app
    print(app)
    try:
        app.MostrarQrCode(image)
    except Exception as e:
        print(e)
        print("App não existe")




