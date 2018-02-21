# coding=utf-8


def is_odd(n):
    return n % 2 == 1


def is_odd_1(n):
    return n & 1 == 1


if __name__ == "__main__":
    print is_odd(5)
    print is_odd_1(5)
