#!/usr/bin/python3
''' uses api '''
import sys
import urllib.request
import json
import csv

if __name__ == '__main__':
    id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'

    with urllib.request.urlopen(f"{base_url}/users/{id}") as res:
        user = json.load(res)
        user_id = user['id']
    with urllib.request.urlopen(f"{base_url}/todos?userId={user_id}") as res:
        todos = json.load(res)

    rows = []
    for t in todos:
        rows.append([user_id,
                     user['username'],
                     t['completed'],
                     t['title']])
    with open('{}.csv'.format(user_id), 'w') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
