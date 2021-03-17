from PageObjects import IndexPage,HomePage,ContactPerson

from Util import Excel
from Conf.ProjVar import *
import os
from Action.test_steps import login,addContact,quit
import traceback
from Util.DateStr import get_chinese_datetime
from Util.TakePic import  take_pic
from Action.test_steps import driver
import time




test_data_file_path = os.path.join(proj_dir_path,"TestData\\126邮箱联系人.xlsx")
print(test_data_file_path)
excel = Excel.ExcelUtil(test_data_file_path)
excel.set_sheet_by_index(0) #设定为第一个sheet,获取登录账号信息

login_data= excel.get_sheet_all_cell_values()#读出第一个sheet的所有数据

for row in login_data[1:]:
    test_data_flag = True  #默认这个用例执行的结果是True，如果出现任何异常设定为False
    print(row)
    print(row[login_data_valid_col_no])
    if row[login_data_valid_col_no].lower()=="y":
        username= row[login_username_col_no]
        passwd= row[login_passwd_col_no]
        try:
            login(username,passwd)
        except Exception as e:
            traceback.print_exc()
            test_data_flag = False
            quit()
            continue
        test_data_sheet_name = row[contact_teat_data_sheet_name_col_no]
        excel.set_sheet_by_name(test_data_sheet_name)
        # 获取所有联系人的sheet中的所有数据
        contact_data = excel.get_sheet_all_cell_values()
        #设定测试结果sheet作为当前操作sheet
        excel.set_sheet_by_name("测试结果")
        excel.write_a_line_in_sheet(contact_data[0],fgcolor="FF9D6F")
        # 从联系人的sheet中读取数据行
        for contact_row in contact_data[1:]:
            contact_data_flag = True
            if contact_row[contact_data_valid_col_no].lower() == "y":
                name = contact_row[contact_name_col_no]
                email = contact_row[contact_email_col_no]
                mobile = contact_row[contact_mobile_col_no]
                info = contact_row[contact_info_col_no]
                assert_word = contact_row[assert_word_col_no]
                try:
                    addContact(name, email, mobile, info, assert_word)
                except Exception as e:
                    traceback.print_exc()
                    pic_file_path = take_pic(driver)
                    contact_row[pic_path_col_no] = pic_file_path
                    contact_data_flag = False
                    test_data_flag = False

            contact_row[test_end_time_col_no] = get_chinese_datetime()
            if contact_row[contact_data_valid_col_no].lower() != "y":
                contact_row[test_result_col_no] = "未执行"
            elif contact_data_flag:
                contact_row[test_result_col_no] = "成功"
            else:
                contact_row[test_result_col_no] = "失败"
            if contact_row[test_result_col_no] == "失败":
                excel.write_a_line_in_sheet(contact_row,font_color="red")
            else:
                excel.write_a_line_in_sheet(contact_row)

        row[login_end_time_col_no] = get_chinese_datetime()
        if test_data_flag:
            row[login_test_result_col_no] = "成功"
        else:
            row[login_test_result_col_no] = "失败"
        excel.write_a_line_in_sheet(login_data[0], fgcolor="FF9F6F")
        if row[login_test_result_col_no] == "失败":
            excel.write_a_line_in_sheet(row,font_color="red")
        else:
            excel.write_a_line_in_sheet(row)
        quit()

"""
from selenium import webdriver
driver = webdriver.Chrome(executable_path="d:\\chromedriver")
index_page = IndexPage.IndexPage(driver)
index_page.login("tingtingzy1","Buyall01$")
#第一个homepage是模块名，第二个是类名
home_page = HomePage.HomePage(driver)
home_page. click_address_link()
contact_person = ContactPerson.ContactPerson(driver)
contact_person.click_create_contact_person_button()
contact_person.input_name("张思")
contact_person.input_email("ew3fsdfds@qq.com")
contact_person.input_phone("138487383833")
contact_person.input_other_info("今天天气不错")
contact_person.click_confirm_button()


"""
