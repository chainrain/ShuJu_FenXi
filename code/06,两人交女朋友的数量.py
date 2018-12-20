from matplotlib import pyplot as plt
import matplotlib.font_manager

# 设定字体
myfont = matplotlib.font_manager.FontProperties(fname="/home/python/Desktop/ShuJu_FenXi/中文字体/NotoSansCJK-Black.ttc")

# 1.xy轴
# 两个人11到30岁每年交女朋友的数量.y轴
p1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
p2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
# 年龄,x轴
age = range(11,31)


# 2.设置最终图片大小(可省略)
plt.figure(figsize=(20,8),dpi=80)

# 3.绘图
"""
拥有参数:
label:图例名称
color:线条颜色(也能用16进制的颜色代码)
linestyle:线条类型,``'-'``    solid line;``'--'``   dashed line;``'-.'``   dash-dot line;``':'``    dotted line
linewidth:线条粗细(接数字)
alpha:透明度
"""
plt.plot(age,p1,label='自己',color="orange",linestyle="-.",linewidth=8)
plt.plot(age,p2,label='同桌',color="cyan",linestyle=":")

# 4.设置刻度
_xtick_labels = ["{}岁".format(i) for i in age]
plt.xticks(age,_xtick_labels,fontproperties=myfont)
plt.yticks(range(0,9))


plt.title('两个人11到31岁,每一年交女朋友的数量',fontproperties=myfont)  # fontproperties没有提示的

# 绘制网格
plt.grid()

# 绘制网格颜色的深度(也可以使用linestyle参数)
plt.grid(alpha=0.1)

# 添加图例,需要再plot的时候添加label参数,注意,这里要显示中文,参数不是fontproperties,是prop
# plt.legend(prop=myfont)
plt.legend(prop=myfont,loc="upper left")# 设置图例的位置,添加loc的参数

# 6.显示图片
plt.show()