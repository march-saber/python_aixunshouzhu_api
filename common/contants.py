import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #动态获取文件API_1的路径
"""
os.path.dirname(path):动态获取当前文件的文件夹路径，往上一层
os.path.abspath(__file__) #动态获取当前文件的绝对路径
"""
print(base_dir)

shouzhu_case_file = os.path.join(base_dir,'data','shouzhu_case.xlsx')
print(shouzhu_case_file)

global_file = os.path.join(base_dir,'config','global.conf')
print(global_file)

online_file = os.path.join(base_dir,'config','online.conf')
print(online_file)

test_file = os.path.join(base_dir,'config','test.conf')
print(test_file)

log_dir = os.path.join(base_dir,'log')
print(log_dir)

report_dir = os.path.join(base_dir,'reports')

case_dir = os.path.join(base_dir,'testcases')



