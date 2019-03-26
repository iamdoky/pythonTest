import requests
from urllib.parse import urlparse

def get_api_result(keyword,display,start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword+"&display="+ str(display)+"&start="+str(start)
    headers = {"X-Naver-Client-Id":"vcueUBX5ehY9HWHNfyhd","X-Naver-Client-Secret":"FDog2u7l6_"}
    result = requests.get(urlparse(url).geturl(),headers=headers)
    json_obj = result.json()
    return json_obj


keyword = '강남역'
display = 100
json_obj = get_api_result(keyword,display,101)
for item in json_obj['items']:
    print(item)