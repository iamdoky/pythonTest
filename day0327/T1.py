import requests
import json

url = 'http://openapi.seoul.go.kr:8088/6e706d73476b646833374b71425a69/json/GetParkInfo/1/5'

arr = []

r = requests.get(url).text
obj = json.loads(r)
total = int(obj['GetParkInfo']['list_total_count'])
for start in range(1,total,1000):
    end = start+1000-1
    if end > total:
        end = total
    suburl = 'http://openapi.seoul.go.kr:8088/6e706d73476b646833374b71425a69/json/GetParkInfo/'+str(start)+'/'+str(end)
    data = json.loads(requests.get(suburl).text)
    row = data['GetParkInfo']['row']
    for item in row:
        name = item['PARKING_NAME']
        addr = item['ADDR']
        lat = item['LAT']
        lng = item['LNG']
        arr.append({'name':name,'addr':addr,'lat':lat,'lng':'lng'})


