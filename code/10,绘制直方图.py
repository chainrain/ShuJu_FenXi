from matplotlib import pyplot as plt
from matplotlib import font_manager

"""工资水平"""

myfont = font_manager.FontProperties(fname="/home/python/Desktop/ShuJu_FenXi/中文字体/NotoSansCJK-Black.ttc")

# 基本信息,工资,分组定位
salary = [2500, 3300, 2700, 5600, 6700, 5400, 3100, 3500, 7600, 7800,
          8700, 9800, 10400]
group = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘图 参数:density=True是统计占百分比
plt.hist(salary, group, rwidth=0.8)

# x轴刻度
plt.xticks(group)

# 显示y轴最大人数的刻度(可省略,绘图自动排列)
# plt.yticks(range(len(salary)))

# x轴总体描述
plt.xlabel('工资', fontproperties=myfont)
# y轴总体描述
plt.ylabel('工资分组人数', fontproperties=myfont, rotation=0)
# 标题
plt.title(u'测试例子——直方图', FontProperties=myfont)

# 网格
plt.grid()

plt.show()
