import pandas as pd
import numpy as np

p1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(p1)
"""
numpy创建三行四列的数组原本是这样的
0  1   2   3
4  5   6   7
8  9  10  11
用DataFrame创建二维数组是这样的
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
总结:在行和列都标示了索引
"""

p2 = pd.DataFrame(np.arange(12).reshape(3,4),index=list('bac'),columns=list("wxyz"))
print(p2)
"""
自定义行索引和列索引
   w  x   y   z
b  0  1   2   3
a  4  5   6   7
c  8  9  10  11
"""

peoples = {'name':['chainrain1','chainrain2'],'phone':[10086,10098],'age':[1,12]}
p3 = pd.DataFrame(peoples)
print(p3)
print(type(p3))
"""
多维数组,结果: 字典的键为列名,字典的值为里面的数据
   age        name  phone
0    1  chainrain1  10086
1   12  chainrain2  10098
<class 'pandas.core.frame.DataFrame'>
"""

peoples2 = [{'name':'chainrain','phone':10010,'age':1},
            {'name':'chainrain2','phone':10016},
            {'name':'chainrain3','age':19}]
p4 = pd.DataFrame(peoples2)
print(p4)
print(type(p4))
"""
多维数组,结果: 字典的键为列名,字典的值为里面的数据,如果没有值的话就显示NaN
    age        name    phone
0   1.0   chainrain  10010.0
1   NaN  chainrain2  10016.0
2  19.0  chainrain3      NaN
<class 'pandas.core.frame.DataFrame'>
"""

print(p4.index)  # RangeIndex(start=0, stop=3, step=1),行索引
print(p4.columns)  # Index(['age', 'name', 'phone'], dtype='object'),列索引
print(p4.values)
"""
值
[[1.0 'chainrain' 10010.0]
 [nan 'chainrain2' 10016.0]
 [19.0 'chainrain3' nan]]
 """
print(p4.shape)  # (3, 3),数组结构
print(p4.dtypes)
"""
每一个字段的类型
age      float64
name      object
phone    float64
dtype: object
"""
print(p4.ndim)  # 数据维度
print(p4.head(1))  # 显示前几行,不赋值默认前五行
print(p4.tail(2))  # 显示后几行
print(p4.info())  # 相关信息概览
print(p4.describe())
"""
快速统计综合结果
             age         phone
count   2.000000      2.000000
mean   10.000000  10013.000000
std    12.727922      4.242641
min     1.000000  10010.000000
25%     5.500000  10011.500000
50%    10.000000  10013.000000
75%    14.500000  10014.500000
max    19.000000  10016.000000
"""

# 定位行号为1的phone
print(p4.loc[1,'phone'])

print(p4.loc[1])
"""
拿到1行的数据
age             NaN
name     chainrain2
phone         10016
Name: 1, dtype: object
"""

# 拿到所有phone
print(p4.loc[:,'phone'])

print(pd.isnull(p4))
"""
如果为NaN的为True
     age   name  phone
0  False  False  False
1   True  False  False
2  False  False   True
"""

# 如果有NaN的行,删除
print(p4.dropna(axis=0,how='any'))
# 没做什么事情
print(p4.dropna(axis=0,how='all'))

# inplace重新赋值
# p4.dropna(axis=0,how='any',inplace=True)
# print(p4)

# 填充NaN为0
print(p4.fillna(0))

# 取平均值填充
print(p4.fillna(p4.mean()))

# 只填充age
# p4['age'] = p4['age'].fillna(p4['age'].mean())
# print(p4)
