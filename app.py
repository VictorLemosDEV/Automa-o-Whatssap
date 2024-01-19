from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils.file import read_file
from utils.file import replace_file
import os

import json

import psutil



from threading import Thread

import chromedriver_autoinstaller


chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

import interface as Interface

cwd = os.path.abspath(os.getcwd())

APP_THREADS = []
IS_SENDING_ACTIVE = True

# Retorna se o navegador já está aberto
def is_browser_open():
    for process in psutil.process_iter(['pid', 'name']):
        if 'chrome' in process.info['name'].lower():
            return True
    return False


# Configurações Padrões
DefaultConfiguration = {
    "Headless": True,
    "Maximized": True,
    "ToleranceTime": 120,
}

# Lê as configurações e retorna ela
def GetConfig():
    #Load Configuration

    try:
        Config = read_file(cwd+ rf"\_internal\assets\config.json",False)
        if len(Config) < 1:
            Config = DefaultConfiguration
            replace_file(cwd+ rf"\_internal\assets\config.json",json.dumps(Config))
        else:
            Config = json.loads(Config)

    except FileNotFoundError:
        Config = read_file(cwd+ rf"\assets\config.json",False)
        if len(Config) < 1:
            Config = DefaultConfiguration
            replace_file(cwd+ rf"\assets\config.json",json.dumps(Config))
        else:
            Config = json.loads(Config)
        

    

    return Config

# Abre ou retorna um navegador já existente
def open_or_get_existing_browser():

    
    Config = GetConfig()



    # Instala o chrome driver caso ele não exista
    s = Service(ChromeDriverManager().install())

    chrome_options = Options()
    if Config["Maximized"]:
        chrome_options.add_argument("start-maximized")
    
    if Config["Headless"]:
        chrome_options.add_argument("--headless=new")


    # Essa linha permite carregar os dados de login do whatsapp sem a necessidade do usuário escanear o código novamente
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-data/" + "Selenium")


    if is_browser_open():
        # Se o navegador já estiver aberto, obtenha a instância existente
        existing_browser = webdriver.Chrome(service=s, options=chrome_options)
        return existing_browser
    else:
        # Caso contrário, crie uma nova instância do navegador
        new_browser = webdriver.Chrome()
        return new_browser





def Trigger(canvas):
    from utils.whatsapp import send_message
    print("Abriu")

    try:
        # Get messages
        message = read_file(cwd+ rf"\_internal\assets\message.txt")

    # Get all contacts
        contacts = read_file(cwd + rf"\_internal\assets\contacts.txt", array=True)

    except FileNotFoundError as error:
         message = read_file(cwd+ rf"\assets\message.txt")

    # Get all contacts
         contacts = read_file(cwd + rf"\assets\contacts.txt", array=True)

    # Initialize Chrome Driver
    
   
    driver = open_or_get_existing_browser()

    # Send WhatsApp Message
    try:
        send_message(driver=driver, contacts=contacts, message=message,canvas=canvas)
    except KeyboardInterrupt:
        driver.close()
    


if __name__ == "__main__":
    Interface.StartApplication(Trigger)

    #InterfaceThread = Thread(target=Interface.StartApplication, args=[Trigger])
    #InterfaceThread.start()

