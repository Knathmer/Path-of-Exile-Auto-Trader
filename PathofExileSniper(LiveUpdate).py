#------------Prerequisites------------#
# To use this script, you must have/do the following:
# 1. All of the modules installed.
# 2. In the initialization section, you must change the path to your chrome profile. Simply replace the name of the profile with your profile name.
# 3. In the initialization section, you must change the path to your chromedriver.exe. Simply replace the path with the path to your chromedriver.exe. I recommend putting it in the same folder as this script.
# 4. Set your threshold prices for chaos, divine, and mirror orbs.
# 5. Chrome must be closed before running the script.
# 6. Before closing out of chrome, you must copy the link to the live update page. This can be done by clicking the "Live Update" button on the trade site. Keep it on your clipboard.
# 7. You must have a default profile in chrome. This is the profile that will be used to run the script.
# 8. Path of Exile must be running.

#------------Use------------#
# To use this script, run it. Once it starts you will see a Chrome page to select your default profile. You want to select the profile that contains your Path of Exile login information.
# If you are unable to select your profile, you may need to change the ENTIRE path to your --profile-directory in the initialization section. Locate the folder of your default profile and copy the ENTIRE path.
# Once you have selected your profile, click on the URL bar and paste the link to the live update page. Then press enter.
# The script will now run. You can minimize the chrome window and it will continue to run in the background. If you want to stop the script, simply close the chrome window.
# If you want to change the threshold prices, you can do so in the initialization section. You will have to restart the script for the changes to take effect.

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
options.add_argument(r"--user-data-dir=C:\Users\(replace this with your username)\AppData\Local\Google\Chrome\User Data") #Path to your Chrome profile
options.add_argument(r'--profile-directory=C:\Users\(replace this with your username)\AppData\Local\Google\Chrome\User Data\Profile 2') #Keep Profile 2 as your default profile
driver = webdriver.Chrome(executable_path=r'C:/Program Files (x86)\chromedriver.exe', chrome_options=options) #Path to your chromedriver.exe

url = 'https://www.google.co.in' # This needs to be set to Google so that the script can import your default profile to bypass Cloudflare bot protection.

#------------Conditions------------#

chaoslimit = 10 # Set the price threshold for chaos orbs
divinelimit = 100 # Set the price threshold divine orbs
mirrorlimit = 1.5 # Set the price threshold for mirrors

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

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'results'))) # Waits for the results to load

while loop == True:
    
    time.sleep(1)
    
    items =  driver.find_elements(By.XPATH,'//div[@class="resultset"]/div[@class="row" or @class="row gone"]')
    
    if length != 0:
        items = items[:-length]
    
    for item in items:
        length += 1
        print("test")
        
        print('----------------------------------------------------------------')
        
        try: # Tries to find the location of price in the main box
        
            price = item.find_element(By.CLASS_NAME,'textCurrency')
            listdate = item.find_element(By.CLASS_NAME,'info')

            if 'chaos' in price.text:
                amount = float(price.text.split(' ')[1]) # Splits the string to pull out the float cost
                if amount < chaoslimit: # If within price range
                    print(str(amount)+' CHAOS \n'+listdate.text+'\n') # String formatting of the cost and date listed
                    send()
                    
            if 'divine' in price.text:
                amount = float(price.text.split(' ')[1])
                if amount < divinelimit:
                    print(str(amount)+' DIVINE(s) \n'+listdate.text+'\n')
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
                        
            if 'Divine Orb' in price.text:
                amount = float(price.text.split('\n')[1].split('×Divine Orb')[0])
                if amount < divinelimit:
                    print(str(amount)+' DIVINES(s) \n'+listdate.text+'\n')
                    send()
                    
            if 'Mirror of Kalandra' in price.text:
                amount = float(price.text.split('\n')[1].split('×Mirror of Kalandra')[0])
                if amount < mirrorlimit:
                    print(str(amount)+' MIRROR(s) \n'+listdate.text+'\n')
                    send()
                    
                    
