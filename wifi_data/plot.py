# import matplotlib.pyplot as plt
#
#
# name_list = ['1', '2', '3', '4', '5', '6']

import matplotlib.pyplot as plt
# from openpyxl import load_workbook
# import configparser
#
# cf = configparser.ConfigParser()
# cf.read('wifi.conf', encoding='utf-8')
# excel = cf.get('wifi_data', 'excel')
# url = "C:\\Users\\t\Desktop\WiFi-data\\time_data\\" + excel
# wb = load_workbook(url,encoding = 'utf-8')
# sheet = wb['old_repetition']



list_00 = [0.16, 0.33, 0.20, 0.31]
list_01 = [0.05, 0.33, 0.39, 0.29]

name_list = ['A', 'B']
x = list(range(len(name_list)))
# total_width, n = 0.8, 4
width = 0.2
plt.bar(x, list_00, width=width, label='a', tick_label=name_list, fc='y')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, list_01, width=width, label='b', fc='r')
for i in range(len(x)):
    x[i] = x[i] + width

plt.legend()
plt.show()
