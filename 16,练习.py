import numpy

# t1 = numpy.arange(12).reshape((3, 4)).astype('float')
# # print(t1)
#
# t1[1, 2:] = numpy.nan
# print(t1)

def fill_ndarray(t1):
    for i in range(t1.shape[1]):  # 一共多少列
        # print(i)
        temp_col = t1[:, i]  # 得出每一列
        print(temp_col)
        nan_num = numpy.count_nonzero(temp_col != temp_col)  # 得出nan的数量
        # print(nan_num)
        if nan_num != 0:  # 说明当前列有nan值
            temp_not_nan_col = temp_col[temp_col == temp_col]  # temp_col[temp_col == temp_col],判断当前列除了nan以外的数值(因为nan是不等的)
            # print(temp_not_nan_col)
            temp_col[numpy.isnan(temp_col)] = temp_not_nan_col.mean()  # 求平均值
    return t1

if __name__ == '__main__':
    t1 = numpy.arange(12).reshape((3,4)).astype('float')  # 生成数组
    t1[1,2:] = numpy.nan  # 数组替换某个为nan方便测试
    print(t1)
    t1 = fill_ndarray(t1)  # 使用方法,替换nan
    print(t1)