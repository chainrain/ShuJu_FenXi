import numpy
t1 = numpy.arange(12).reshape(2,6)
# print(t1)

t2 = numpy.arange(12,24).reshape(2,6)
# print(t2)

# 竖直拼接
t3 = numpy.vstack((t1,t2))
print(t3)

# 水平拼接
t4 = numpy.hstack((t1,t2))
# print(t4)

# 行交换
t3[[0,1],:] = t3[[1,0],:]
# print(t3)

# 列交换
t3[:,[0,1]] = t3[:,[1,0]]
print(t3)