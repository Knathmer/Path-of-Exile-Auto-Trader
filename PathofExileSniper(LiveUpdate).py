#------------Initialization------------#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pygetwindow as gw
import pyperclip
from pynput.keyboard import Key, Controller
import time

loop = True
length = 0

win = gw.getWindowsWithTitle('Path of Exile')[0] # Sets win = to the path of exile window

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\Eraj\AppData\Local\Google\Chrome\User Data")
options.add_argument(r'--profile-directory=C:\Users\Eraj\AppData\Local\Google\Chrome\User Data\Profile 2')
driver = webdriver.Chrome(executable_path=r'C:/Program Files (x86)\chromedriver.exe', chrome_options=options)

url = 'https://www.google.co.in'

#------------Conditions------------#
chaoslimit = 10 # Set the max cost for chaos
exaltlimit = 100 # Set the max cost for exalts
mirrorlimit = 1.5 # Set the max cost for mirrors

#------------Functions------------#

def copy(): 
    button = item.find_element(By.CLASS_NAME,'whisper-btn')
    button.click()

def paste():
    s = pyperclip.paste()
    print(s+'\n')

def message(): # Simulates Control+V
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release(Key.ctrl)
    keyboard.release('v')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def send():
    copy()
    paste()
    win.activate()
    message()

#------------Main Program------------#
driver.get(url)

time.sleep(10)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'results')))

while loop == True:
    
    time.sleep(1)
    
    items =  driver.find_elements(By.XPATH,'//div[@class="resultset"]/div[@class="row" or @class="row gone"]')
    
    if length != 0:
        items = items[:-length]
    
    for item in items:
        length += 1
        
        print('----------------------------------------------------------------')
        
        
        try: # Tries to find the location of price in the main box
        
            price = item.find_element(By.CLASS_NAME,'textCurrency')
            listdate = item.find_element(By.CLASS_NAME,'info')

            if 'chaos' in price.text:
                amount = float(price.text.split(' ')[1]) # Splits the string to pull out the float cost
                if amount < chaoslimit: # If within price range
                    print(str(amount)+' CHAOS \n'+listdate.text+'\n') # String formatting of the cost and date listed
                    send()
                    
            if 'exalted' in price.text:
                amount = float(price.text.split(' ')[1])
                if amount < exaltlimit:
                    print(str(amount)+' EXALT(s) \n'+listdate.text+'\n')
                    send()
                    
            if 'mirror' in price.text:
                amount = float(price.text.split('\n')[1].split('×Mirror of Kalandra')[0])
                if amount < mirrorlimit:
                    print(str(amount)+'MIRROR(s) \n'+listdate.text+'\n')
                    send()
                     
                    
        except: # If the main box price doesn't exist, then it refers to the price on the side
        
            price = item.find_element(By.CLASS_NAME,'price')
            listdate = item.find_element(By.CLASS_NAME,'info')
            
            if 'Chaos Orb' in price.text:
                amount = float(price.text.split('\n')[1].split('×Chaos Orb')[0])
                if amount < chaoslimit:
                    print(str(amount)+' CHAOS \n'+listdate.text+'\n')
                    send()
                        
            if 'Exalted Orb' in price.text:
                amount = float(price.text.split('\n')[1].split('×Exalted Orb')[0])
                if amount < exaltlimit:
                    print(str(amount)+' EXALT(s) \n'+listdate.text+'\n')
                    send()
                    
            if 'Mirror of Kalandra' in price.text:
                amount = float(price.text.split('\n')[1].split('×Mirror of Kalandra')[0])
                if amount < mirrorlimit:
                    print(str(amount)+' MIRROR(s) \n'+listdate.text+'\n')
                    send()
                    
                    

