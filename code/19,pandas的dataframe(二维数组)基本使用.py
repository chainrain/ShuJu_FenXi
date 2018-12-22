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