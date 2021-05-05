#!/usr/bin/python3
"""
    Gather data from an API
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    u_id = int(argv[1])
    u_p = requests.get(url + '/users/{}'.format(u_id)).json()
    u_td = requests.get(url + '/todos?userId={}'.format(u_id)).json()
    u_tasks = []

    for x in u_td:
        dicUser = {}
        dicUser["task"] = x.get('title')
        dicUser["completed"] = x.get('completed')
        dicUser["username"] = u_p.get('username')

        u_tasks.append(dicUser)

    u_json = {}
    u_json[u_id] = u_tasks

    with open("{}.json".format(u_id), 'w') as f:
        json.dump(u_json, f)
    f.close()
