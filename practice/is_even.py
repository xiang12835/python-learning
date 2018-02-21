# coding=utf-8


def is_even(n):
    return n % 2 == 0


def is_even_1(n):
    return n & 1 == 0


if __name__ == "__main__":
    print is_even(5)
    print is_even_1(5)

    print is_even(6)
    print is_even_1(6)
