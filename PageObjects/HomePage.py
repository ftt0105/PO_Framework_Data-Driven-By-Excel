from Conf.ProjVar import conf_file_path
from Util.ReadConfig import read_ini_file_option
from Util.LocateElement import find_element

class HomePage():
    def __init__(self,driver):
        self.driver  = driver
        if "main.jsp" not in driver.current_url:
            print("此页面未处于登录状态后的首页")

    def get_address_link(self):
        locate_method, locate_exp = read_ini_file_option(conf_file_path, "126mail_homePage","homePage.addressLink").split(">")
        address_link = find_element(self.driver, locate_method, locate_exp)
        return address_link

    def click_address_link(self):
        address_link = self.get_address_link()
        address_link.click()
        import time
        time.sleep(4)
"""       
class HomePage():
    def __init__(self,driver):
        self.driver  = driver
        if "main.jsp" not in driver.current_url:
            print("此页面未处于登录状态后的首页")

    def get_address_link(self):
        address_link  = self.driver.find_element_by_xpath("//div[.='通讯录']")
        return address_link

    def click_address_link(self):
        address_link = self.get_address_link()
        address_link.click()
        import time
        time.sleep(4)
"""