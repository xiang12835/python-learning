# coding=utf-8
""" 02. 散点图
"""


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0., 5., 0.2)

# 红色破折号, 蓝色方块 ，绿色三角块
plt.plot(x, x, 'r--', x, x**2, 'bs', x, x**3, 'g^')
plt.show()
