from Util.ReadConfig import *
from Util.LocateElement import  *
from Conf.ProjVar import proj_dir_path,conf_file_path

class IndexPage():
    def __init__(self,driver):
        self.driver = driver
        if self.driver.current_url!="https://mail.126.com":
            self.driver.get("https://mail.126.com")
    #获取iframe网页对象
    def get_iframe(self):
        locate_method,locate_exp = read_ini_file_option(conf_file_path,"126mail_indexPage","indexPage.frame").split(">")
        iframe = find_element(self.driver,locate_method,locate_exp)
        return iframe
    #切入iframe
    def switch_to_iframe(self):
        iframe = self.get_iframe()
        self.driver.switch_to.frame(iframe)
    #切出iframe
    def switch_out_iframe(self):
        self.driver.switch_to.default_content()
    #获得用户名网页对象
    def get_username(self):
        locate_method, locate_exp = read_ini_file_option(conf_file_path, "126mail_indexPage", "indexPage.username").split(">")
        user_name = find_element(self.driver,locate_method,locate_exp)
        return user_name
    #获得密码框网页对象
    def get_passwd(self):
        locate_method, locate_exp = read_ini_file_option(conf_file_path, "126mail_indexPage","indexPage.password").split(">")
        passwd = find_element(self.driver, locate_method, locate_exp)
        return passwd
    #获得登录蛮牛网页对象
    def get_submit_button(self):
        locate_method, locate_exp = read_ini_file_option(conf_file_path, "126mail_indexPage", "indexPage.loginbutton").split(">")
        submit_button = find_element(self.driver, locate_method, locate_exp)
        return submit_button
    #输入用户名
    def input_username(self,user_name):
        username = self.get_username()
        username.send_keys(user_name)
    #输入密码
    def input_passwd(self,pass_wd):
        passwd = self.get_passwd()
        passwd.send_keys(pass_wd)
    #点击登录按钮
    def click_submit(self):
        submit = self.get_submit_button()
        submit.click()
        import time
        time.sleep(5)

    def login(self,user_name,pass_wd):
        self.switch_to_iframe()
        self.input_username(user_name)
        self.input_passwd(pass_wd)
        self.click_submit()

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="d:\\chromedriver")
    #driver.get("http://mail.126.com")
    index_page = IndexPage(driver)
    index_page.login("tingtingzy1","Buyall01$")
    driver.quit()

"""
class IndexPage():
    def __init__(self,driver):
        self.driver = driver
        if self.driver.current_url!="https://mail.126.com":
            self.driver.get("https://mail.126.com")
            
    #获取iframe网页对象
    def get_iframe(self):
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'x-URS-iframe')]")
        return iframe
    #切入iframe
    def switch_to_iframe(self):
        iframe = self.get_iframe()
        self.driver.switch_to.frame(iframe)
    #切出iframe
    def switch_out_iframe(self):
        self.driver.switch_to.default_content()
    #获得用户名网页对象
    def get_username(self):
        user_name = self.driver.find_element_by_xpath('//input[@name="email"]')
        return user_name
    #获得密码框网页对象
    def get_passwd(self):
        passwd = self.driver.find_element_by_xpath('//input[@name="password"]')
        return passwd
    #获得登录蛮牛网页对象
    def get_submit_button(self):
        submit_button = self.driver.find_element_by_id('dologin')
        return submit_button
    #输入用户名
    def input_username(self,user_name):
        username = self.get_username()
        username.send_keys(user_name)
    #输入密码
    def input_passwd(self,pass_wd):
        passwd = self.get_passwd()
        passwd.send_keys(pass_wd)
    #点击登录按钮
    def click_submit(self):
        submit = self.get_submit_button()
        submit.click()
        import time
        time.sleep(5)
        
    def login(self,user_name,pass_wd):
        self.switch_to_iframe()
        self.input_username(user_name)
        self.input_passwd(pass_wd)
        self.click_submit()

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="d:\\chromedriver")
    #driver.get("http://mail.126.com")
    index_page = IndexPage(driver)
    index_page.login("tingtingzy1","Buyall01$")
    driver.quit()
"""