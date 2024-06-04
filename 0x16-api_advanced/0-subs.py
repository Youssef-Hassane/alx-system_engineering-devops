#!/usr/bin/python3
"""
the number of subscribers (not active users, total subscribers)
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        GET /r/subreddit/aboutread
            Return information about the subreddit.
            Data includes the subscriber count, description, and header image.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
