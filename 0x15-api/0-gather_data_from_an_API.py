#!/usr/bin/python3
'''uses api froom jsonplaceholder
'''
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        id = int(sys.argv[1])
        base_url = 'https://jsonplaceholder.typicode.com'

        user = requests.get("{}/users/{}".format(base_url, id)).json()

        todos = requests.get("{}/todos".format(base_url)).json()
        todos = [t for t in todos if t.get('userId') == id]
        todos_done = [t for t in todos if t.get('completed')]
        print("Employee {} is done with tasks({}/{}):".format(
            user.get('name'), len(todos_done), len(todos)))
        for t in todos_done:
            print('\t {}'.format(t.get('title')))
