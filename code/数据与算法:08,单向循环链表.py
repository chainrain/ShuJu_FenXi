"""
单向链表的特征:
    节点:这个和单向链表不同,单向链表尾部是None,而循环链表把尾部重新引用到头部,实现了一个循环
    尾节点的向后引用为头部
"""


class Node(object):
    """节点"""

    def __init__(self, data):
        self.data = data
        self.next = None


class SinCycLinkedlist(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """链表是否为空"""
        return not self.__head

    def add(self, node_data):
        """链表头部添加元素"""
        node = Node(node_data)

        if self.is_empty():
            self.__head = node
            # 保证首尾相连
            self.__head.next = self.__head
            return

        cur = self.__head

        # 当前节点不是尾部节点的时候，往后偏移
        while cur.next != self.__head:
            cur = cur.next

        # cur指向的就是尾部节点
        node.next = self.__head
        self.__head = node
        cur.next = self.__head  # node

    def show(self):
        """遍历整个链表"""
        if self.is_empty():
            return

        cur = self.__head

        # 当前节点不是尾部节点的时候，往后偏移
        while cur.next != self.__head:
            print(cur.data, end=' --> ')
            cur = cur.next

        # cur指向的就是尾部节点
        print(cur.data)

    def append(self, node_data):
        """链表尾部添加元素"""
        node = Node(node_data)

        if self.is_empty():
            self.add(data)
            return

        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next

        # cur就是尾部节点
        cur.next = node
        node.next = self.__head

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0

        cur = self.__head
        count = 0
        while cur.next != self.__head:
            count += 1
            cur = cur.next

        count += 1
        return count

    def search(self, node_data):
        """查找节点是否存在"""
        if self.is_empty():
            return False

        cur = self.__head
        while cur.next != self.__head:

            if cur.data == node_data:
                return True

            cur = cur.next

        if cur.data == node_data:
            return True

        return False

    def remove(self, node_data):
        """删除节点"""
        if self.is_empty():
            return

        cur = self.__head
        pre = None

        while cur.next != self.__head:

            if cur.data == node_data:
                # 当前节点cur就是要删除的节点
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next

                    # rear指向的就是尾部节点
                    self.__head = self.__head.next
                    rear.next = self.__head
                    return

                pre.next = cur.next
                return

            pre = cur
            cur = cur.next

        # cur指向的是尾部节点
        if cur.data == node_data:
            # 尾部节点就是要删除的节点
            if cur == self.__head:
                self.__head = None
                return
            pre.next = cur.next  # self.__head
            return

    def insert(self, index, node_data):
        """index位置添加元素"""
        if index <= 0:
            self.add(node_data)
            return
        if index > self.length() - 1:
            self.append(node_data)
            return

        node = Node(node_data)
        cur = self.__head
        for i in range(index - 1):
            cur = cur.next

        # cur指向的就是index-1
        node.next = cur.next
        cur.next = node


if __name__ == "__main__":
    s = SinCycLinkedlist()
    s.add(1)
    s.add(2)
    s.add(3)

    s.show()

    s.append(999)
    s.show()
    print("length: ", s.length())
    print("search: ", s.search(3))

    s.insert(index=1, node_data=888)
    s.show()

    # s.remove(1)
    # s.show()
