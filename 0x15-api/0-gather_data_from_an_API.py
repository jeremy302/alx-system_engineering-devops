#!/usr/bin/python3
'''uses api froom jsonplaceholder
'''
import json
import sys
import urllib.request


if __name__ == '__main__':
    id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'

    print("Employee {} is done with tasks({}/{})".format(
        user.get('name'), todos_done, len(todos)))
    for t in todos:
        print('\t {}'.format(t.get('title')))
