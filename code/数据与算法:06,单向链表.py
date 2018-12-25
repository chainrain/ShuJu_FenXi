"""
单向链表的特征:
    节点:有两个域,数据域和引用域
    每一组数据节点都有尾部节点next,最后一个数据的next为空
    每个数据节点只有一个向后的引用
"""


class Node(object):
    """节点"""
    def __init__(self, data):
        # 数据域
        self.data = data
        # 引用域
        self.next = None


class SingleLinkList(object):
    """单向链表"""
    def __init__(self):
        # 私有属性
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        if self.__head == None:
            return True  # 如果空,返回True
        else:
            return False  # 如果不是空,返回False

    def add(self,data):
        """链表头部添加元素,add(数据)把数据传递给Node生成节点,然后这个节点插入到头部节点,前面的节点顺位退一位"""
        node = Node(data)
        # 之前的头节点变成头节点的下一个节点
        node.next = self.__head
        # 这个节点为头节点
        self.__head = node

    def append(self,data):
        """链表尾部追加节点"""
        # 拿到当前头部节点
        cur = self.__head
        # 判断.如果链表为空,链表在头部添加数据
        if s.is_empty():
            s.add(data)
        # 循环.如果cur的下一个节点不是None(尾部节点)的时候,cur变成当前节点的下一个节点继续循环
        while cur.next != None:
            cur = cur.next
        node = Node(data)
        # cur指向的就是尾部节点
        cur.next = node

    def show(self):
        """遍历整个链表"""
        # 拿到当前头部节点
        cur = self.__head
        # 循环.如果这个节点不为None,输出节点的数据,cur变成当前节点的下一个节点继续循环
        while cur != None:
            print(cur.data,end='--> ')
            cur = cur.next

    def length(self):
        """链表的长度"""
        # 拿到当前头部节点
        cur = self.__head
        count = 0
        # 循环.如果节点不为None,数量加一,cur变成当前节点的下一个节点继续循环
        while cur != None:
            count += 1
            cur = cur.next
        print(' ')  # 为了好看点而已,没什么实际作用
        return count

    def search(self,node_data):
        """搜索链表的某个节点,方法是在运行search函数的时候传入一个节点的数据,然后验证它是否存在"""
        cur = self.__head
        # 循环.首先判断节点是否是None(最后一个节点),然后如果传入的这个值和节点数据能对的上,输出;否则输出'没有这个节点'
        while cur != None:
            if cur.data == node_data:
                return '有%s的节点' % cur.data
            cur = cur.next
        return '没有这个节点'

        # 不用while循环这种也行
        # if cur.data == node_data:
        #     return '有%s的节点' % cur.data
        # else:
        #     return '没有这个节点'

    def remove(self,node_data):
        """删除某个节点,方法是在运行remove函数的时候传入需要删除的节点的数据,然后删除它"""
        cur = self.__head
        pre = None

        # 循环.首先去掉尾部节点循环
        while cur != None:
            # 如果节点数据等于传入数据,进入下一个判断
            if cur.data == node_data:
                # 如果节点是开头
                if cur == self.__head:
                    # 那么开头的重新指向之前的开头的下一位(也就是把下一位移动回开头)
                    self.__head = self.__head.next
                    return
                # 那么当前节点的下一个为前置节点的下一个(剔除当前节点位,其他补位)
                pre.next = cur.next
                return
            # pre是cur的前置节点
            pre = cur
            cur = cur.next

    def insert(self,index,node_data):
        """在指定位置插入节点"""
        # 使用写好都add方法,在头部插入节点
        if index <= 0:
            s.add(data=node_data)
            return
        # 使用写好的append方法,在尾部插入节点
        if index > s.length() - 1:
            s.append(data=node_data)
            return
        cur = self.__head
        # 得出所有的节点的下一个值cur.next
        for i in range(index-1):
            cur = cur.next

        node = Node(data=node_data)
        node.next = cur.next
        cur.next = node

if __name__ == '__main__':
    s = SingleLinkList()

    print('is empty: ',s.is_empty())

    s.add(1)
    s.add(2)
    s.add(3)
    # s.append(10)
    s.show()  # 结果: 3--> 2--> 1-->   总结,最后添加的节点为头节点

    print('length: ',s.length())
    print('search: ',s.search(5))

    s.remove(3)
    s.show()

    s.insert(index=1,node_data=333)
    s.show()