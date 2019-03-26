from urllib.parse import quote
import requests
from bs4 import BeautifulSoup
def pharmacy():
    endPoint ='http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
    serviceKey = 'UoL8y2fnhJVqh9eHvIKkVzCNyD2IYj%2BJKaidjN3NMXyQjQhJ%2F72eQp1DaxdONF1T%2BPCAAm0hfB7ys%2FPhIcxnwQ%3D%3D'

    Q0 = quote('서울특별시')
    # Q1 = quote('강남구')
    # QN = quote('삼성약국')
    # QT = "1"
    ORD = "name"
    pageNo = "1"
    startPage= "1"
    numOfRows = "50"
    pageSize = "10"

    paramset = "serviceKey="+serviceKey+"&Q0="+Q0+"&ORD="+ORD+"&pageNo="+pageNo+"&startPage="+startPage+"&numOfRows="+numOfRows+"&pageSize="+pageSize

    url = endPoint+paramset
    result = requests.get(url)
    obj = BeautifulSoup(result.content,'html.parser')
    items = obj.findAll('item')
    map = []
    for item in items:
        s = item.find('dutytime8c')
        c = item.find('dutytime7c')
        if s != None or c != None:
            addr = item.find('dutyaddr').text
            name = item.find('dutyname').text
            w1 = item.find('wgs84lat').text
            w2 = item.find('wgs84lon').text
            map.append({'addr':addr,'name':name,'w1':w1,'w2':w2})
    return map

