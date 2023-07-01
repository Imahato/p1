from selenium import webdriver as wd 
from selenium.webdriver.common.keys import Keys as ky
import pyautogui as pyt
import time


url_1 = "https://in.linkedin.com/home" 
    # url of network page of linkedin.com   
network_url1 = "http:/linkedin.com/my_network/"   
    # path for browser web driver  
driver_1 = wd.Chrome(executable_path= r"C:\Users\Shreya\Downloads\chromedriver_win32 (1)\chromedriver.exe")
driver_1.get(url_1)
time.sleep(3)
