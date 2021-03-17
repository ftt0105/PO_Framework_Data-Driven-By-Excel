import os
#print(os.path.abspath(__file__))
#print(os.path.dirname(os.path.abspath(__file__)))

#当前工程在硬盘上的绝对路径
proj_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(proj_dir_path)

#配置文件的绝对路径
conf_file_path = os.path.join(proj_dir_path,"conf","ElementsRepository.ini")
print(conf_file_path)

#配置用什么浏览器跑case
browser_name = "chrome"


#浏览器驱动的位置
chrome_driver_path = "d:\\chromedriver"
ie_driver_path = "d:\\IEDriverServer"
firefox_driver_path = "d:\\geckodriver.exe"

#测试数据文件第一个登录sheet的列号设置
login_username_col_no= 1
login_passwd_col_no= 2
contact_teat_data_sheet_name_col_no = 3
login_data_valid_col_no=4
login_end_time_col_no = 5
login_test_result_col_no = 6

#联系人sheet数据中的列号设置
contact_name_col_no=1
contact_email_col_no=2
contact_mobile_col_no=4
contact_info_col_no=5
assert_word_col_no=6
contact_data_valid_col_no=7
test_end_time_col_no = 8
test_result_col_no = 9

#截图目录
pic_capture_dir = os.path.join(proj_dir_path,"ScreenCapture")
pic_path_col_no = 10