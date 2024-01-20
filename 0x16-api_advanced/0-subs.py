import requests

def number_of_subscribers(subreddit):
    # Reddit API URL for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid potential issues with API requests
    headers = {"User-Agent": "Perfect123pct"}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract the number of subscribers from the response
            subscribers = data["data"]["subscribers"]
            
            return subscribers
        elif response.status_code == 404:
            # If the subreddit is not found, return 0
            return 0
        else:
            # Handle other errors
            response.raise_for_status()

    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        print(f"Error: {e}")
        return 0

# Example usage:
subreddit_name = "python"
subscribers_count = number_of_subscribers(subreddit_name)

if subscribers_count != 0:
    print(f"The subreddit '{subreddit_name}' has {subscribers_count} subscribers.")
else:
    print(f"The subreddit '{subreddit_name}' is not valid or not found.")
