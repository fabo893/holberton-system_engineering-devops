#!/usr/bin/python3
"""
0-subs
"""


import json
import requests


def number_of_subscribers(subreddit):
    """ Query for number of subcribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'Fabo win'}
    response = requests.get(url, headers=header)
    try:
        if response.status_code != 200:
            return 0
        return response.json()['data']['subscribers']
    except:
        return 0
