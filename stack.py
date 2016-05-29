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
