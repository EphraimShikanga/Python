# This Whatsapp Spam Bot was made for educational purposes, and this publicly available Python script
# was made to aid the tutorial that was made for it on YouTube.

# Importing modules/libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setting some parameters for when the actual spamming happens
message = "" # Message to spam
amount = 20 # Amound of times message should get spammed
delay = 0.2 # Delay in seconds between each message sent (to be safe, don't make this lower than 0.2)
contact = "" # Contact to spam - this is the contact's exact name

# Creating Chrome WebDriver - this represents an instance of Chrome
options = webdriver.ChromeOptions() # ChromeOptions instance
options.add_argument('user-data-dir=C:\\ChromeProfile') # Adding argument to options - this option will make us use
                                                          # newly made Chrome Profile
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=options) # Creating the actual driver instance
driver.get('https://web.whatsapp.com/') # Opening whatsapp web on chrome instance
# driver.minimize_window() # minimizing window to not disturb user

# Delay to allow time for Whatsapp to open
time.sleep(20)

# Name list will contain most recent contact names (in order) - this will be used when choosing the contact to spam
name_list = []

# //*[@id="pane-side"]/div[1]/div/div/div[1]
# //*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/span 

# Obtaining most recent contact names and storing the names in name_list (in order)
for i in range(1, 15):
    info = driver.find_element_by_xpath(f'//*[@id="pane-side"]/div[1]/div/div/div[{i}]' + '/div/div/div/div[2]/div[1]/div[1]/span')
    name_list.append(info.text)

# Obtaining index of contact to spam
to_click = name_list.index(contact) + 1

# Finding contact on whatsapp web and clicking on them
driver.find_element_by_xpath(f'//*[@id="pane-side"]/div[1]/div/div/div[{to_click}]').click()

# Extra Delay (just in-case)
time.sleep(5)

# For loop that will spam messages to contact
# wait = WebDriverWait(driver, 10)
for i in range(amount):
    # Searching for text box
    text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    # text_box = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
    text_box.send_keys(message) # Typing message to text box
    text_box.send_keys(Keys.ENTER) # Pressing enter to send message
    time.sleep(delay) # Adding delay between messages