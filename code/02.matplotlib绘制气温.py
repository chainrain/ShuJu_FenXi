import random
from matplotlib import pyplot as plt

"""
matplotlib主要流程:
1.创建XY轴
2.设置最终图片大小(可省略)
3.绘图
4.设置刻度(可省略)
5.保存图片(可省略)
6.显示图片


matplotlib绘制120分钟内的气温,限制在20到35度之间
"""

# 1.创建XY轴
x = range(0,121)
y = [random.randint(20,35) for i in range(121)]

# 2.设置最终图片大小(可省略)
plt.figure(figsize=(20,8),dpi=80)

# 3.绘图
plt.plot(x,y)

# 4.设置刻度(可省略)
plt.xticks(x)
plt.yticks(y)

# 6.显示图片
plt.show()