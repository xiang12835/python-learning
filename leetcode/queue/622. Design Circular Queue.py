# coding=utf-8

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k + 1 # 因为循环队列需要空一个
        self.front = 0
        self.rear = 0
        self.queue = [0 for _ in range(k+1)]

    def enQueue(self, value: int) -> bool:
        """队尾添加元素：注意不满的时候才能添加"""
        if self.isFull():
            return False
        else:
            self.rear = (self.rear+1) % self.size
            self.queue[self.rear] = value
            return True

    def deQueue(self) -> bool:
        """队头删除元素：注意非空的时候才能删除"""
        if not self.isEmpty():
            self.front = (self.front+1) % self.size
            return True
        else:
            return False

    def Front(self) -> int:
        """返回头部所指的元素：注意是下一个，因为有一个一直空着"""
        if self.isEmpty():
            return -1
        else:
            return self.queue[(self.front+1) % self.size]

    def Rear(self) -> int:
        """返回队尾所指元素：直接返回所指的就行"""
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear]

    def isEmpty(self) -> bool:
        """判断队空:队空的条件是头尾相接"""
        return self.rear == self.front

    def isFull(self) -> bool:
        """判断队满：注意队满的是队首和队尾之间空着一个"""
        return (self.rear+1) % self.size == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()