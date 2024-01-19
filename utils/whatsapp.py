import urllib
from time import sleep
from .phone_number import is_phone_valid
from .file import write_file, clean_file
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
# from termcolor import colored

from PIL import Image as ImageWrapper

import time

from utils.gui.gui import EditLabel, StatusLabel

import qrcodewrapper

from threading import Thread

import interface

import app

cwd = os.path.abspath(os.getcwd())

WHATSAPP_WEB_URL = 'https://web.whatsapp.com'
DELAY = 120
DELAY_BETWEEN_CONTACTS = 30

THREADS = []

IS_SESSION_ACTIVE = True

def print_empty_lines(n):
    for i in range(n):
        print('\n')


def generate_link(contact, message, web=False):
    message = urllib.parse.quote_plus(message,encoding="utf-8")
    message = urllib.parse.unquote(urllib.parse.quote_plus(message))

    
    

    if web:
        return f"https://web.whatsapp.com/send?phone={contact}&text={message}"
    else:
        return f"https://wa.me/{contact}&text={message}"


def send_message(driver, contacts, message,canvas):
    print_empty_lines(2)
    print(f"Once your browser opens up, sign in to WhatsApp Web...")
    print("Wait for your chats to be visible so you don't have to sign in again.")
    print_empty_lines(1)

    #qrcodewrapper.UpdateQrCode(driver)



    driver.get(WHATSAPP_WEB_URL)



    class QrCodeSearcher():


        def __init__(self,newDriver) -> None:
            self.previousContainerData = ""
            self.driver = newDriver
            self.FoundQrCode = True
            try:
                os.remove("qr-code.png")
            except Exception:
                print("Não encontrou arquivo")

    
    

        def UpdateQrCode(self):

    


            
            

            def GetContainerAttributes():

                
                try:
                    self.canvas = WebDriverWait(self.driver, 20).until(lambda x: x.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div/div[2]/div[2]'))
                    return self.canvas.get_attribute('data-ref')
                
                except Exception as e:
                    print(f"Something went wrong...")
                    self.FoundQrCode = False
                    

                

            def CheckUpdate():
                currentData = GetContainerAttributes()

                if currentData != self.previousContainerData:
                    print("Updated")
                    self.FoundQrCode = True
                    GetQrCodeImage()

            def GetQrCodeImage():
                if self.canvas:
                    self.canvas.screenshot("qr-code.png")
                    
                    image = ImageWrapper.open("qr-code.png")
                    
                    interface.DisplayQRCode(image)

            # get the canvas as a PNG base64 string

            def CallFunctions():
                try:
                    self.canvas = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/canvas'))

                    self.Checker = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div/div[3]/div/span'))
                    
                    print(self.Checker)
                    
                except Exception as e:
                    print(f"Something went wrong...")

                    try:
                        os.remove("qr-code.png")
                    except Exception as e:
                        print("Deletado")


                CheckUpdate()
                time.sleep(20)

            while True:
                CallFunctions()
            

        

        def StartSearch(self):
            QrCodeThread = Thread(target=self.UpdateQrCode,name="QrCodeSearcher")
            QrCodeThread.start()


    seacher = QrCodeSearcher(driver)
    seacher.StartSearch()

    


    
    time.sleep(3)

    #input("Press any key to start...")

    contacts = [x for x in contacts if x]

    try:
        clean_file(cwd + rf"\_internal\assets\invalid_contacts.txt")
    except FileNotFoundError:
        clean_file(cwd + rf"\assets\invalid_contacts.txt")

    for index, contact in enumerate(contacts):
        if app.IS_SENDING_ACTIVE == False:
            break

        isPhoneValid = is_phone_valid(contact)
        #print(isPhoneValid)

        sending_index = index + 1
        total_contacts = len(contacts)

        # if not isPhoneValid:
        #     print(f"{sending_index}/{total_contacts} => Phone number is invalid.")
        #     print_empty_lines(1)

        #     write_file(f"{cwd}/assets/invalid_contacts.txt", contact)

        #     continue

        if contact == "":
            continue

        print(f"{sending_index}/{total_contacts} => Sending message to {contact}.")
        #EditLabel(canvas,StatusLabel,f"{sending_index}/{total_contacts} => Sending message to {contact}.")

        try:
            whatsapp_url = generate_link(contact, message, web=True)
            message_sent = False

            if not message_sent:
                driver.get(whatsapp_url)

                try:
                    send_button = WebDriverWait(driver, DELAY_BETWEEN_CONTACTS).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')))
                except Exception as e:
                    invalid_button = WebDriverWait(driver, 1).until(lambda x: x.find_element(By.CLASS_NAME,'p357zi0d ns59xd2u kcgo1i74 gq7nj7y3 lnjlmjd6 przvwfww mc6o24uu e65innqk le5p0ye3'))
               
                    print(invalid_button)
                    print("-----------------------------------------------")
                    print("BOTÂO LEGAL")
                    print("-----------------------------------------------")

                    print_empty_lines(1)

                    write_file(f"{cwd}/assets/invalid_contacts.txt", contact)

                    continue
                    # print(f"Failed to send message to this contact: {contact}, retry ({sending_index}/3)")
                    # print_empty_lines(1)
                    # print("Make sure your phone and computer are connected to the internet.")
                    # print("If there is an alert, please dismiss it.")
                    # print_empty_lines(1)
                    # input("Press any key to continue...")
                else:
                    sleep(1)

                    send_button.click()
                    message_sent = True

                    sleep(3)

                    print(f"Message sent to: {contact}")
                    print_empty_lines(1)

        except Exception as e:
            try:
                write_file(cwd + "/assets/invalid_contacts.txt", contact)
            except FileNotFoundError:
                write_file(cwd + "/_internal/assets/invalid_contacts.txt", contact)
            #print(f"Failed to send message to {contact}: {str(e)}")
