#!/usr/bin/python3
''' uses api '''
import sys
import requests


if __name__ == '__main__':
    id = int(sys.argv[1])
    base_url = 'https://jsonplaceholder.typicode.com'

    user = requests.get("{}/users/{}".format(base_url, id)).json()
    todos = requests.get("{}/todos".format(base_url)).json()
    todos = [t for t in todos if t.get('userId') == id]

    csv = ''
    for t in todos:
        csv += '"{}","{}","{}","{}"\n'.format(
            id, user.get('username'), t.get('completed'), t.get('title'))
    with open('{}.csv'.format(id), 'w') as file:
        file.write(csv)
