# encoding:utf-8


class Node(object):
    """
        # 链表
        - 单项链表
        -
    """

    def __init__(self, initdata):
        self.data = initdata
        # 引用None代表没有下一节点
        self.next = None

    # 获得数据
    def getData(self):
        return self.data

    # 获得下一个节点的引用
    def getNext(self):
        return self.next

    # 修改数据
    def setData(self, newdata):
        self.data = newdata

    # 修改下一节点的引用
    def setNext(self, newnext):
        self.next = newnext


class Stack:
    """
    #栈
    -
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    s = Stack()
    print(s.isEmpty())
    s.push("第一个元素")
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())