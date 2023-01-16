#!/usr/bin/python3
'''uses api froom jsonplaceholder
'''
import json
import sys
import urllib.request


base_url = 'https://jsonplaceholder.typicode.com'
''' base url '''


if __name__ == '__main__':
    id = sys.argv[1]

    with urllib.request.urlopen(f"{base_url}/users/{id}") as res:
        user = json.load(res)
        user_id = user.get('id')
    with urllib.request.urlopen(f"{base_url}/todos?userId={user_id}") as res:
        todos = json.load(res)
        todos_done = len([t for t in todos if t.get('completed')])

    print("Employee {} is done with tasks({}/{})".format(
        user.get('name'), todos_done, len(todos)))
    for t in todos:
        print('\t {}'.format(t.get('title')))
