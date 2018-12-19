from matplotlib import pyplot as plt


x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,27,22,18,15]

# 设置图片大小
plt.figure(figsize=(20,8),dpi=80)

# 绘图
plt.plot(x,y)

# 设置x轴的刻度
# plt.xticks(x)
_xtick_labels = [i/2 for i in range(4,49)]
plt.xticks(_xtick_labels[::4])  # 当刻度太密集的时候,使用列表步长(间隔取值),matplotlib会自动对应
# plt.xticks(range(25,50))  # 溢出范围
# 设置y轴的刻度
# plt.yticks(y)
plt.yticks(range(min(y),max(y)+1))

# 保存绘图,可以保存为svg矢量图格式,放大不会有锯齿
# plt.savefig("./test/01.png")

# 展示图形
plt.show()