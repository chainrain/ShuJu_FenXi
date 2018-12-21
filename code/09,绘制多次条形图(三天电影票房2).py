from matplotlib import pyplot as plt
from matplotlib import font_manager

"""4部电影三天的票房数"""

myfont = font_manager.FontProperties(fname="/home/python/Desktop/ShuJu_FenXi/中文字体/NotoSansCJK-Black.ttc")

# 基本信息
a = ['猩球崛起3:终极之战', "敦刻尔克", '蜘蛛侠:英雄归来', '战狼2']
day16 = [15746, 312, 4497, 319]
day15 = [12357, 156, 2045, 168]
day14 = [2358, 399, 2358, 362]

# 条形图的宽度,全局变量
width = 0.2

# x轴绘制点
x_day14 = list(range(len(a)))
x_day14a = [i * width for i in x_day14]
# print(x_day14a)
x_day15a = [i * width + 1 for i in x_day14]
# print(x_day15a)
x_day16a = [i * width + 2 for i in x_day14]
# print(x_day16a)

# 绘图
plt.bar(x=x_day14a, height=day14, width=width,label='12月14日')
plt.bar(x=x_day15a, height=day15, width=width,label='12月15日')
plt.bar(x=x_day16a, height=day16, width=width,label='12月16日')

# 添加图例
plt.legend(prop=myfont)

# x轴刻度描述
_x = list(x_day14a) + list(x_day15a) + list(x_day16a)
# print(_x)
a += a + a  # 有三天,所以要添加三次
plt.xticks(_x, a,fontproperties=myfont)

# y轴刻度描述
_y = list(day14) + list(day15) + list(day16)
plt.yticks(_y)

# y轴总体描述
plt.ylabel('票房',fontproperties=myfont,rotation=0)

# 展示
plt.show()
