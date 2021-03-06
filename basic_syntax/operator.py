# coding=utf-8

""" 运算符
Q 25. 在Python中有多少种运算符？解释一下算数运算符。
在Python中，我们有7种运算符：算术运算符、关系运算符、赋值运算符、逻辑运算符、位运算符、成员运算符、身份运算符。
我们有7个算术运算符，能让我们对数值进行算术运算：
1.加号（+），将两个值相加
>>> 7+8
15
复制代码2.减号（-），将第一个值减去第二个值
>>> 7-8
-1
复制代码3.乘号（*），将两个值相乘
>>> 7*8
56
复制代码4.除号（/），用第二个值除以第一个值
>>> 7/8
0.875
>>> 1/1
1.0
//运算符执行地板除法（向下取整除），它会返回整除结果的整数部分。
>>> 7//2
3
复制代码这里整除后会返回3.5。
同样地，执行取幂运算。ab会返回a的b次方。
>>> 2**10
1024
复制代码最后，%执行取模运算，返回除法的余数。
>>> 13%7
6
>>> 3.5%1.5
0.5


Q 26. 解释一下Python中的关系运算符
关系运算符用于比较两个值。
1.小于号（<），如果左边的值较小，则返回True。
>>> 'hi'<'Hi'
False
复制代码2.大于号（>），如果左边的值较大，则返回True。
>>> 1.1+2.2>3.3
True
复制代码3.小于等于号（<=），如果左边的值小于或等于右边的值，则返回Ture。
>>> 3.0<=3
True
复制代码4.大于等于号（>=），如果左边的值大于或等于右边的值，则返回True。
>>> True>=False
True
复制代码
等于号（==），如果符号两边的值相等，则返回True。

>>> {1,3,2,2}=={1,2,3}
True
复制代码
不等于号（!=），如果符号两边的值不相等，则返回True。

>>> True!=0.1
True
>>> False!=0.1
True


复制代码Q 27. 解释一下Python中的赋值运算符
这在Python面试中是个重要的面试问题。
我们将所有的算术运算符和赋值符号放在一起展示：
>>> a=7
>>> a+=1
>>> a
8

>>> a-=1
>>> a
7

>>> a*=2
>>> a
14

>>> a/=2
>>> a
7.0

>>> a**=2
>>> a
49

>>> a//=3
>>> a
16.0

>>> a%=4
>>> a
0.0


复制代码Q 28. 解释一下Python中的逻辑运算符
Python中有3个逻辑运算符：and，or，not。
>>> False and True
False

>>> 7<7 or True
True

>>> not 2==2
False
复制代码Q 29. 解释一下Python中的成员运算符
通过成员运算符‘in’和‘not in’，我们可以确认一个值是否是另一个值的成员。
>>> 'me' in 'disappointment'
True

>>> 'us' not in 'disappointment'
True
复制代码Q 30. 解释一下Python中的身份运算符
这也是一个在Python面试中常问的问题。
通过身份运算符‘is’和‘is not’，我们可以确认两个值是否相同。
>>> 10 is '10'
False

>>> True is not False
True
复制代码Q 31. 讲讲Python中的位运算符
该运算符按二进制位对值进行操作。

与（&），按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0

>>> 0b110 & 0b010
2
复制代码2.或（|），按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
>>> 3|2
3
复制代码3.异或（^），按位异或运算符：当两对应的二进位相异时，结果为1
>>> 3^2
1
复制代码4.取反（~），按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1
>>> ~2
-3
复制代码5.左位移（<<），运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0
>>> 1<<2
4
复制代码6.右位移（>>），把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数
>>> 4>>2
1

"""
