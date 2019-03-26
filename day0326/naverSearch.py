import requests
from urllib.parse import urlparse

keyword = "강남역"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword+"&display=100"
headers = {"X-Naver-Client-Id":"vcueUBX5ehY9HWHNfyhd","X-Naver-Client-Secret":"FDog2u7l6_"}
result = requests.get(urlparse(url).geturl(),headers=headers)
json_obj = result.json()
# for item in json_obj['items']:
#    print(item['title'].replace("<b>","").replace("</b>",""),item['link'])
print(len(json_obj['items']))

