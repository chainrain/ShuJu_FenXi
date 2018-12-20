from pylab import *
import random
from matplotlib import pyplot as plt
import matplotlib
import matplotlib.font_manager


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

myfont = matplotlib.font_manager.FontProperties(fname="/home/python/Desktop/数据分析/中文字体/NotoSansCJK-Black.ttc")  # 设定字体
# mpl.rcParams['axes.unicode_minus'] = False

# 1.创建XY轴
x = range(0,121)
y = [random.randint(20,35) for i in range(121)]

# 2.设置最终图片大小(可省略)
plt.figure(figsize=(20,8),dpi=80)

# 3.绘图
plt.plot(x,y)

# 4.设置刻度(可省略)
_x = list(x)[::10]  # 每10个输出
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
# plt.xticks(list(x)[::3],_xtick_labels[::3])  # 取步长,数字和字符串一一对应,数据长度一样
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45,fontproperties=myfont)  # rotation字体旋转xx度


plt.xlabel(u'这里是X坐标',fontproperties=myfont)
plt.ylabel(u'这里是Y坐标',fontproperties=myfont)

# plt.xticks(x)
# plt.yticks(y)

# 6.显示图片
plt.show()