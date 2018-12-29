"""
选择排序
选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。

选择排序的主要优点与数据移动有关。
如果某个元素位于正确的最终位置上，则它不会被移动。
选择排序每次交换一对元素，它们当中至少有一个将被移到其最终位置上，因此对n个元素的表进行排序总共进行至多n-1次交换。
在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种。
"""
import time

start_time = time.time()

l = [54, 26, 17, 31, 44, 55, 20]

def choose_sort(alist):
    n = len(alist)

    for i in range(n - 1):
        min_index = i

        for j in range(i+1,n):
            if alist[min_index] > alist[j]:
                min_index = j

        alist[min_index],alist[i] = alist[i],alist[min_index]


choose_sort(l)
print(l)

end_time = time.time()
print('程序运行时间:',end_time-start_time)

"""
总结:
时间复杂度
最优时间复杂度：O(n2)
最坏时间复杂度：O(n2)
稳定性：不稳定（考虑升序每次选择最大的情况）
"""