"""
pandas安装:
pip install pandas
pandas常用的数据类型:
1.Series一维,带标签数组
2.DateFrame二维,Series容器
"""
import pandas as pd


p1 = pd.Series([1,2,31,12,3,4])
# print(type(p1))  # <class 'pandas.core.series.Series'>
# print(p1)
"""
结果:第一列,标签索引.第二列,值
(默认索引为数字)
0     1
1     2
2    31
3    12
4     3
5     4
dtype: int64
"""

# 指定索引
p2 = pd.Series([1,23,2,2,1],index=list('abcde'))
# print(p2)
"""
结果:第一列,标签索引.第二列,值
(使用自定义索引)
a     1
b    23
c     2
d     2
e     1
dtype: int64
"""

# 通过字典创建一维数组
man = {'name':'chainrain','age':30,'phone':10087}
p3 = pd.Series(man)
# print(p3)
# print(p3.dtype)  # dtype('O')
"""
结果:键为索引,值为值,类型也变成了object
age             30
name     chainrain
phone        10087
dtype: object
"""

# 修改类型
p4 = p2.astype(float)
# print(p4)

# 通过索引查找,如果没找到返回NaN
print(p3['age'])
# 也能通过定位查找
print(p3[1])
# 查找前两个
print(p3[:2])
# 查找不连续的两个
print(p3[[1,2]])
print(p3[['name','phone']])

# 大于
print(p1[p1>10])

# index属性
print(p3.index)
print(type(p3.index))  # <class 'pandas.core.indexes.base.Index'>
for i in p3.index:
    print(i)
    """
    结果:得到索引
    age
    name
    phone
    """
# 索引转列表取前两个
print(list(p3.index)[:2])

# values属性
print(p3.values)
print(type(p3.values))  # <class 'numpy.ndarray'>

p5 = pd.Series(range(5))
p5.where(p5>0)
print(p5)

print(p5.mask(p5>0))
"""
结果:
0    0.0
1    NaN
2    NaN
3    NaN
4    NaN
dtype: float64
"""

print(p5.where(p5>1,10))
"""
结果:小于1的索引,值替换为10
0    10
1    10
2     2
3     3
4     4
dtype: int64
"""