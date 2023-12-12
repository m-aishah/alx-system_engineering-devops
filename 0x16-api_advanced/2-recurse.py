#!/usr/bin/python3
'''
Queries the Reddit API and returns a list of all hot post on a given subreddit.
'''

import requests


def recurse(subreddit, hot_list=[], count=0, after=''):
    '''Returns a list of titles of all hot post on a given subreddit.

    Args:
        subreddit (str): The subreddit in question.
        hot_list (list): The list of titles of hot post gotten thus far.
        count (int): The parameter of results matched thus far.
        after (str): Th eparame

    Returns: A list of all hot posts.
    '''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyRedditApp/1.0'}
    params = {
            'after': after,
            'count': count,
            'limit': 100
        }
    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )
    if response.status_code == 404:
        return None

    data = response.json().get('data')
    after = data.get('after')
    count += data.get('dist')

    for title in data.get('children'):
        hot_list.append(title.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, count, after)
    return hot_list
