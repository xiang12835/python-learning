# coding=utf-8

#try…finally的使用
#假如要实现不管中间是否发生异常，都要输出一串字符串
try:
    i = 7
    print i
finally:
    print "不管上面是否异常，我必须输出！"

#第二个例子：要实现将一串字符串输出10000000次，假如异常发生，需要判断前面已经输出了多少次。
try:
    for i in range(10000000):
        print "我要输出10000000次，现在正在输出中，也不知道现在是多少次了"
finally:
    print "此时i的值是："+str(i)+"--并未完成全部输出"
