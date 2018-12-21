import numpy

# 生成1的数组
t1 = numpy.ones((2,3))
# print(t1)

# 生成0的数组
t2 = numpy.zeros((3,4))
# print(t2)

# 生成数据方列
t3 = numpy.eye(4)
# print(t3)

# 每一行的最大值的位置
# print(numpy.argmax(t3, axis=0))  # axis表示每一行的最大值 [0 1 2 3]

# 数据转换,1转为-1
t3[t3==1] = -1
# print(t3)

# 取每一行的最小值
# print(numpy.argmin(t3, axis=1))

# 随机生成4行5列的 10到20的数
# numpy.random.seed(0)  # 如果添加了一个随机种子,那么随机的数值将不改变
t4 = numpy.random.randint(10,20,(4,5))
# print(t4)

# 转成nan数值
t3[3,3] = numpy.nan
# print(t3)

# 统计不为0的个数
# print(numpy.count_nonzero(t3))

# 在nan的位置,为不等于true,其他为等于false
# print(t3 != t3)  # 方法1
# print(numpy.isnan(t3))  # 方法2

# 统计不等于的数量
# print(numpy.count_nonzero(t3 != t3))   # 方法1
# print(numpy.count_nonzero(numpy.isnan(t3)))   # 方法2

t5 = numpy.arange(12).reshape((3,4))
print(t5)
# 求和
print(numpy.sum(t5))
# axis=0求每一列的和 [12 15 18 21]
print(numpy.sum(t5,axis=0))
# axis=1求每一行的和 [ 6 22 38]
print(numpy.sum(t5,axis=1))
# 任何和nan求和的数值,结果都是nan
print(numpy.sum(t3,axis=0))
# axis=0每一列的均值
print(numpy.mean(t3,axis=0))
# 每一列的,中间值
print(numpy.median(t5,axis=0))
# 最大值
print(t5.max(axis=0))
# 最小值
print(t5.min(axis=0))
# axis=0没一列的最大值和最小值之差:极值
print(numpy.ptp(t5,axis=0))
# 标准差,越大表示越不稳定
print(numpy.std(t5,axis=0))
