"""
双向链表的特征:
    节点:双向链表和单向链表不同,双向链表会多一个域.一个向前引用的域
    头节点的向前引用为空
    尾节点的向后引用为空
"""


class Node(object):
    """节点"""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        return not self.__head
        # 方法二:
        # if self.__head == None:
        #     return True  # 如果空,返回True
        # else:
        #     return False  # 如果不是空,返回False

    def add(self,node_data):
        """在链式表头部添加节点"""
        # 当前节点用Node类生成
        node = Node(data=node_data)
        # 判断链表是否为空
        if s.is_empty():
            self.__head = node
            return

        # 链表的头部为节点的下一个
        node.next = self.__head
        # 该节点就是列表头(就是上一个节点)的前一个,也就是None,这里目的是不改变节点的结构
        self.__head.prev = node
        # 该节点是链表的头部
        self.__head = node

    def append(self,node_data):
        """在链表里的尾部追加节点"""
        if self.is_empty():
            self.add(node_data=node_data)
            return
        cur = self.__head
        # 循环.如果cur的下一个节点不是None(尾部节点)的时候,cur变成当前节点的下一个节点继续循环
        while cur.next != None:
            cur = cur.next

        node = Node(data=node_data)
        cur.next = node
        node.prev = cur

    def show(self):
        """遍历整个链表"""
        # 拿到整个链表的头部
        cur = self.__head
        # 循环.拿出每个节点的数据,和当前节点的下一个节点的值
        while cur != None:
            print(cur.data,end='--> ')
            cur = cur.next

    def length(self):
        """统计链表长度"""
        cur = self.__head
        count = 0
        while cur != None:
            # cur是一个有效节点
            count += 1
            cur = cur.next

        return count

    def search(self, node_data):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            # cur是一个有效节点
            if cur.data == node_data:
                return True
            cur = cur.next
        return False

    def remove(self, node_data):
        """删除该节点"""
        cur = self.__head
        while cur != None:

            if cur.data == node_data:
                # 就是要删除的节点

                # 头部特殊处理
                if cur == self.__head:
                    self.__head = self.__head.next
                    # 将新的头节点的prev指向空，保证双向链表的结构特征不变
                    if self.__head:
                        self.__head.prev = None
                    return

                # 尾部特殊处理
                if cur.next == None:
                    cur.prev.next = cur.next
                    return

                cur.next.prev = cur.prev
                cur.prev.next = cur.next

            cur = cur.next


    def insert(self, index, node_data):
        """在index的位置添加节点"""
        if index <= 0:
            self.add(node_data)
            return
        if index > self.length() - 1:
            self.append(node_data)
            return
        cur = self.__head
        for i in range(index - 1):
            cur = cur.next
        # cur指向的就是index-1个
        node = Node(node_data)
        node.next = cur.next
        node.prev = cur
        cur.next.prev = node
        cur.next = node

if __name__ == '__main__':
    s = DoubleLinkList()

    print('is empty',s.is_empty())

    s.add(1)
    s.add(2)
    s.add(3)

    # s.show()
    s.append(4)
    s.show()