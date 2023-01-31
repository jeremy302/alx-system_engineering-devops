#!/usr/bin/python3
'''<TODO> documentation'''
import requests


def recurse(subreddit, hot_list=[], n=0, after=None):
    '''<TODO> documentation'''
    res = requests.get(
        'https://www.reddit.com/r/{}/.json'.format(subreddit),
        params={'sort': 'hot', 'limit': 30, 'count': n, 'after': after or '0'},
        headers={'User-Agent': (
                           'Mozilla/5.0 (X11; Linux x86_64;' +
                           ' rv:109.0) Gecko/20100101 Firefox/109.0')},
        allow_redirects=False)
    if res.status_code == 200:
        res = res.json()
        posts = res['data']['children']
        hot_list.extend(post['data']['title'] for post in posts)
        if len(posts) >= 30 and res['data']['after']:
            return recurse(subreddit, hot_list, n + len(posts),
                           res['data']['after'])
    return hot_list or None
