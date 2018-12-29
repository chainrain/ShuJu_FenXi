"""
队列的概述
队列（queue）是只允许在一端进行插入操作，而在另一端进行删除操作的线性表。

队列是一种先进先出的（First In First Out）的线性表，简称FIFO。
允许插入的一端为队尾，允许删除的一端为队头。队列不允许在中间部位进行操作！
假设队列是q=（a1，a2，……，an），那么a1就是队头元素，而an是队尾元素。这样我们就可以删除时，总是从a1开始，而插入时，总是在队列最后。
这也比较符合我们通常生活中的习惯，排在第一个的优先出列，最后来的当然排在队伍最后。



队列的实现
同栈一样，队列也可以用顺序表或者链表实现。

操作
Queue() 创建一个空的队列
put_queue(data) 往队列中添加一个data元素
pop_queue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
"""


class Queue(object):
    def __init__(self):
        self.__item = []

    def put_queue1(self,data):
        """往队列中添加一个元素,追加"""
        self.__item.append(data)

    def put_queue2(self,data):
        """往队列添加一个元素,在头部插入"""
        self.__item.insert(0,data)

    def pop_queue1(self):
        """pop0,删除第一个元素"""
        return self.__item.pop(0)

    def pop_queue2(self):
        """pop,删除尾部元素"""
        return self.__item.pop()

    def size(self):
        """队列的长度"""
        return len(self.__item)

    def is_empty(self):
        """用队列的长度判断队列是否为空"""
        return not self.size()

    def print(self):
        return self.__item

if __name__ == '__main__':
    queue = Queue()

    # 队列追加元素
    # queue.put_queue1(1)
    # queue.put_queue1(2)
    # queue.put_queue1(3)

    # 队列头部添加元素
    queue.put_queue2(1)
    queue.put_queue2(2)
    queue.put_queue2(3)

    # 队列删除第一个元素
    # queue.pop_queue1()

    # 队列删除尾部元素
    queue.pop_queue2()

    # 队列长度
    print(queue.size())

    # 队列所有元素(列表),True为空,False为非空
    print(queue.print())

    # 队列是否为空
    print(queue.is_empty())