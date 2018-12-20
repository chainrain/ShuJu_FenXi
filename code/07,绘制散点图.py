from matplotlib import pyplot as plt
import matplotlib.font_manager
"""
散点图:
3月份和10月份最高气温规律
"""

# 中文字体
myfont = matplotlib.font_manager.FontProperties(fname="/home/python/Desktop/ShuJu_FenXi/中文字体/NotoSansCJK-Black.ttc")

# 3月份(y轴1)
march = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
# 10月份(y轴2)
october = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

# 日期(x轴)
day1 = range(1,32)  # x轴3月绘制前面
day2 = range(51,82)  # x轴10月绘制后面,从51(只要大于3月前面的就行了)开始绘制

# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

# 绘散点图
plt.scatter(x=day1,y=march,label='3月')
plt.scatter(x=day2,y=october,label='10月')

# 调整x轴刻度
_x = list(day1)+list(day2)
_xtick_labels = ["3月{}日".format(i) for i in day1]
_xtick_labels += ["10月{}日".format(i-50) for i in day2]
plt.xticks(_x[::3],_xtick_labels[::3],fontproperties=myfont,rotation=-45)  # [::3]每隔3个显示,以免太密集

# 添加图例
plt.legend(loc="upper left",prop=myfont)

# 添加描述信息
plt.xlabel('3月和10月',fontproperties=myfont)
plt.ylabel('气 温',fontproperties=myfont,rotation=0)
plt.title('3月份和10月份最高气温规律',fontproperties=myfont)

# 展示
plt.show()