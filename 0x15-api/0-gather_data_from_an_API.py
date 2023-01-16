#!/usr/bin/python3
'''uses api froom jsonplaceholder
'''
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        id = sys.argv[1]
        base_url = 'https://jsonplaceholder.typicode.com'

        user = requests.get("{}/users/{}".format(base_url, id)).json()
        user_id = user.get('id')

        todos = requests.get("{}/todos?userId={}".format(
            base_url, user_id)).json()
        todos_done = len([t for t in todos if t.get('completed')])
        print("Employee {} is done with tasks({}/{})".format(
            user.get('name'), todos_done, len(todos)))
        for t in todos:
            if t.get('completed'):
                print('\t {}'.format(t.get('title')))
