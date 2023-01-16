#!/usr/bin/python3
''' uses api '''
import sys
import urllib.request
import json

if __name__ == '__main__':
    id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'

    with urllib.request.urlopen(f"{base_url}/users/{id}") as res:
        user = json.load(res)
        user_id = user['id']
    with urllib.request.urlopen(f"{base_url}/todos?userId={user_id}") as res:
        todos = json.load(res)
        todos_done = len([t for t in todos if t.get('completed')])

    print("Employee {} is done with tasks({}/{})".format(
        user['name'], todos_done, len(todos)))
    for t in todos:
        print('\t {}'.format(t.get('title')))
