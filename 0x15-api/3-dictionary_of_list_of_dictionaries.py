#!/usr/bin/python3
"""
    Gather data from an API
"""

import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    u_p = requests.get(url + '/users').json()
    u_json = {}

    for u in u_p:
        u_id = u.get('id')
        u_td = requests.get(url + '/todos?userId={}'.format(u_id)).json()
        u_tasks = []

        for x in u_td:
            dicUser = {}
            dicUser["task"] = x.get('title')
            dicUser["completed"] = x.get('completed')
            dicUser["username"] = u.get('username')

            u_tasks.append(dicUser)

        u_json[u_id] = u_tasks

    with open("todo_all_employees.json".format(u_id), 'w') as f:
        json.dump(u_json, f)
    f.close()
