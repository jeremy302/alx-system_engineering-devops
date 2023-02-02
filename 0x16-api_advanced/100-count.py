#!/usr/bin/python3
'''<TODO> documentation'''
import requests


def count_words(subreddit, word_list, tally=None, n=0, after=None):
    '''<TODO> documentation'''

    if tally is None:
        word_list = list(set(map(lambda w: w.lower(), word_list)))
        tally = list(map(lambda w: [w.lower(), 0], word_list))
        tally = count_words(subreddit, word_list, tally, 0, None)
        tally = list(filter(lambda v: v[0] and v[1], tally))
        tally.sort(key=lambda v: (-v[1], v[0]))
        list(map(lambda v: print('{}: {}'.format(v[0], v[1])), tally))
        return
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
        titles = list(map(lambda p: p['data']['title'].lower().split(),
                          posts))
        tally = list(map(lambda t: [
            t[0],
            t[1] + sum(map(lambda title: title.count(t[0]), titles))
        ], tally))
        if len(posts) >= 30 and res['data']['after']:
            return count_words(subreddit, word_list, tally, n + len(posts),
                               res['data']['after'])
    return tally
