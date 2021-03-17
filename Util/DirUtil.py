import os
from Util.DateStr import *
from Conf.ProjVar import proj_dir_path


def make_curdate_dir(file_path):
    curdate = get_chinese_current_date()
    #下面一行是修改的代码
    dir_path = os.path.join(file_path,curdate)
    print(dir_path)
    cur_hour = str(get_cur_hour())
    dir_path = os.path.join(dir_path,cur_hour)
    print(dir_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return  dir_path

if __name__ == "__main__":
    print(make_curdate_dir(os.path.join(proj_dir_path, "ScreenCapture")))
