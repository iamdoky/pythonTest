import requests
import json

def park_seuol():
    endpoint = "http://openapi.seoul.go.kr:8088/"
    KEY	= ""
    TYPE = "json"
    SERVICE	= "GetParkInfo"
    START_= "1"
    END_INDEX = "50"

    paramset = KEY+'/'+TYPE+'/'+SERVICE+'/'+START_+'/'+END_INDEX
    url = endpoint+paramset
    print(url)
    result = requests.get(url)
    park = result.json()
    info1 = (park['GetParkInfo']['row'])
    info2 = []
    for item in info1:
        name = (item['PARKING_NAME'])
        addr = (item['ADDR'])
        lat = (item['LAT'])
        lng = (item['LNG'])
        info2.append({'name':name,'addr':addr,'lat':lat,'lng':lng})
    return info2


def seoul():
    url = 'http://openapi.seoul.go.kr:8088/6e706d73476b646833374b71425a69/json/GetParkInfo/1/5'
    arr = []
    r = requests.get(url).text
    obj = json.loads(r)
    total = int(obj['GetParkInfo']['list_total_count'])
    for start in range(1, total, 1000):
        end = start + 1000 - 1
        if end > total:
            end = total
        suburl = 'http://openapi.seoul.go.kr:8088/6e706d73476b646833374b71425a69/json/GetParkInfo/' + str(
            start) + '/' + str(end)
        data = json.loads(requests.get(suburl).text)
        row = data['GetParkInfo']['row']
        for item in row:
            name = item['PARKING_NAME']
            addr = item['ADDR']
            lat = item['LAT']
            lng = item['LNG']
            arr.append({'name': name, 'addr': addr, 'lat': lat, 'lng': 'lng'})
    return arr





