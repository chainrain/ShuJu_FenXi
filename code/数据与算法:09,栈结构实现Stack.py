"""
栈结构实现
栈可以用顺序表实现，也可以用链表实现。

栈的操作
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
"""


class Stack(object):
    def __init__(self):
        self.__item = []

    def push(self,data):
        """添加一个新的元素item到栈顶"""
        self.__item.append(data)

    def pop(self):
        """弹出栈顶元素"""
        return self.__item.pop()

    def peak(self):
        """返回栈顶元素"""
        return self.__item[len(self.__item)-1]

    def size(self):
        """返回栈的元素个数"""
        return len(self.__item)

    def is_empty(self):
        """判断栈是否为空"""
        return not self.size()

    def print(self):
        """打印栈的元素"""
        return self.__item




if __name__ == '__main__':
    stack = Stack()

    # 添加栈的元素
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # 删除栈的元素(最后一个)
    print(stack.pop())

    # 栈的长度
    print(stack.size())

    # 栈是否为空
    print(stack.is_empty())

    # 栈的所有元素(列表)
    print(stack.print())

    # 栈顶的元素(列表的最后一个)
    print(stack.peak())
