# coding=utf-8

""" 三元操作符 ”?:“

C?X:Y 在 Python 中等价的形式为 X if C else Y

"""

""" switch...case

Python 中可以使用多种方式来实现 switch...case 比如下面这一种：

switch(n) {
  case 0:
    printf("0");
    break;
  case 1:
    printf("1");
    break;
  case 2:
    printf("2");
    break;
  default:
    printf("????");
    break;
}

def f(x):
    return {
      0: "0",
      1: "1",
      2: "2"
    }.get(n, "???")

"""
