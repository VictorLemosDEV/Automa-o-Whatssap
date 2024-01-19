import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from threading import Thread

import time

canvas = None



def UpdateQrCode(driver):

    

    previousContainerData = ""

    
    

    def GetContainerAttributes():

        global canvas
        
        try:
            canvas = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div/div[2]/div'))
            return canvas.get_attribute('data-ref')
        
        except Exception as e:
            print(f"Something went wrong...")
            

        

    def CheckUpdate():
        currentData = GetContainerAttributes()

        if currentData != previousContainerData:
            print("Updated")
            GetQrCodeImage()

    def GetQrCodeImage():
        if canvas:
            canvas.screenshot("qr-code.png")

    # get the canvas as a PNG base64 string

    def CallFunctions():
        try:
            canvas = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[3]/div[1]/div/div/div[2]/div/canvas'))
            
        except Exception as e:
            print(f"Something went wrong...")


        CheckUpdate()
        time.sleep(20)

    CallFunctions()

def StartSearch():
    UpdateQrCode()
    

