from selenium import webdriver
import time

class Common(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()

        #访问指定url
    def open_url(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
    #对定位方式的封装
    def locate_element(self,locatetype,value):   #locatetype通过哪种方式进行定位   value  他的这个元素是什么

            #通过id进行定位
        if(locatetype=="id"):
            el=self.driver.find_element_by_id(value)

            #通过name进行定位
        if(locatetype=="name"):
            el=self.driver.find_element_by_name(value)

            #通过class_name进行定位
        if(locatetype=="class_name"):
            el=self.driver.find_element_by_class_name(value)

            #通过tag_name进行定位
        if(locatetype=="tag_name"):
            el=self.driver.find_element_by_tag_name(value)

            #通过link进行定位
        if(locatetype=="link"):
            el=self.driver.find_element_by_partial_link_text(value)

             #通过partial_link进行定位
        if(locatetype=="partial_link"):
            el=self.driver.find_element_by_partial_link_text(value)

            #通过css进行定位
        if(locatetype=="css"):
            el=self.driver.find_element_by_css_selector(value)

            #通过xpath进行定位
        if(locatetype=="xpath"):
            el=self.driver.find_element_by_xpath(value)
        return el if el else None

    #对点击元素的封装
    def click(self,locatetype,value):
        el=self.locate_element(locatetype,value)
        el.click()

    #对输入信息操作的封装
    def input_date(self,locatetype,value,data):
        el=self.locate_element(locatetype,value)
        el.send_keys(data)

    #获取定位到的元素内容
    def get_text(self,locatetype,value):
        el=self.locate_element(locatetype,value)
        return el.text

    #获取标签属性
    def get_attr(self,locatetypr,value,attr):
        el=self.locate_element(locatetypr,value)
        return  el.get_attribute(attr)

    def  __del__(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    com=Common()
    com.open_url("http://www.baidu.com")