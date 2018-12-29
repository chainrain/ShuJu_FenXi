import time

start_time = time.time()

l = [0, 1, 2, 8, 13, 17, 19, 32, 42]

def binary_search(alist, data):
    n = len(alist)
    if n == 0:
        return False
    mid_index = n // 2
    if alist[mid_index] == data:
        return True
    if data > alist[mid_index]:
        # 对右表进行拆分
        return binary_search(alist=alist[mid_index + 1:], data=data)
    else:
        # 对左表进行拆分
        return binary_search(alist=alist[:mid_index], data=data)


print(binary_search(alist=l, data=1))

end_time = time.time()

print("总耗时: ",end_time-start_time)