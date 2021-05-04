#!/usr/bin/python3
"""
    Gather data from an API
"""

import requests
from sys import argv
import csv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    u_id = int(argv[1])
    u_p = requests.get(url + '/users/{}'.format(u_id)).json()
    u_td = requests.get(url + '/todos?userId={}'.format(u_id)).json()

    u_name = u_p.get('name')
    td_total = len(u_td)
    td_title = []
    row = []

    for x in u_td:
        r = [u_id, u_p.get('username'), x.get('completed'), x.get('title')]
        row.append(r)

    with open("{}.csv".format(u_id), 'w') as f:
        writer = csv.writer(f)
        writer.writerows(row)
    f.close()
