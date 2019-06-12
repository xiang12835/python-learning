# coding=utf-8

"""

给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

"""

class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return []
        B = []
        for i in xrange(len(A)):
            tmp = A[i]
            A[i] = 1
            B.append(reduce(lambda x,y: x*y, A))
            A[i] = tmp
        return B
