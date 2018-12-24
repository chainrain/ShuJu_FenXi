
"""
先简单的使用一下算法
题目:如果a+b+c=1000,且a^2+b^2=c^2(a的平方加b的平方等于c的平方),如何求出所有的abc可能的组合
"""

# 这次,是遍历a和b,然后在使用a+b+c=1000的条件,计算出c

import time

start_time = time.time()

for a in range(1001):
    # 遍历取a的值
    for b in range(1001):
        # 遍历取b的值
        c= 1000-a-b  # 然后使用已知的a和b(因为a+b+c=1000的条件),计算出c的结果
        if a*a + b*b == c*c:
            print(a,b,c)

end_time = time.time()

print('总耗时:  ',end_time-start_time)  # 最终需要0.6秒左右(这个数值关乎CPU的算力)

"""这里运用了c = 1000-a-b,所以程序只用到了1000*1000次"""