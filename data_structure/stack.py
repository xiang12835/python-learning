# coding=utf-8

# 栈的实现
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



class RightStack():
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

    def r_push(st,data):
        if st.full():
            print "RightStack is full"
        else:
            st.stack.append(data)
            st.top=st.top+1

    def r_pop(st):
        if st.empty():
            print "RightStack is empty"
        else:
            st.top=st.top-1


class LeftStack():
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

    def l_push(st,data):
        if st.full():
            print "LeftStack is full"
        else:
            st.stack.insert(0, data)
            st.top=st.top+1

    def l_pop(st):
        if st.empty():
            print "LeftStack is empty"
        else:
            for i in xrange(1, len(st.stack)):
                st.stack[i-1] = st.stack[i]
            st.top=st.top-1
