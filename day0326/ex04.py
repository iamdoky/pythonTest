import requests
import json

url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
r = requests.get(url)
text = bytes(r.text,'iso-8859-1').decode('utf-8')
list = json.loads(text)
for row in list:
    print(row['code'],row['value'])






