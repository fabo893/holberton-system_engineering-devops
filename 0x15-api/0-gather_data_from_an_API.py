#!/usr/bin/python3
"""
    Gather data from an API
"""


import requests
import sys


if __name__ == "__main__":
    u = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    d1 = u.json()
    td = requests.get('https://jsonplaceholder.typicode.com/todos')
    d2 = td.json()

    EMPLOYEE_NAME = d1['name']
    empid = d1['id']

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

    print("Employee {} is done with tasks({}/{}):".format(e, n, t))
    for i in d2:
        if i['userId'] == empid and i['completed'] is True:
            title = i['title']
            print("\t {}".format(title))
