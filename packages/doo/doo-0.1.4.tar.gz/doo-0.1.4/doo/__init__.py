import os
import sys
from shutil import copyfile
from doo.mock import app


def mkdir(path):
    # 引入模块
    import os
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print path+' 创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' 目录已存在'
        return False


def doo():
    sweetest_dir = os.path.dirname(os.path.realpath(__file__))
    current_dir = os.getcwd()
    doo_folder = os.path.join(current_dir, 'doo_example')
    mkdir(doo_folder)
    copyfile(os.path.join(sweetest_dir, 'EMOS.xlsx'), os.path.join(doo_folder, 'EMOS.xlsx'))
    copyfile(os.path.join(sweetest_dir, 'app.py'), os.path.join(doo_folder, 'app.py'))

    print('\n生成 doo example 成功\n')

    app.serve('127.0.0.1', 5000, debug=True)
