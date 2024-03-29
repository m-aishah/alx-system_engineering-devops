# 0x16. API advanced


## Overview

This project is a programming assignment focused on utilizing Python for working with APIs, specifically the Reddit API. The project aims to enhance the developer's skills in reading API documentation, handling pagination, parsing JSON responses, making recursive API calls, and sorting dictionaries. The tasks involve creating Python functions to interact with the Reddit API, such as retrieving the number of subscribers for a given subreddit, printing the titles of the top 10 posts in a subreddit, and recursively fetching all hot articles for a given subreddit. The project provides specific requirements for coding style, organization, and the use of the Requests module. The tasks are designed to reinforce fundamental concepts related to API usage and prepare the developer for potential interview questions. 


## Tasks

<b>0.How many subs?</b>

- Description: Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

- File: [0-subs.py](./0-subs.py)


<b>1.Top Ten</b>

- Description: Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

- File: [1-top_ten.py](./1-top_ten.py)


<b>2. Recurse it!</b>

- Description: Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

- File: [2-recurse.py](./2-recurse.py)

<b>3.Count it!</b>

- Description: Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).

- File: [100-count.py](./100-count.py)
