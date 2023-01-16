#!/usr/bin/python3
''' uses api '''
import sys
import urllib.request
import json

if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com'

    with urllib.request.urlopen(f"{base_url}/users") as res:
        users = json.load(res)
    with urllib.request.urlopen(f"{base_url}/todos") as res:
        todos = json.load(res)

    data = {}

    for user in users:
        user_id = user['id']
        tasks = [t for t in todos if t['userId'] == user_id]
        arr = []
        for t in tasks:
            arr.append({'username': user['username'],
                        'task': t['title'],
                        'completed': t['completed']})
        data[str(user_id)] = arr
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
