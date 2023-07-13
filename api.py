import requests

API_KEY = "krZH4Yv0npRF1XFqi87BGod4BM2fyLPK"
endpoint = "https://api.griphy.com/v1/gifs/trending"

params = {"api_key": API_KEY, "limit": 6, "rating": "g"}
response = requests.get(endpoint, params=params).json()
for gif in response["data"]:
    title = gif["title"]
    trending_date = gif["trending_datetime"]
    url = gif["url"]
    print(f"{title} | {trending_date} | {url}")