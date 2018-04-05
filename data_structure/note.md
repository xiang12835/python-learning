## 栈

> First-In-Last-Out

<font size=4> **1. 数组实现** </font></br>

```python
class Stack():
    def __init__(st,size):
        st.stack=[]
        st.size=size
        st.top=-1

    def empty(st):
        if st.top==-1:
            return True
        else:
            return False

    def full(st):
        if st.top==st.size:
            return True
        else:
            return False

    def push(st,data):
        if st.full():
            print "Stack is full"
        else:
            st.stack.append(data)
            st.top=st.top+1

    def pop(st):
        if st.empty():
            print "Stack is empty"
        else:
            st.top=st.top-1
```

<font size=4> **2. 链表实现** </font></br>

需要使用链表的头插法来实现，因为头插法中最后压入栈的元素在链表的开头，它的 next 指针指向前一个压入栈的元素，在弹出元素使就可以通过 next 指针遍历到前一个压入栈的元素从而让这个元素称为新的栈顶元素。


## 队列

> First-In-First-Out

<font size=4> **1. 数组实现** </font></br>

```python
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
```

下面是队列的链表实现，需要维护 first 和 last 节点指针，分别指向队首和队尾。

这里需要考虑 first 和 last 指针哪个作为链表的开头。因为出队列操作需要让队首元素的下一个元素成为队首，所以需要容易获取下一个元素，而链表的头部节点的 next 指针指向下一个元素，因此可以让 first 指针链表的开头。

