from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.file import read_file
from utils.whatsapp import send_message
import os

cwd = os.path.abspath(os.getcwd())

# Get messages
message = read_file(f"{cwd}/assets/message.txt")

# Get all contacts
contacts = read_file(f"{cwd}/assets/contacts.txt", array=True)

# Initialize Chrome Driver
s = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--user-data-dir=/tmp/chrome-data/" + "Selenium")
driver = webdriver.Chrome(options=chrome_options,service=s)

# Send WhatsApp Message
send_message(driver=driver, contacts=contacts, message=message)

