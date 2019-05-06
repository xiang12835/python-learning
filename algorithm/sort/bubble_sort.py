# coding=utf-8


"""
    Bubble Sort
    -----------
    Time Complexity: O(n**2)
    Space Complexity: O(1) Auxiliary
    Stable: Yes
"""


# 冒泡排序
def bubble_sort(lists):  # 小数上浮 - 每趟会在 i 处找到最小的数
    """ 
    它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
    走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
    """
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


l = [3, 4, 6, 1, 2, 5]
print bubble_sort(l)


a = [6, 5, 4, 3, 2, 1]  # 大数下沉
def bubble_sort1(a):
    # O(n ** 2) | O(1) | 原地 | 稳定
    # 冒泡排序，大数下沉
    n = len(a)
    for i in range(n):
        has_changed = False  # 提前退出冒泡循环的标记位
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                has_changed = True  # 数据有交换
        if not has_changed:  # 没有数据交换，提前退出
            break
    return a

print bubble_sort1(a)
