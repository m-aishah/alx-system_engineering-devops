#!/usr/bin/python3
'''
Queries the Reddit API,
extracts the titles of all hot articles,
and outputs a sorted count of specified keywords.
'''

import requests


def count_words(subreddit, word_list, w_count={}, count=0, after=''):
    '''Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit in question.
        word_list (list): The list of words to be searched for.
        w_count (obj): key/value apir of words and their counts.
        after (str): The parmeter for the next page of the API results.
        count (int): The parameter of results matched thus far.
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

    try:
        data = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    data = response.json()
    data = data.get("data")
    after = data.get("after")
    count += data.get("dist")
    for c in data.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()
                             or t == word])
                word_lower = word.lower()
                if w_count.get(word_lower) is None:
                    w_count[word_lower] = times
                else:
                    w_count[word_lower] += times

    if after is None:
        if len(w_count) == 0:
            print("")
            return
        w_count = sorted(w_count.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in w_count]
    else:
        count_words(subreddit, word_list, w_count, count, after)
