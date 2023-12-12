#!/usr/bin/python3
'''
Queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
'''
import requests


def top_ten(subreddit):
    ''' Prints the title of the top 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit in question.
    '''

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 10}
    headers = {'User-Agent': 'MyRedditApp/1.0'}
    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )

    if response.status_code == 404:
        print(None)
        return

    posts = response.json().get('data')
    [print(post.get('data').get('title')) for post in posts.get('children')]
