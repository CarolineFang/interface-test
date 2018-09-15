from selenium import webdriver

url = 'https://www.zhihu.com/explore'
dr = webdriver.Chrome()
dr.get(url)

daily_div = dr.find_element_by_css_selector('div[data-type="daily"]')

for link in daily_div.find_elements_by_css_selector('.question_link'):
    print(link.text)

dr.quit()