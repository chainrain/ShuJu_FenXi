"""
插入排序
插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
"""
import time

start_time = time.time()

l = [54, 26, 17, 31, 44, 55, 20]


def pop_sort(alist):
    n = len(alist)

    for i in range(n - 1):
        count = 0
        for j in range(n - 1 - i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                count += 1
            if count == 0:
                break


pop_sort(l)
print(l)
end_time = time.time()
print('程序运行时间:', end_time - start_time)

"""
总结:
时间复杂度
最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
最坏时间复杂度：O(n2)
稳定性：稳定
"""
