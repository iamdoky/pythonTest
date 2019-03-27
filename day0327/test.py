import day0327.seoulFunc

# r = day0327.seoulFunc.park_seuol()
# for i in r:
#     a = i['addr']
#     if a == i['addr']:
#         print(i['name'])

r = day0327.seoulFunc.seoul()
print(len(r))

#
# import requests
# import json
#
# endpoint = "http://openapi.seoul.go.kr:8088/"
# KEY	= "6e706d73476b646833374b71425a69"
# TYPE = "json"
# SERVICE	= "GetParkInfo"
# START_= "1"
# END_INDEX = "10"
#
# paramset = KEY+'/'+TYPE+'/'+SERVICE+'/'+START_+'/'+END_INDEX
# url = endpoint+paramset
# result = requests.get(url)
# park = result.json()
# info1 = (park['GetParkInfo']['row'])
# info2 = []
# for item in info1:
#     name = (item['PARKING_NAME'])
#     addr = (item['ADDR'])
#     lat = (item['LAT'])
#     lng = (item['LNG'])
#     info2.append({'name':name,'addr':addr,'lat':lat,'lng':lng})
# print(info2)



