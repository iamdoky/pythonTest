import requests

endpoint = "http://www.career.go.kr/cnet/openapi/getOpenApi?"
apiKey = ""
svcType = "api"
svcCode = "JOB"
contentType = "json"
gubun = "job_dic_list"
perPage = "10000"

paramset = 'apiKey='+apiKey+'&svcType='+svcType+'&svcCode='+svcCode+'&contentType='+contentType+'&gubun='+gubun+'&perPage='+perPage
url = endpoint+paramset
print(url)
result = requests.get(url)
career_data = result.json()
career_list = career_data['dataSearch']['content']
cnt = 0
for item in career_list:
    if item['salery'] != 'null':
        sal = int(item['salery'][0:4])
        j = item['job']
        print(sal,j)
        if sal >= 4000:
            cnt += 1
print(cnt)
