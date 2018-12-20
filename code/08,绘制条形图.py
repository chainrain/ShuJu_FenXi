from matplotlib import pyplot as plt
from matplotlib import font_manager

"""
数据来源:http://58921.com/
"""
myfont = font_manager.FontProperties(fname="/home/python/Desktop/ShuJu_FenXi/中文字体/NotoSansCJK-Black.ttc")

# 电影名称
a = ['海王', '中国合伙人2', '印度合伙人', '网络谜踪', '无名之辈', '狗十三', '绿毛怪格林奇', '毒液：致命守护者', '午夜整容室', '照相师', '龙猫', '淡蓝琥珀']
# 当日票房(万)
b = ['72.4', '5.47', '13.79', '5.61', '5.17', '3.27', '1.49', '1.52', '0.4341', '0.3688', '17.94', '0.1222']

# 首先拼接字典
dict1 = {}
for i in range(len(a)):
    dict1[a[i]] = float(b[i])
# print(type(sorted(dict1.items(), key=lambda item: item[1])))

# dict1.items()转换为元祖,这里key参数对应的lambda表达式的意思则是选取元组中的第二个元素作为比较参数
index = sorted(dict1.items(), key=lambda item: item[1])
# print(index)

# 在把有序的数值转回列表
piaofang = []
dianying = []
for i in range(len(index)):
    # print(list(index[i]))
    # print(type(list(index[i])))
    list1 = list(index[i])
    # print(list1[1])
    # print(list1[0])
    piaofang.append(list1[1])
    dianying.append(list1[0])
# print(piaofang)
# print(dianying)

# 设定图片大小
plt.figure(figsize=(20,8),dpi=90)
# 绘条形图
plt.bar(x=range(len(a)), height=piaofang,width=0.2)
# 添加刻度
plt.xticks(range(len(a)), dianying,fontproperties=myfont,rotation=-45)
plt.yticks(range(100))
# 展示图片
plt.show()
