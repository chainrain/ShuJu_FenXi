"""
快速排序
快速排序（英语：Quicksort），又称划分交换排序（partition-exchange sort），
通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

步骤为：
从数列中挑出一个元素，称为"基准"（pivot），
重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。
虽然一直递归下去，但是这个算法总会结束，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。
"""
import time

start_time = time.time()

l = [54, 26, 17, 31, 44, 55, 20]


# 递归
def merge_sort(alist):
    if len(alist) == 1:
        return alist

    n = len(alist)

    left_list = merge_sort(alist[:n//2])
    right_list = merge_sort(alist[n//2:])


    return merge(left_list, right_list)


# 合并
def merge(left_list, right_list):
    new_list = []

    l_index, r_index = 0, 0

    while l_index < len(left_list) and r_index < len(right_list):
        # if l_index > len(left_list)-1 or r_index > len(right_list)-1:
        #     break

        if left_list[l_index] < right_list[r_index]:
            new_list.append(left_list[l_index])
            l_index += 1
        else:
            new_list.append(right_list[r_index])
            r_index += 1


    new_list += left_list[l_index:]
    new_list += right_list[r_index:]


    return new_list



print(merge_sort(l))
end_time = time.time()
print('程序运行时间:', end_time - start_time)

"""
总结:
时间复杂度
最优时间复杂度：O(nlogn)
最坏时间复杂度：O(nlogn)
稳定性：稳定
"""
