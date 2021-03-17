from Conf.ProjVar import chrome_driver_path,ie_driver_path,firefox_driver_path
from PageObjects import IndexPage,HomePage,ContactPerson

from selenium import webdriver
import time
from Conf.ProjVar import browser_name

driver = ""

def browser(browser_name):
    global driver
    if "ie" in browser_name.lower():
        driver = webdriver.Ie(executable_path=ie_driver_path)
    elif "chrome" in browser_name.lower():
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
    else:
        driver = webdriver.Firefox(executable_path=firefox_driver_path)
    return driver

driver = browser(browser_name)

def login(username,passwd):
    global driver
    #driver = webdriver.Chrome(executable_path=chrome_driver_path)
    index_page = IndexPage.IndexPage(driver)
    index_page.login(username,passwd)
    time.sleep(4)
    assert "通讯录" in driver.page_source
    return driver

def addContact(name,email,phone,other_info,assert_keyword):
    global driver
    home_page = HomePage.HomePage(driver)
    home_page. click_address_link()
    contact_person = ContactPerson.ContactPerson(driver)
    contact_person.click_create_contact_person_button()
    contact_person.input_name(name)
    contact_person.input_email(email)
    contact_person.input_phone(phone)
    contact_person.input_other_info(other_info)
    contact_person.click_confirm_button()
    time.sleep(1)
    assert assert_keyword in driver.page_source


def quit():
    global  driver
    if driver is not None and (not isinstance(driver,str)):
        driver.quit()


if __name__ == "__main__":
    browser("chrome")
    login("tingtingzy1","Buyall01$")
    addContact("王五","dsfdds@qq.com","1253332231","今天天气不错")
    driver.quit()