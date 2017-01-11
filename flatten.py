from compiler.ast import flatten


l1 = [1, 2]
l2 = [3, 4]
l = flatten([l1, l2])
print l


l = l1 + l2
print l


l = flatten([[1, 2], 3, [4, 5]])
print l

