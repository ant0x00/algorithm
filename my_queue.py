# encoding:utf8
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [None] * k
        self.maxsize = k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.maxsize
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        self.head = (self.head + 1) % self.maxsize
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return ((self.tail + 1) % self.maxsize) == self.head


# Your MyCircularQueue object will be instantiated and called as such:
circularQueue = MyCircularQueue(3)  # 设置长度为 3

circularQueue.enQueue(1)  # 返回 true
print(circularQueue.Front())
print(circularQueue.Rear())
circularQueue.enQueue(2)  # 返回 true

circularQueue.enQueue(3)  # 返回 true

circularQueue.enQueue(4)  # 返回 false，队列已满
print(circularQueue.Front())
print(circularQueue.Rear())
circularQueue.Rear()  # 返回 3

circularQueue.isFull()  # 返回 true

circularQueue.deQueue()  # // 返回 true

circularQueue.enQueue(4)  # // 返回 true

circularQueue.Rear()  # // 返回 4
