# coding=utf-8
""" 5.1 普通饼图

"""


import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]

# 设置分离的距离，0表示不分离
explode = (0, 0.1, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

# Equal aspect ratio 保证画出的图是正圆形
plt.axis('equal')

plt.show()
