#!/usr/bin/python3
"""
    Gather data from an API
"""


import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    u_id = argv[1]
    u_p = requests.get(url + "/{}".format(u_id)).json()
    u_td = requests.get(url + "/{}/todos".format(u_id)).json()

    u_name = u_p.get('name')
    td_total = len(u_td)
    done = 0
    td_title = []

    for x in u_td:
        if x.get('completed'):
            done = done + 1
            td_title.append(x.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(u_name,
                                                          done,
                                                          td_total))
    print("\n".join("\t {}".format(title) for title in td_title))
