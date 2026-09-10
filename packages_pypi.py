'''
import requests


response = requests.get("https://example.com")

print(response.status_code)
'''

import requests

url = "https://api.github.com/users/octocat"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"Username: {data['login']}")
    print(f"Public repos:{data['public_repos']}")
    print(f"Followers: {data['followers']}")
else:
    print(f"Request failed with status code: {response.status_code}")