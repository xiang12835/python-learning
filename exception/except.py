# coding=utf-8

# Python异常的处理
# 使用try…except语句，假如try出现了某种异常，则执行except下面的语句
try:
    print i
except NameError:     #这里一定要指明异常类型
    i=9
    i+=10
    print "刚才i没定义，处理了异常之后，i的值为："+str(i)


#处理多种异常
try:
    print i+j
except NameError:
    i=j=0
    print "刚刚i或j没有进行初始化数据，现在我们将其都初始化为0，结果是："
    print i+j
except TypeError:
    print "刚刚i与j类型对应不上，我们转换一下类型即可处理异常，处理后：结果是："+str(i)+str(j)


try:
    print('try...')
    r = 10 / int('2')
    # r = 10 / 0
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


''' 总结
try/except/else/finally

- 如果 try 内没有发生异常，则调用 else 内的代码
- except 块用于捕获异常，可以有多个 except 来捕获不同类型的错误
- else 会在 finally 之前运行，else 块可以用来缩减 try 块中的代码量
- 最终一定会执行 finally，可以在其中进行清理工作
'''



a = 1
try:
  a += 1
except:
  a += 1
else:
  a += 1
finally:
  a += 1
print a

