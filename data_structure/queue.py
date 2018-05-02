# coding=utf-8

# 队列的实现
class Queue():
    def __init__(qu, size):
        qu.queue = []
        qu.size = size
        qu.front = -1
        qu.rear = -1

    def empty(qu):
        if qu.front == qu.rear:
            return True
        else:
            return False

    def full(qu):
        if qu.rear - qu.front + 1 == qu.size:
            return True
        else:
            return False

    def enQueue(qu, data):
        if qu.full():
            print "Queue is full"
        else:
            qu.queue.append(data)
            qu.rear += 1

    def outQueue(qu):
        if qu.empty():
            print("Queue is empty")
        else:
            qu.front -= 1


""" 双向队列

双向队列，头部或尾部插入或删除一个元素，只需要消耗常数级别的时间
而list，而从list头部插入或删除一个元素，只需要消耗线性级别的时间，比较慢
从list尾部插入或删除一个元素，只需要消耗常数级别的时间

"""
from collections import deque

fifo = deque()
fifo.append(1)
print fifo
fifo.popleft()
print fifo


""" 优先级队列（堆队列）

堆操作所消耗的时间，与列表长度的对数成正比

"""
from heapq import heappush, heappop, nsmallest

a = []

heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)

print a
print nsmallest(1, a)
assert a[0] == nsmallest(1, a)[0] == 3

print heappop(a), heappop(a), heappop(a), heappop(a)
print a

