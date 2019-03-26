from urllib.parse import quote
import requests
from bs4 import BeautifulSoup

endPoint ='http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
serviceKey = 'UoL8y2fnhJVqh9eHvIKkVzCNyD2IYj%2BJKaidjN3NMXyQjQhJ%2F72eQp1DaxdONF1T%2BPCAAm0hfB7ys%2FPhIcxnwQ%3D%3D'

Q0 = quote('서울특별시')	
# Q1 = quote('강남구')
# QN = quote('삼성약국')
# QT = "1"
ORD = "name"
pageNo = "1"
startPage= "1"
numOfRows = "5000"
pageSize = "10"

# paramset = "serviceKey="+serviceKey+"&Q0="+Q0+"&Q1="+Q1+"&QN="+QN+"&QT="+QT+"&ORD="+ORD+"&pageNo="+pageNo+"&startPage="+startPage+"&numOfRows="+numOfRows+"&pageSize="+pageSize
paramset = "serviceKey="+serviceKey+"&Q0="+Q0+"&ORD="+ORD+"&pageNo="+pageNo+"&startPage="+startPage+"&numOfRows="+numOfRows+"&pageSize="+pageSize

url = endPoint+paramset
result = requests.get(url)
obj = BeautifulSoup(result.content,'html.parser')
items = obj.findAll('item')
for item in items:
    tag_item = item.find("dutyname").text
    print(tag_item)

