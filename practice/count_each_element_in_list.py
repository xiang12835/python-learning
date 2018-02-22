# coding=utf-8


from collections import Counter


def count_each_element_nums_in_list(nums):
    d = {}
    for n in nums:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    return d


if __name__ == "__main__":

    nums = [1, 2, 2, 4, 5]
    print count_each_element_nums_in_list(nums)
    print Counter(nums)
