def test1():
    """追加列表"""
    l = []
    for i in range(1000):
        l.append(i)


def test2():
    """插入列表"""
    l = []
    for i in range(1000):
        l.insert(0, i)


def test3():
    """列表相加"""
    l = []
    for i in range(1000):
        l += [i]


def test4():
    """列表生成式"""
    l = [x for x in range(1000)]


def test5():
    """列表类型转换"""
    l = list(range(1000))

from timeit import Timer
#
# # Timer方法可以运行函数,其中timeit的方法可以多次调用函数
# t1 = Timer('test1()','from __main__ import test1')
# print('尾部追加',t1.timeit(number=10000))  # number=调用的次数
# t2 = Timer('test2()','from __main__ import test2')
# print('头部插入',t2.timeit(number=10000))
# t3 = Timer('test3()','from __main__ import test3')
# print('列表相加',t3.timeit(number=10000))
# t4 = Timer('test4()','from __main__ import test4')
# print('列表生成式',t4.timeit(number=10000))
# t5 = Timer('test5()','from __main__ import test5')
# print('强制类型转换',t5.timeit(number=10000))



"""
结果:
尾部追加 1.778462713999943
头部插入 4.3479886020004415
列表相加 1.9892594240000108
列表生成式 0.879036119000375
强制类型转换 0.29277422099949035

总结:强制类型转换最快.....
"""



x = list(range(2000000))
pop_zero = Timer("x.pop(20000)","from __main__ import x")
print("删除某个值 ",pop_zero.timeit(number=1000))
x = list(range(2000000))
pop_end = Timer("x.pop()","from __main__ import x")
print("删除尾部 ",pop_end.timeit(number=1000))

"""
结果:
删除0  2.2723999949994322
删除尾部  0.00018832500063581392

总结:
如果删除要删除某个值,那么就会慢点.(速度要要看这个值在列表的哪个位置,越靠后,速度越慢)
如果是正常删除(删除尾部),那么会快很多
"""