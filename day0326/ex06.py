import requests
from urllib.parse import urlparse

keyword = "강남역"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword
headers = {"X-Naver-Client-Id":"vcueUBX5ehY9HWHNfyhd","X-Naver-Client-Secret":"FDog2u7l6_"}
result = requests.get(urlparse(url).geturl(),headers=headers)
json_obj = result.json()
print(json_obj['lastBuildDate'])
print(json_obj['total'])
print(json_obj['start'])
print(json_obj['display'])
print(json_obj['items'])



