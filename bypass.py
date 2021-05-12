from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from dotenv import dotenv_values as secret


env = secret('config.env')
amount = int(env['TOTAL_QTN'])


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
    sleep(4)
    show_details_button = driver.find_element_by_id("clikeyboxbtn")
    show_details_button.click()
    sleep(2)
    text_details = driver.find_element_by_id("clikeybox")
    to_parse_text = text_details.text
    to_parse_text = ((to_parse_text.strip("Copy and paste the following into ~/.aws/credentials")).split("\n[default]\n")[1]).split('\n')
    acc_key = (to_parse_text[0].split('='))[0] + '="' + (to_parse_text[0].split('='))[1]  + '"'
    sec_acc_key = (to_parse_text[1].split('='))[0] + '="' + (to_parse_text[1].split('='))[1]  + '"'
    sec_acc_token = (to_parse_text[2].split('='))[0] + '="' + (to_parse_text[2].split('='))[1]  + '"'
    to_print = acc_key + ',\n' + sec_acc_key + ',\n' + sec_acc_token + ',\n'
    #print(to_print)
    driver.close()

for i in range(1,amount+1):
    acc = (env[f"ACC_NO_{i}"]).split(":")
    email = acc[0]
    password = acc[1]
    start_session(email, password)    