from Util.DirUtil import make_curdate_dir
from Util.DateStr import *
import os
from selenium import webdriver
from Conf.ProjVar import pic_capture_dir



def take_pic(driver):
    try:
        '''
        调用get_screenshot_as_file(filename)方法，对浏览器当前打开页面
        进行截图,并保为C盘下的screenPicture.png文件。
        '''
        file_path = make_curdate_dir(pic_capture_dir)
        pic_path = os.path.join(file_path, get_english_current_time() + ".png")
        print(pic_path)
        result = driver.get_screenshot_as_file(pic_path)
        return pic_path
    except IOError as e:
        print(e)


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="d:\\chromedriver")
    driver.get("http://www.baidu.com")
    take_pic(driver)
