# coding=utf-8


# 快速排序
def quick_sort(lists, left, right):
    """
    通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
    然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

    :param lists: 
    :param left: 
    :param right: 
    :return:
    """
    if left >= right:
        return lists
    val = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= val:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= val:
            left += 1
        lists[right] = lists[left]
    lists[right] = val
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists
