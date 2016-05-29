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
