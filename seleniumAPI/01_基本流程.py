#创建浏览器对象
from selenium import webdriver

driver=webdriver.Chrome()
#driver1=webdriver.firefox()

#获取指定页面
url="http://www.baidu.com"
driver.get(url)
print("1. %s" % driver.current_url)      #打印出当前界面的url
print(driver.title)       #打印出当前页面的title
''' 
#页面最大化
driver.maximize_window()

#页面大小的获取和设置
print(driver.get_window_size())
driver.set_window_size(400,400)

#页面位置
print(driver.get_window_position())
driver.get_window_position(100,100)    #分别向右向下移动100
'''
url_zhihu="http://zhuanlan.zhihu.com"
driver.get(url_zhihu)
print("2. %s" % driver.current_url)    #打印出当前界面的url
print(driver.title)       #打印出当前页面的title
driver.back()          #回退到之前页面
print("3. %s" % driver.current_url)         #打印出当前界面的url
print(driver.title)       #打印出当前页面的title
driver.forward()     #前进到第二个页面
print("4. %s" % driver.current_url)      #打印出当前界面的url
print(driver.title)       #打印出当前页面的title
driver.refresh()     #刷新页面
print("5. %s" % driver.current_url)          #打印出当前界面的url
print(driver.title)       #打印出当前页面的title

#关闭页面
driver.close()