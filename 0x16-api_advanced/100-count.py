iimport requests
from collections import Counter

def count_words(subreddit, word_list, after=None, word_counter=None):
    # Base case: if word_counter is None, initialize it as a Counter
    if word_counter is None:
        word_counter = Counter()

    # Reddit API URL for getting hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"

    # Set a custom User-Agent to avoid potential issues with API requests
    headers = {"User-Agent": "Perfect123pct"}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract titles of hot posts and update word_counter
            for post in data["data"]["children"]:
                title = post["data"]["title"].lower()
                for word in word_list:
                    if word.lower() in title:
                        word_counter[word.lower()] += title.count(word.lower())

            # Check for pagination, if there are more posts
            after = data["data"]["after"]
            if after:
                # Recursive call with the updated parameters
                return count_words(subreddit, word_list, after, word_counter)
            else:
                # Base case: print the sorted results when no more posts
                sorted_results = sorted(word_counter.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_results:
                    print(f"{word}: {count}")
                return

        elif response.status_code == 404:
            # If the subreddit is not found, print nothing
            return
        else:
            # Handle other errors
            response.raise_for_status()

    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        print(f"Error: {e}")
        return

# Example usage:
subreddit_name = "python"
keywords = ["python", "java", "javascript"]

print(f"Keyword counts in '{subreddit_name}':")
count_words(subreddit_name, keywords)
