#!/usr/bin/python3
'''uses api froom jsonplaceholder
'''
import json
import sys
import urllib.request


if __name__ == '__main__':
    id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'
    with urllib.request.urlopen("{base_url}/users/{id}") as res:
         user = json.load(res)
