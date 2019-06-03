import matplotlib.pyplot as plt  #绘图模块
from openpyxl import load_workbook
import configparser
from wifi_data.do_excel_data import DoExcel
import numpy as np
#导入数据
cf = configparser.ConfigParser()
cf.read('wifi.conf', encoding='utf-8')
excel = cf.get('wifi_data', 'excel')
url = "C:\\Users\\t\Desktop\WiFi-data\\time_data\\" + excel

# wb = load_workbook(url,encoding = 'utf-8')
# sheet = wb['old_repetition']
do_excel = DoExcel(url,'old_repetition')
do_excel2 = DoExcel('C:\\Users\\t\Desktop\WiFi-data\\time_data\wifi2.xlsx','old_repetition')
do_excel3 = DoExcel('C:\\Users\\t\Desktop\WiFi-data\\time_data\wifi3.xlsx','old_repetition')
do_excel4 = DoExcel('C:\\Users\\t\Desktop\WiFi-data\\time_data\wifi4.xlsx','old_repetition')
do_excel5 = DoExcel('C:\\Users\\t\Desktop\WiFi-data\\time_data\wifi5.xlsx','old_repetition')
do_excel6 = DoExcel('C:\\Users\\t\Desktop\WiFi-data\\time_data\wifi6.xlsx','old_repetition')

old_time1 = do_excel.get_time()
new_time1 = do_excel.get_newtime()
# print(type(new_time1),new_time1)
old_time2 = do_excel2.get_time()
new_time2 = do_excel2.get_newtime()
old_time3 = do_excel3.get_time()
new_time3 = do_excel3.get_newtime()
old_time4 = do_excel4.get_time()
new_time4 = do_excel4.get_newtime()
old_time5 = do_excel5.get_time()
new_time5 = do_excel5.get_newtime()
old_time6 = do_excel6.get_time()
new_time6 = do_excel6.get_newtime()

# 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
plt.figure(figsize=(10,10), dpi=80)
#柱子总数
N = 12
#柱子对于的值
val = ("old_time","new_time")
values = (old_time1,new_time1,old_time2,new_time2,old_time3,new_time3,\
          old_time4,new_time4,old_time5,new_time5,old_time6,new_time6)
print(values)
#每个柱子下标的序列
index = np.arange(N)
#柱子的宽度
width = 0.15
# 绘制柱状图, 每根柱子的颜色为紫罗兰色
p2 = plt.bar(index, values, width, label="data",color="#87CEFA")
# 设置横轴标签
plt.xlabel('Months')
# 设置纵轴标签
plt.ylabel('data(mm)')
# 添加标题
plt.title('old_data-new_data')
# 添加纵横轴的刻度
plt.xticks(index, ('old1','new1','old2','new2','old3','new3','old4','new4','old5','new5','old6','new6'))
plt.yticks(np.arange(0, 440, 10))
# 添加图例
plt.legend(loc="upper right")
plt.show()