# 这里没有本地的数据文件,所以只写过程
import numpy

# # 文件路径
# file_path = "./"
#
#
# """
# loadtxt有以下常用参数:
# fname读取的文件名;
# delimiter以','分割;
# dtype转换的数据类型(默认为float);
# unpack如果是True,读取属性将分别写入不通过不同数组变量,False读入数据只写入一个数组变量,默认为False
# """
# t1 = numpy.loadtxt(fname=file_path,delimiter=',',dtype='int',unpack=True)
#
# print(t1)
#
# # 取行
# print(t1[2])
#
# # 连续取多行
# print(t1[2:])
#
# # 取不连续的多行
# print(t1[2,8,10])
#
# # 取列
# print(t1[:,0])
#
# # 取连续的多列
# print(t1[:,2:])
#
# # 取不连续多列,取第一列和第三列
# print(t1[:,[0,2]])
#
# # 取多行多列,取第三行,第四列的值(因为从0开始,所以2,3是3行4列),这里是numpy.int64类型
# print(t1[2,3])
#
# # 取多行多列,取第三行到第五行,第二列到第四列的结果,得出的数值是交叉点的数值
# print(t1[2:5,1:4])
#
# # 取多个不相邻的点
# # [[0,2],[0,1]]的意思是:取0,0的数(1行1列),和2,1的数(3行2列)
# print(t1[[0,2],[0,1]])

# t2数组里面小于10的数,替换成0
t2 = numpy.arange(24).reshape(4,6)
print(t2)
t2[t2<10] = 0
print(t2)

# t1数组里面小于3的替换成100,其他替换成300
t1 = numpy.arange(24).reshape(4,6)
print(numpy.where(t1 < 3, '100', '300'))

# 小于10的替换为10,大于18的替换为18
t3 = t1.clip(10,18)
print(t3)