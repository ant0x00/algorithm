# encoding:utf-8


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


def test_stack():
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


def stack_deque():
    import collections
    stack = collections.deque()
    print(len(stack))
    stack.append("first in")
    print(stack[-1])
    stack.append("second in")
    print(stack[-1])
    print(len(stack))
    print(stack.pop())


class Queue:
    """模拟队列"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):  # 进队
        self.items.insert(0, item)

    def dequeue(self):  # 出队
        return self.items.pop()

    def size(self):
        return len(self.items)


def test_queue():
    q = Queue()
    print(q.is_empty())
    q.enqueue('dog')
    q.enqueue(4)
    print(q)
    q = Queue()
    print(q.is_empty())
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)


def quick_queue():
    from collections import deque
    queue = deque(["Eric", "John", "Michael"])
    print(queue)
    queue.append("Terry")  # Terry arrives
    print(queue)
    queue.append("Graham")  # Graham arrives
    print(queue)
    queue.popleft()  # The first to arrive now leaves
    print(queue)
    queue.popleft()  # The second to arrive now leaves
    print(queue)
    queue.insert(2,'wanglong')
    print(queue)


class Node(object):
    """
        # 链表
        - 单向链表
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


def test_node():
    task_list = Node('first')
    print(task_list.getData())
    print(type(task_list))
    task_list.setNext(Node('second'))
    print(task_list.next.getData())

class LinkedList():
    def __init__(self):
        self.length = 0
        self.head = None
    #判断链表是否为空
    def is_empty(self):
        return self.length == 0
    #插入节点this_node
    def append(self, this_node):
        if isinstance(this_node, Node):
            pass
        else:
            this_node = Node(this_node)
        if self.is_empty():
            self.head = this_node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = this_node
        self.length+=1
    #在第index处插入节点this_node
    def insert(self, this_node, index):
        if index > self.length:
            return 'Error'
        if isinstance(this_node, Node):
            pass
        else:
            this_node = Node(this_node)
        if index == 0:
            this_node.next = self.head
            self.head = this_node
        else:
            p = self.head
            while index-1:
                p = p.next
                index-=1
            this_node.next = p.next
            p.next = this_node
        self.length+=1
    #删除第index个节点
    def delete(self, index):
        if not 0<= index < self.length:
            return 'Error'
        if index == 0:
            self.head = self.head.next
        else:
            p = self.head
            while index-1:
                p = p.next
                index-=1
            p.next = p.next.next
        self.length-=1
    #更新第index节点的值
    def update(self, data, index):
        if not 0<= index < self.length:
            return 'Error'
        if index == 0:
            self.head.data = data
        else:
            p = self.head
            while index:
                p = p.next
                index-=1
            p.data = data
    #获取第index节点的值
    def get_data(self, index):
        if not 0<= index < self.length:
            return 'Error'
        if index == 0:
            return self.head.data
        else:
            p = self.head
            while index:
                p = p.next
                index-=1
            return p.data
    #获取链表长度
    def get_length(self):
        return self.length
    #清空链表
    def clear(self):
        self.head = None
        self.length = 0
    #打印链表
    def PrintList(self):
        if self.length ==0:
            return None
        else:
            p = self.head
            while p.next:
                print(p.data,'-->',end = '')
                p = p.next
            print(p.data)


if __name__ == "__main__":
    # stack_deque()
    # test_queue()
    # quick_queue()
    test_node()
