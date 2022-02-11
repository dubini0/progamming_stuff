# export PATH=$PATH:/home/dubini0/Desktop/crawler
# This works in 2022.02.11 Twitter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

# Change info
my_username = 'sampleusername'  # change username
my_password = 'samplepassword'  # change password
gecko_path = r'/home/dubini0/Desktop/crawler/geckodriver'  # change driver path

def login_twitter(my_username, my_password):
    driver = webdriver.Firefox(executable_path=gecko_path)
    driver.get('https://twitter.com')
    driver.implicitly_wait(3)

    sign_in = driver.find_element(By.XPATH, '//div/div/div/div[2]/main/div/div/div/div/div/div[3]/div[5]/a')
    sign_in.click()

    # Login to Twitter
    username = driver.find_element(By.XPATH, "//input[@autocomplete='username']")
    username.send_keys(my_username)

    next_btn = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div')
    next_btn.click()

    driver.implicitly_wait(5)
    password = driver.find_element(By.XPATH, "//input[@autocomplete='current-password']")
    password.send_keys(my_password)

    login_btn = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
    login_btn.click()

if __name__ == "__main__":
    login_twitter(my_username, my_password)
