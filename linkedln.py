from selenium import webdriver as wd  
from selenium.webdriver.common.keys import Keys as ky  
import pyautogui as pyt  
def login_1():  
    # First, we will get the login element  
    username_1 = driver.find_element_by_id("login-email")    
    # then, we will send the keys for username_1       
    username_1.send_keys("username")         
    # now, send the password element in it                              
    password_1 = driver.find_element_by_id("login-password")   
    # then, send the keys for password_1     
    password_1.send_keys("password")                 
    # then, get the tag for submit button             
    driver.find_element_by_id("login-submit").click()  
def go_to_network():  
    driver.find_element_by_id("my_network-tab-icon").click()  
def send_requests_1():  
    # the Nnumber of requests we want to send  
    n_1 = input("The number of connection requests: ")     
  
    for k in range(0, n_1):  
        # position(in px) of connection button will be different for different user  
        pyt.click(810, 670)    
    print("All request are sent!")  
def main():  
    # url of LinkedIn,com  
    url_1 = "https://in.linkedin.com/home"    
    # url of network page of linkedin.com   
    network_url1 = "http:/linkedin.com/my_network/"   
    # path for browser web driver  
    driver_1 = wd.Chrome(executable_path= r"C:\Users\Shreya\Downloads\chromedriver_win32 (1)\chromedriver.exe")
    driver_1.get(url_1)  
  
# Drivers code  
if __name__ == __main__:  
    main()  