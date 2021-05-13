from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from decouple import config


amount = int(config("TOTAL_QTN"))

def start_session(email, password):
    print(f"Bypassing Account No {i}")
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.awseducate.com/signin/SiteLogin?ec=302")
    login_email = driver.find_element_by_id('loginPage:siteLogin:loginComponent:loginForm:username')
    login_password = driver.find_element_by_id('loginPage:siteLogin:loginComponent:loginForm:password')
    login_email.send_keys(email)
    login_password.send_keys(password)
    login_button = driver.find_element_by_class_name('loginText')
    login_button.click()
    sleep(3)
    driver.get("https://www.awseducate.com/student/s/launch-starter")
    sleep(8)
    get_details_button = driver.find_element_by_id("showawsdetail")
    get_details_button.click()
    if get_details_button:
        print(f"Bypassed Account No . {i}")
    else:
        print(f"Failed To Bypass Account No {i} , {email}:{password}")
    driver.close()

for i in range(1,amount+1):
    acc = (config(f"ACC_NO_{i}")).split(":")
    email = acc[0]
    password = acc[1]
    start_session(email, password)