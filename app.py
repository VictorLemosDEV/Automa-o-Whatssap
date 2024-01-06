from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils.file import read_file
from utils.whatsapp import send_message
import os

import psutil

from threading import Thread

import chromedriver_autoinstaller


chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

import utils.gui.gui as Interface

cwd = os.path.abspath(os.getcwd())

def is_browser_open():
    for process in psutil.process_iter(['pid', 'name']):
        if 'chrome' in process.info['name'].lower():
            return True
    return False

def open_or_get_existing_browser():
    s = Service(ChromeDriverManager().install())

    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    #chrome_options.add_argument("--headless=new")
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
    # Get messages
    message = read_file(cwd+ rf"\_internal\assets\message.txt")

    # Get all contacts
    contacts = read_file(cwd + rf"\_internal\assets\contacts.txt", array=True)

    # Initialize Chrome Driver
    
   
    driver = open_or_get_existing_browser()

    # Send WhatsApp Message
    send_message(driver=driver, contacts=contacts, message=message, canvas=canvas)

    


if __name__ == "__main__":
    InterfaceThread = Thread(target=Interface.Init, args=[Trigger])
    InterfaceThread.start()

