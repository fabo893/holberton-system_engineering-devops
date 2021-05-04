#!/usr/bin/python3
"""
    Gather data from an API
"""


import requests
from sys import argv


if __name__ == "__main__":
    u = requests.get('https://jsonplaceholder.typicode.com/users')
    d1 = u.json()
    td = requests.get('https://jsonplaceholder.typicode.com/todos')
    d2 = td.json()

    arg = int(argv[1]) - 1

    ul = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                      .format(arg + 1))
    d3 = ul.json()

    EMPLOYEE_NAME = d1[arg]['name']
    empid = d1[arg]['id']

    total_res = 0
    for i in d2:
        if i['userId'] == empid:
            total_res = total_res + 1

    TOTAL_NUMBER_OF_TASKS = total_res

    done = 0
    for i in d2:
        if i['userId'] == empid and i['completed'] is True:
            done = done + 1

    NUMBER_OF_DONE_TASKS = done

    e = EMPLOYEE_NAME
    n = NUMBER_OF_DONE_TASKS
    t = TOTAL_NUMBER_OF_TASKS

    lis = []
    for l in d3:
        for k, v in l.items():
            if k == 'completed' and v is True:
                lis.append(l.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(e, n, t))
    print("\n".join("\t {}".format(title) for title in lis))
