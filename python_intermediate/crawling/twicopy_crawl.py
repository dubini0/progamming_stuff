import requests
import csv
import time

def tweet_to_csv(tweet_data):
    with open(f'result_{time.time()}.csv', 'a+', newline='', encoding='utf-8') as f:
        #header = ['Username', 'id', 'Content', 'search keyword', 'URL']
        writer = csv.writer(f)
        #writer.writerow(header)
        writer.writerow('')
        writer.writerows(tweet_data)

if __name__ =="__main__":
    tw_list = []
    with open('twitter_usernames.txt') as file:
        for twitter_id in file:
            print("[*] crawling from account: "+twitter_id, end='')
            url = f'https://twicopy.com/{twitter_id.strip()}/'
            res = requests.get(url)
            if res.status_code == 200:
                tw_list.append([url, twitter_id.strip()])
            
    print(tw_list)
    tweet_to_csv(tw_list)
