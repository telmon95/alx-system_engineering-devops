#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests

def recurse(subreddit, hot_list=None, after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return None

        results = response.json().get("data", {})
        after = results.get("after")
        count += results.get("dist", 0)
        for c in results.get("children", []):
            hot_list.append(c.get("data", {}).get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list

    except requests.RequestException:
        return None
