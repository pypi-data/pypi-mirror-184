import configparser
import csv,time,json
import hashlib
import os
import pymysql
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from requests import Session


class RequestsUtil:
    '''
    封装Requests
    '''
    def send_requests(self,method,url,  data=None, json=None, **kwargs):
        if method in ('g','get'):
            return requests.get(url=url, params=data, **kwargs)
        elif method in ('p','post'):
            return requests.post(url=url,  data=data, json=json, **kwargs)
        else:
            raise Exception('暂时不支持get、post之外的请求方式')
    def Session(self):
        return Session()

class MD5:
    def md5_password(self,text):
        hl = hashlib.md5()
        hl.update(text.encode(encoding='utf8'))
        md5 = hl.hexdigest()
        return str(md5)

class Base:
    '''
    对selenium进行二次封装，用于操作页面元素
    '''
    def __init__(self,browser='c'):
        '''
        根据传入的浏览器类型，实例化一个相应的浏览器对象
        :param browser: 浏览器类型，默认为谷歌浏览器
        '''
        desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
        desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出

        if browser in ('c','chrome'):
            self.driver = webdriver.Chrome()
        elif browser in ('f','firefox'):
            self.driver = webdriver.Firefox()
        elif browser in ('i','ie'):
            self.driver = webdriver.Ie()
        else:

            raise Exception('浏览器类型暂不支持')
        self.driver.maximize_window()

    def open_url(self,url):

        self.driver.get(url)

    def __convert_selector_locator(self,selector):
        '''
        把选择器转换成定位器
        内部方法，不需要公开，私有化即可
        :param selector: 元素选择器，类似于'i,account'。i:定位的标识；account:定位的值
        :return: locator: 元素定位器，类似于By.ID,account
        '''
        selector_key = selector.split(',')[0]
        selector_value = selector.split(',')[1]
        if selector_key in ('i','id'):
            locator = (By.ID,selector_value)
        elif selector_key in ('x','xpath'):
            locator = (By.XPATH,selector_value)
        elif selector_key in ('s','css'):
            locator = (By.CSS_SELECTOR,selector_value)
        elif selector_key in ('n','name'):
            locator = (By.NAME,selector_value)
        elif selector_key in ('c','class'):
            locator = (By.CLASS_NAME,selector_value)
        elif selector_key in ('t','tag'):
            locator = (By.TAG_NAME,selector_value)
        elif selector_key in ('l','link'):
            locator = (By.LINK_TEXT,selector_value)
        elif selector_key in ('p','partial'):
            locator = (By.PARTIAL_LINK_TEXT,selector_value)
        else:
            raise Exception('输入的定位方式不合法')
        return locator

    def get_element(self,selector):
        locator = self.__convert_selector_locator(selector)
        element = self.driver.find_element(*locator)
        return element

    def get_elements(self,selector):
        locator = self.__convert_selector_locator(selector)
        elements = self.driver.find_elements(*locator)
        return elements

    def sleep(self,second=1):
        time.sleep(second)

    def switch_to_iframe(self,selector):
        element = self.get_element(selector)
        self.driver.switch_to.frame(element)

    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    def implicitly_wait(self,s=30):
        self.driver.implicitly_wait(s)

    def WebDriverWait(self, selecter):
        locator = self.__convert_selector_locator(selecter)
        WebDriverWait(self.driver, 10, 0.5).until(expected_conditions.presence_of_element_located(locator))

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def select_by_index(self,selector,index):
        element = self.get_element(selector)
        Select(element).select_by_index(index)

    def select_by_value(self,selector,value):
        element = self.get_element(selector)
        Select(element).select_by_value(value)

    def select_by_visible_text(self,selector,text):
        element = self.get_element(selector)
        Select(element).select_by_visible_text(text)

    def execute_script(self,js_script):
        self.driver.execute_script(js_script)

    def alert_accept(self):
        self.driver.switch_to.alert.accept()

    def alert_dismiss(self):
        self.driver.switch_to.alert.dismiss()

    def Action(self,selector):
        ActionChains(self.driver).click(self.get_element(selector)).perform()

    def double_Action(self,selector):
        ActionChains(self.driver).double_click(self.get_element(selector)).perform()

    def move_to_element(self,xpath):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(xpath)).perform()

    def execute_script_click(self,elemnt):
        self.driver.execute_script("arguments[0].click();",elemnt)

    def screenshot(self,path):
        self.driver.get_screenshot_as_file(path)

    def close(self):
        self.driver.quit()

class BasePage:
    def __init__(self,base:Base):
        self.base=base

class CsvUtil:
    def get_csv_data(self,file,mode='r',encoding='utf8'):
        data_list = []
        if os.path.exists('data'):
            data = open(file='data/%s.csv'%file,mode=mode,encoding=encoding)
        else:
            data = open(file='../data/%s.csv' % file, mode=mode, encoding=encoding)
        csv_data = csv.reader(data)
        for i in csv_data:
            data_list.append(tuple(i))
        data.close()
        return data_list

    # 以字典方式读取
    def get_csv_data_dict(self,file,mode='r',encoding='utf8'):
        res = []
        if os.path.exists('data'):
            data = open(file='data/%s.csv'%file,mode=mode,encoding=encoding)
        else:
            data = open(file='../data/%s.csv' % file, mode=mode, encoding=encoding)
        csv_data = csv.DictReader(data)
        for i in csv_data:
            res.append(dict(i))
        return res

class jsonUtil:
    def get_json_dir(self,json_dir):
        res = []
        if os.path.exists('data'):
            path = "data/%s"%json_dir
        else:
            path = "../data/%s"%json_dir
        arr = os.listdir(path)
        for i in arr:
            with open(path+"/"+i,"r+",encoding="utf8") as file:
                res.append(json.loads(file.read()))
        return res

class RequestUtil:

    def send_request(self,method,url, data=None, json=None,**kwargs):
        if method in ('g','get'):

            return requests.get(url=url,params=data,**kwargs)
        elif method in ('p','post'):
            return requests.post(url=url, data=data, json=json, **kwargs)
        else:
            raise Exception('暂不支持get、post之外的请求')

    def session(self):
        return Session()

class ConfUtil:
    def get_data(self,file,key,value):
        conf=configparser.ConfigParser()
        if os.path.exists('conf'):
            conf.read(r'conf/%s.ini'%file)
        else:
            conf.read(r'../conf/%s.ini' %file)

        return conf.get(key,value)

class ListUtil:
    def list_unonly_remove(self,list: list, str):
        remove_index = []
        for i in list:
            if str not in i:
                remove_index.append(i)
        for i in remove_index:
            list.remove(i)

        return list



class MysqlUtil:

    def __init__(self,host='localhost',user='root',password='',port=3306):
        try:
            self.db = pymysql.connect(host=host,user=user,password=password,port=port)
            self.cursor = self.db.cursor()
        except:
            raise Exception('连接数据库的参数不合法')

    def get_data(self,sql):
        '''
        根据传入的sql语句查询数据
        :param sql: sql语句
        :return: [(),(),()..]模型的列表
        '''
        # info = []
        cursor = self.cursor
        cursor.execute(sql)
        data = cursor.fetchall()
        # for i in data:
        #     info.append(tuple(i))
        info = [tuple(i) for i in data]
        return info

    def close(self):
        self.cursor.close()
        self.db.close()






if __name__ == '__main__':
    mysql=MysqlUtil(password='123456')
    data=mysql.get_data('select * from mysql.user;')
    print(data)
    mysql.close()
    url='http://www.baidu.com'
    re=requests.get(url)
    re.encoding=re.apparent_encoding
    print(re.text)