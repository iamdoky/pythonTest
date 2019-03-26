# import os
# import sys
# import urllib.request

# keyword = '타이레놀'
# encText = urllib.parse.quote(keyword)
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     r = response_body.decode('utf-8')
#     print(r)
# else:
#     print("Error Code:" + rescode)
import func
keyword = '강남역'
r = func.naverSearch(keyword)
print(r)
