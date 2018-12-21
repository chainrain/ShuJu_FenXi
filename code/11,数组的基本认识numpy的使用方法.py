import numpy as np
import random

# 使用numpy生成数组
t1 = np.array([1,2,3])
print(t1)
print(type(t1))

# 使用numpy生成数组
t2 = np.array(range(10))
print(t2)  # 结果 [0 1 2 3 4 5 6 7 8 9]

# 使用numpy生成数组
t3 = np.arange(10)
print(t3)  # 结果 [0 1 2 3 4 5 6 7 8 9]
# 结论,array和arange两个方法都一样

# 4到10,隔两个数输出
t4 = np.arange(4,10,2)
print(t4)  # [4 6 8]

# 数据类型int64,numpy生成数组默认是这种类型int+64位的系统,就是int64
print(t4.dtype)

# 指定数组类型
t5 = np.array(range(1,4),dtype=float)
t5 = np.array(range(1,4),dtype='float32')
t5 = np.array(range(1,4),dtype='i1')  # i1是int8类型
print(t5)
print(t5.dtype)

# 指定为布尔类型
t6 = np.array([1,1,0,1,0,0],dtype=bool)
print(t6)  # [ True  True False  True False False]
print(t6.dtype)

# t7为t6调整为int8类型
t7 = t6.astype('int8')
print(t7)
print(t7.dtype)

# numpy中的小数
t8 = np.array([random.random() for i in range(10)])
print(t8)
print(t8.dtype)

# numpy的round方法,取小数的多少位
"""
随机3位小数的小技巧
一:
round = round(random.random(),3)
print(round)
二:
round = '%.3f'%random.random()
print(round)
"""
t9 = np.round(t8,2)
print(t9)
print(t9.dtype)