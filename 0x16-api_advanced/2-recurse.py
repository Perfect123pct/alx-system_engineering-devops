import requests

def recurse(subreddit, hot_list=None, after=None):
    # Base case: if hot_list is None, initialize it as an empty list
    if hot_list is None:
        hot_list = []

    # Reddit API URL for getting hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    
    # Set a custom User-Agent to avoid potential issues with API requests
    headers = {"User-Agent": "Your-App-Name"}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract titles of hot posts and add them to the hot_list
            for post in data["data"]["children"]:
                hot_list.append(post["data"]["title"])

            # Check for pagination, if there are more posts
            after = data["data"]["after"]
            if after:
                # Recursive call with the updated hot_list and after parameter
                return recurse(subreddit, hot_list, after)
            else:
                # Base case: return the final hot_list when no more posts
                return hot_list

        elif response.status_code == 404:
            # If the subreddit is not found, return None
            return None
        else:
            # Handle other errors
            response.raise_for_status()

    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        print(f"Error: {e}")
        return None

# Example usage:
subreddit_name = "python"
result = recurse(subreddit_name)

if result is not None:
    print(f"All hot article titles in '{subreddit_name}':")
    for title in result:
        print(title)
else:
    print(f"The subreddit '{subreddit_name}' is not valid or no results found.")
