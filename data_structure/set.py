# coding=utf-8

'''
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”
'''

a = set("aghglcdhgjlagtjafajlag")
b = set("cdes")

print a&b
print a|b
print a-b
print set(a)


s = set([1, 1, 2, 2, 3, 3])
print s

s.add(4) # 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
print s

s.remove(4) # 通过remove(key)方法可以删除元素
print s

# 小结: 使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。


q = {"a", "b", "c", "d"}
print q
print type(q)

print q.pop()  # pop() 函数用于移除集合中的第一个元素，并且返回该元素的值。
