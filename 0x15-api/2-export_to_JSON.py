#!/usr/bin/python3
''' uses api '''
import json
import requests
import sys


if __name__ == '__main__':
    id = int(sys.argv[1])
    base_url = 'https://jsonplaceholder.typicode.com'

    user = requests.get("{}/users/{}".format(base_url, id)).json()
    todos = requests.get("{}/todos".format(base_url)).json()
    todos = [t for t in todos if t.get('userId') == id]
    arr = []
    for t in todos:
        arr.append({'task': t['title'],
                    'completed': t['completed'],
                    'username': user['username']})
    data = {str(id): arr}
    with open('{}.json'.format(id), 'w') as file:
        json.dump(data, file)
