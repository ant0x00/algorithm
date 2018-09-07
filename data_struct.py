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


if __name__ == "__main__":
    # stack_deque()
    # test_queue()
    quick_queue()
