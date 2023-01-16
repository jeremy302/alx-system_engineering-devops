#!/usr/bin/python3
''' uses api '''
import json
import sys
import urllib.request

if __name__ == '__main__':
    id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'

    with urllib.request.urlopen(f"{base_url}/users/{id}") as res:
        user = json.load(res)
        user_id = user['id']
    with urllib.request.urlopen(f"{base_url}/todos?userId={user_id}") as res:
        todos = json.load(res)

    arr = []
    for t in todos:
        arr.append({'task': t['title'],
                    'completed': t['completed'],
                    'username': user['username']})
    data = {str(user_id): arr}
    with open('{}.json'.format(user_id), 'w') as file:
        json.dump(data, file)
