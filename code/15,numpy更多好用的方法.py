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
print(t4)