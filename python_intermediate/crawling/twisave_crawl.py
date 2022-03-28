import requests
import csv
import time
import re

def tweet_to_csv(tweet_data):
    with open(f'twisave_result_{time.time()}.csv', 'a+', newline='', encoding='utf-8') as f:
        #header = ['URL', 'id', 'Content']
        writer = csv.writer(f)
        #writer.writerow(header)
        writer.writerow('')
        writer.writerows(tweet_data)

if __name__ =="__main__":
    tw_list = []
    with open('twitter_usernames.txt') as file:
        for twitter_id in file:
            print("[*] crawling from account: "+twitter_id, end='')
            url = f'https://www.twisave.com/{twitter_id.strip()}/'
            res = requests.get(url)

            # if valid account, crawl all tweets
            if "404" != res.text:
                tw_list.append([url, twitter_id.strip()])
                try:
                    tweet_text = twitter_id.strip()+r"/tweet/\d+"
                    found = re.findall(tweet_text, res.text)
                except AttributeError:
                    found = ""
                    print("[!] no tweet found")
                for tweets in found:
                    tweet_url = 'https://www.twisave.com/'+tweets
                    #print(tweet_url)
                    tw_list.append([tweet_url, twitter_id.strip()])
            
    print(tw_list)
    tweet_to_csv(tw_list)
