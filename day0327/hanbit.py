import requests
from bs4 import BeautifulSoup as bs

# s = requests.session()
# url = 'http://www.hanbit.co.kr/member/login_proc.php'
# data = {'m_id':'','m_passwd':''}
# r = s.post(url,data=data)
# r2 = s.get('http://www.hanbit.co.kr/myhanbit/myhanbit.html').text
# bs_obj = bs(r2,'html.parser')
# dl = bs_obj.find('dl',{'class':'mileage_section1'})
# result = dl.find("span").text
# print(result)

s = requests.session()
url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
data =