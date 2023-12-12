#!/usr/bin/python3
'''Queries the Reddit Api and returns the number of subscribers.'''

import requests

def number_of_subscribers(subreddit):
    '''Returns the total number of subscribers for a given subreddit.

    subreddit (str): The given subreddit.

    Returns: The total number of subscribers.
    '''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    # Setting a custom User-Agent
    headers = { 'User-Agent': 'MyRedditApp/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    subscribers = response.json().get('data').get('subscribers')
    return subscribers
