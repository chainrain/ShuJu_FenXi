import time

start_time = time.time()

l = [54, 26, 17, 31, 44, 55, 20]

l.sort()
print(l)

end_time = time.time()
print('程序运行时间:',end_time-start_time)

"""
总结:不是稳定的,幅度挺大的
"""