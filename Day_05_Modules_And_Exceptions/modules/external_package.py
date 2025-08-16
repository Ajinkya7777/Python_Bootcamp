# external_package.py

import requests

def fetch_data_from_url(url):
    """
    Fetch data from a URL using the requests library and return the status code and content.
    """
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.text[:200]}...")  # Displaying the first 200 characters
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")

# Notes:
# 1. The `requests.get()` method sends an HTTP GET request to the given URL.
# 2. We handle any possible network errors using `requests.exceptions.RequestException`.
# 3. The `response.status_code` and `response.text` provide the status and content of the HTTP response.
# 4. The `requests` package is a popular library for making HTTP requests in Python.
