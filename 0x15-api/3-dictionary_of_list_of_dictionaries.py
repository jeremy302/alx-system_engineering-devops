#!/usr/bin/python3
''' uses api to get all users and tasks '''
import json
import requests


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com'

    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

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
