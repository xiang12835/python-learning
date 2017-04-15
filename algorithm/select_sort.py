# coding=utf-8


# 选择排序
def select_sort(lst=[]):
    """
    基本思想：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；
    第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
    以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。

    :param lst: 
    :return: 
    """
    count = len(lst)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):  # 从待排记录中选出最小的记录
            if lst[min] > lst[j]:
                min = j
        lst[min], lst[i] = lst[i], lst[min]  # 将最小的记录与待排序记录中的第一个记录进行交换
    return lst
