"""
双端队列
双端队列（deque，全名double-ended queue），是一种具有队列和栈的性质的数据结构。

双端队列中的元素可以从两端弹出，其限定插入和删除操作在表的两端进行。双端队列可以在队列任意一端入队和出队。

Deque() 创建一个空的双端队列
add_front(item) 从队头加入一个item元素
add_rear(item) 从队尾加入一个item元素
remove_front() 从队头删除一个item元素
remove_rear() 从队尾删除一个item元素
is_empty() 判断双端队列是否为空
size() 返回队列的大小
"""


class DoubleQueue():
    def __init__(self):
        self.__item = []

    def size(self):
        """队列的长度"""
        return len(self.__item)

    def is_empty(self):
        """用队列长度判断队列是否为空"""
        return not self.size()

    def add_front(self,data):
        """在队列头部添加元素"""
        self.__item.insert(0,data)

    def add_end(self,data):
        """在队列尾部添加元素"""
        self.__item.append(data)

    def pop_front(self):
        """从头部删除元素"""
        return self.__item.pop(0)

    def pop_rear(self):
        """从尾部删除元素"""
        return self.__item.pop()

    def print(self):
        return self.__item

if __name__ == '__main__':
    double_queue = DoubleQueue()

    # 队列添加头部
    double_queue.add_front(1)
    double_queue.add_front(2)

    # 队列添加尾部
    double_queue.add_end(3)
    double_queue.add_end(4)

    # 删除队列头部
    print(double_queue.pop_front())
    print(double_queue.pop_front())

    # 删除队列尾部
    print(double_queue.pop_rear())
    print(double_queue.pop_rear())

    # 队列长度
    print(double_queue.size())

    # 队列是否为空,True为空,False为非空
    print(double_queue.is_empty())

    # 队列所有元素(列表)
    print(double_queue.print())