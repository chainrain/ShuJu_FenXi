# 这里没有本地的数据文件,所以只写过程
import numpy

# 文件路径
file_path = "./"


"""
loadtxt有以下常用参数:
fname读取的文件名;
delimiter以','分割;
dtype转换的数据类型(默认为float);
unpack如果是True,读取属性将分别写入不通过不同数组变量,False读入数据只写入一个数组变量,默认为False
"""
t1 = numpy.loadtxt(fname=file_path,delimiter=',',dtype='int',unpack=True)

print(t1)