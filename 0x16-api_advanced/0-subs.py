#!/usr/bin/python3
'''<TODO> documentation'''
import requests


def number_of_subscribers(subreddit):
    '''<TODO> documentation'''
    res = requests.get(
        'https://www.reddit.com/r/{}/about/.json'.format(
            subreddit), allow_redirects=False,
        headers={
            'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64;' +
                           ' rv:109.0) Gecko/20100101 Firefox/109.0')
        })
    return res.json()['data']['subscribers'] if res.status_code == 200 else 0
