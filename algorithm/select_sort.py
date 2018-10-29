# coding=utf-8


# 选择排序
def select_sort(a):
    """
    基本思想：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；
    第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
    以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。

    :param lst: 
    :return: 
    """
    n = len(a)
    for i in range(0, n):
        min = i
        for j in range(i + 1, n):  # 从待排记录中选出最小的记录
            if a[min] > a[j]:
                min = j
        a[min], a[i] = a[i], a[min]  # 将最小的记录与待排序记录中的第一个记录进行交换
    return a


a = [3, 5, 4, 6, 2, 1]
print select_sort(a)
