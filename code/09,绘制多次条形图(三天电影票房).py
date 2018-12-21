from matplotlib import pyplot as plt
from matplotlib import font_manager
"""4部电影三天的票房数"""

myfont = font_manager.FontProperties(fname="/home/python/Desktop/ShuJu_FenXi/中文字体/NotoSansCJK-Black.ttc")

a = ['猩球崛起3:终极之战', "敦刻尔克", '蜘蛛侠:英雄归来', '战狼2']
day16 = [15746, 312, 4497, 319]
day15 = [12357, 156, 2045, 168]
day14 = [2358, 399, 2358, 362]

# 条形图的宽度,全局变量
width = 0.2

# day14的x轴绘制点
x_day14= list(range(len(a)))
print(x_day14)
# day15的x轴绘制点,在day14的基础上平移一个柱宽
x_day15= [i+width for i in x_day14]
print(x_day15)
# day16的x轴绘制点,在day15的基础上平移一个柱宽
x_day16 = [i+width*2 for i in x_day14]
print(x_day16)

# 设置图片大小
plt.figure(figsize=(20,8),dpi=80)

# 绘图
plt.bar(x=x_day14,height=day14,width=width,label='12月14日')
plt.bar(x=x_day15,height=day15,width=width,label='12月15日')
plt.bar(x=x_day16,height=day16,width=width,label='12月16日')

# 显示图例
plt.legend(prop=myfont)

# 设置x轴刻度,绘制再中间的,达到居中的效果
plt.xticks(x_day15,a,fontproperties=myfont)

# 展示
plt.show()