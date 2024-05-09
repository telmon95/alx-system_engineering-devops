import requests


def recurse(subreddit, hot_list=[]):
    """Recursively retrieves titles of hot articles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    params = {'limit': 100}
    if len(hot_list) > 0:
        params['after'] = hot_list[-1]['data']['name']

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        if children:
            hot_list.extend(children)
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None


# Test the function
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
