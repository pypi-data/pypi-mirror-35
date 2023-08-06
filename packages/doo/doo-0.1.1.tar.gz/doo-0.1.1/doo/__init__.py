import os
import sys
from doo import app

def doo():   
    sweetest_dir = os.path.dirname(os.path.realpath(__file__))
    current_dir = os.getcwd()
    extract(os.path.join(sweetest_dir, 'EMOS.xlsx'), current_dir)

    print('\n生成 doo example 成功\n')
    
    app.serve('127.0.0.1', 5000, debug=True)


   