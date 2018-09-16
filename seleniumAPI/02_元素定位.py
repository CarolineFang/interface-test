from selenium import webdriver
import time


driver=webdriver.Chrome()
'''
#5. 通过partial link text 定位,只能操作a标签,只需要选取部分文本信息
url ="http://www.baidu.com"
driver.get(url)
hao_el=driver.find_element_by_partial_link_text("hao")
hao_el.click()
driver.quit()
'''

#页面定位
'''
#1.  id定位
el_input=driver.find_element_by_id("kw")
el_input.send_keys("selenium")            #输入内容

el_submit=driver.find_element_by_id("su")
el_submit.click()
'''
'''
#2.  通过class name定位
url_douyu="https://www.douyu.com/directory/all"
driver.get(url_douyu)
next_page_el=driver.find_element_by_class_name('shark-pager-next')
next_page_el.click()
time.sleep(5)
'''
'''
#3. 通过name定位
url_renren="http://sns.renren.com/"
driver.get(url_renren)
#定位到"用户名"输入框
user_el=driver.find_element_by_class_name("email")
user_el.send_keys("17173805860")
#定位到"密码"输入框
user_pwd=driver.find_element_by_class_name("password")
user_pwd.send_keys("1qaz@WSX3edc")
#定位到"登录"按钮
login_el=driver.find_element_by_class_id("login")
login_el.click()
'''
'''
#4. 通过link text 定位,link text只能定位a标签
url_58="http://sh.58.com/"
driver.get(url_58)
#定位到房屋出租链接
rent_el=driver.find_element_by_link_text("租房")
rent_el.click()
time.sleep(5)
'''
'''
#6. 通过tag name定位,该元素是页面中第一个该类型标签,或者唯一的一个
url_biying="http://cn.bing.com"
driver.get(url_biying)
input_el=driver.find_element_by_tag_name("input")
input_el.send_keys("selenium")
time.sleep(5)
'''

#7. 通过css selector定位
url_tianmao="http://www.tianmao.com"
driver.get(url_tianmao)
inter_el=driver.find_element_by_css_selector("#content > div.main-nav > div > div > div > a:nth-child(1) > img")
inter_el.click()
time.sleep(5)

#8. 通过xpath定位
url_douban="https://movie.douban.com/top250"
driver.get(url_douban)

yinyue_el=driver.find_element_by_xpath(r'//*[@id="db-global-nav"]/div/div[3]/ul/li[4]/a')
yinyue_el.click()
time.sleep(5)

driver.close()