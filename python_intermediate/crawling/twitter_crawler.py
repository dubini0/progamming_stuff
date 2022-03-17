# export PATH=$PATH:/home/dubini0/Desktop/crawler
import csv
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

KEYWORDS = ['keyword', 'you', 'want', 'to', 'search']

my_username = 'sampleusername'  # change username
my_password = 'samplepassword'  # change password

def login_twitter(my_username, my_password):
    driver = webdriver.Firefox(executable_path=r'/home/dubini0/Desktop/crawler/geckodriver')    # change to where to your geckodriver path
    driver.get('https://twitter.com')
    driver.implicitly_wait(3)

    sign_in = driver.find_element(By.XPATH, '//div/div/div/div[2]/main/div/div/div/div/div/div[3]/div[5]/a')
    sign_in.click()

    # Login to Twitter
    username = driver.find_element(By.XPATH, "//input[@autocomplete='username']")
    username.send_keys(my_username)

    next_btn = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div')
    next_btn.click()

    driver.implicitly_wait(3)
    password = driver.find_element(By.XPATH, "//input[@autocomplete='current-password']")
    password.send_keys(my_password)

    login_btn = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
    login_btn.click()
    return driver

def get_twitter_data(card, keyword):
    username = card.find_element(By.XPATH, './/span').text                                      # username
    twitter_id = card.find_element(By.XPATH, './/a/div/div[2]/div/span').text                   # twitter id
    content = card.find_element(By.XPATH, './/div[2]/div[2]/div[2]').text                       # tweet content
    url = card.find_element(By.XPATH, './/div[2]/div/div/div/div/a').get_attribute('href')      # url
    
    #print("URL: " + url)
    tweet = (username, twitter_id, content, keyword, url)
    return tweet

# for hashtags, it should search by top/latest
# for normal string, it should search by people
def search_by_latest(driver, keyword):
    search_input = driver.find_element(By.XPATH, '//input[@aria-label="Search query"]')
    search_input.clear()
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.RETURN)
    driver.find_element(By.LINK_TEXT, 'Latest').click()
    
    # collect tweets
    last_position = driver.execute_script("return window.pageYOffset;")
    tweet_ids = set()
    tweet_data = []
    scrolling = True

    while scrolling:
        cards = driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')
        for card in cards[-5:]:
            try:
                data = get_twitter_data(card, twitter_id)
            except:
                break
            if data:
                tweet_id = ''.join(data)
                if tweet_id not in tweet_ids:
                    tweet_ids.add(tweet_id)
                    tweet_data.append(data)

        scroll_attempt = 0
        while True:
            #check scroll position
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            driver.implicitly_wait(2)
            curr_position = driver.execute_script("return window.pageYOffset;")
            if last_position == curr_position:
                scroll_attempt += 1
                if scroll_attempt >= 3:
                    scrolling = False
                    break
                else:
                    driver.implicitly_wait(2)
            else:
                last_position = curr_position
                break

    print(f"[*] total crawled: {len(tweet_data)}")
    return tweet_data

def get_all_tweets(driver, twitter_id):
    driver.get('https://twitter.com/'+str(twitter_id))

    # collect tweets
    last_position = driver.execute_script("return window.pageYOffset;")
    tweet_ids = set()
    tweet_data = []
    scrolling = True

    while scrolling:
        cards = driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')
        for card in cards[-5:]:
            try:
                data = get_twitter_data(card, twitter_id)
            except:
                break
            time.sleep(2)
            if data:
                tweet_id = ''.join(data)
                if tweet_id not in tweet_ids:
                    tweet_ids.add(tweet_id)
                    tweet_data.append(data)

        scroll_attempt = 0
        while True:
            #check scroll position
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            driver.implicitly_wait(2)
            curr_position = driver.execute_script("return window.pageYOffset;")
            if last_position == curr_position:
                scroll_attempt += 1
                if scroll_attempt >= 3:
                    scrolling = False
                    break
                else:
                    driver.implicitly_wait(2)
            else:
                last_position = curr_position
                break

    print(f"[*] total crawled: {len(tweet_data)}", end='')
    return tweet_data

def tweet_to_csv(tweet_data):
    with open('result.csv', 'a+', newline='', encoding='utf-8') as f:
        #header = ['Username', 'id', 'Content', 'search keyword', 'URL']
        writer = csv.writer(f)
        #writer.writerow(header)
        writer.writerow('')
        writer.writerows(tweet_data)

if __name__ == "__main__":
    driver = login_twitter(my_username, my_password)
    with open('username.txt') as file:
        for twitter_id in file:
            print("[*] crawling from account: "+twitter_id)
            tweets = get_all_tweets(driver, twitter_id)
            #print(tweets)
            tweet_to_csv(tweets)
