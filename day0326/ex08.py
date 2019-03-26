import requests
from bs4 import BeautifulSoup

endpoint = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?'
serviceKey = 'UoL8y2fnhJVqh9eHvIKkVzCNyD2IYj%2BJKaidjN3NMXyQjQhJ%2F72eQp1DaxdONF1T%2BPCAAm0hfB7ys%2FPhIcxnwQ%3D%3D'
numOfRows = "10"
pageSize = "1"
pageNo = "1"
MobileOS = "ETC"
MobileApp = "AppTest"
arrange = "A"
contentTypeId = "15"
areaCode = "1"
sigunguCode = "1"
listYN = "Y"
paramset = "serviceKey=" + serviceKey + "&numOfRows=" + numOfRows + "&pageSize=" + pageSize + "&pageNo=" + pageNo + "&MobileOS=" + MobileOS + "&MobileApp=" + MobileApp + "&arrange=" + arrange + "&contentTypeId=" + contentTypeId + "&areaCode=" + areaCode + "&sigunguCode=" + sigunguCode + "&listYN=" + listYN

url = endpoint + paramset
print(url)
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, 'html.parser')
title_list = bs_obj.findAll("title")
print(title_list)


