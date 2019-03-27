from selenium import webdriver
import bs4

driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver')
driver.implicitly_wait(3)
url = "https://www.instagram.com/accounts/login/?source=auth_switcher"
driver.get(url)

driver.find_element_by_id("m_id").send_keys("id")
driver.find_element_by_id("m_passwd").send_keys("pwd")
driver.find_element_by_xpath('//*[@id="login_btn"]').click()

target_url = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
driver.get(target_url)

html = driver.page_source
bs_obj = bs4.BeautifulSoup(html, 'html.parser')
res = bs_obj.find("dl", {"class": "mileage_section1"})
res = res.find("span").text
print(res)