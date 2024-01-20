import requests

def top_ten(subreddit):
    # Reddit API URL for getting hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set a custom User-Agent to avoid potential issues with API requests
    headers = {"User-Agent": "Perfect123pct"}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract and print titles of the first 10 hot posts
            for post in data["data"]["children"]:
                print(post["data"]["title"])

        elif response.status_code == 404:
            # If the subreddit is not found, print None
            print(None)
        else:
            # Handle other errors
            response.raise_for_status()

    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        print(f"Error: {e}")
        print(None)

# Example usage:
subreddit_name = "python"
print(f"Top 10 hot posts in '{subreddit_name}':")
top_ten(subreddit_name)
