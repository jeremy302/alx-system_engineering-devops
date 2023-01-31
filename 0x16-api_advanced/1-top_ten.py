#!/usr/bin/python3
'''<TODO> documentation'''
import requests


def top_ten(subreddit):
    '''<TODO> documentation'''
    res = requests.get('https://www.reddit.com/r/{}/.json'.format(subreddit),
                       params={'sort': 'top', 'limit': 10},
                       headers={'User-Agent': (
                           'Mozilla/5.0 (X11; Linux x86_64;' +
                           ' rv:109.0) Gecko/20100101 Firefox/109.0')},
                       allow_redirects=False)

    if res.status_code == 200:
        for item in res.json()['data']['children']:
            print(item['data']['title'])
    else:
        print(None)
