# coding=utf-8


"""

快排的思想是这样的：如果要排序数组中下标从 p 到 r 之间的一组数据，我们选择 p 到 r 之间的任意一个数据作为 pivot（分区点）。

我们遍历 p 到 r 之间的数据，将小于 pivot 的放到左边，将大于 pivot 的放到右边，将 pivot 放到中间。经过这一步骤之后，数组 p 到 r 之间的数据就被分成了三个部分，前面 p 到 q-1 之间都是小于 pivot 的，中间是 pivot，后面的 q+1 到 r 之间是大于 pivot 的。

根据分治、递归的处理思想，我们可以用递归排序下标从 p 到 q-1 之间的数据和下标从 q+1 到 r 之间的数据，直到区间缩小为 1，就说明所有的数据都有序了。


// 快速排序，A 是数组，n 表示数组的大小
quick_sort(A, n) {
  quick_sort_c(A, 0, n-1)
}
// 快速排序递归函数，p,r 为下标
quick_sort_c(A, p, r) {
  if p >= r then return
  q = partition(A, p, r) // 获取分区点
  quick_sort_c(A, p, q-1)
  quick_sort_c(A, q+1, r)
}
//分区函数
partition(A, p, r) {
  pivot := A[r]
  i := p
  for j := p to r-1 do {
    if A[j] < pivot {
      swap A[i] with A[j]
      i := i+1
    }
  }
  swap A[i] with A[r]
  return i
}
分区函数代码说明：通过游标i把A[p...r-1]分成2部分，A[p...i-1]的元素都是小于pivot的，我们暂且叫它“已处理区间”，A[i+1...r-1]是“未处理区间”。我们每次都从未处理区间取出一个元素A[j]，与poivt相比，如果小于pivot，则将其加入到已处理区间的尾部，也就是A[i]位置。

"""


import random


def quick_sort(a):
    _quick_sort_between(a, 0, len(a) - 1)


def _quick_sort_between(a, low, high):
    if low < high:
        # get a random position as the pivot
        k = random.randint(low, high)
        a[low], a[k] = a[k], a[low]

        m = _partition(a, low, high)  # a[m] is in final position
        _quick_sort_between(a, low, m - 1)
        _quick_sort_between(a, m + 1, high)


def _partition(a, low, high):
    pivot, j = a[low], low
    for i in range(low + 1, high + 1):
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]  # swap
    a[low], a[j] = a[j], a[low]
    return j


def test_quick_sort():
    a1 = [3, 5, 6, 7, 8]
    quick_sort(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    quick_sort(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    quick_sort(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a4)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a1)
    print(a1)
    quick_sort(a2)
    print(a2)
    quick_sort(a3)
    print(a3)
    quick_sort(a4)
    print(a4)



def quick_sort1(ls, idx_start, idx_end):
    if idx_end - idx_start <= 0:
        return

    pivot = idx_end
    i = idx_start
    for j in range(i, idx_end+1):
        if ls[j] <= ls[pivot]:
            ls[i], ls[j] = ls[j], ls[i]
            if j == pivot:
                pivot = i
            i += 1
    quick_sort1(ls, idx_start, pivot-1)
    quick_sort1(ls, pivot+1, idx_end)


# 快速排序
def quick_sort2(lists, left, right):
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
    while left != right:
        while left < right and lists[right] >= val:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= val:
            left += 1
        lists[right] = lists[left]
    lists[right] = val
    quick_sort2(lists, low, left - 1)
    quick_sort2(lists, left + 1, high)
    return lists


# if __name__ == '__main__':
#     l = [6, 4, 8, 9, 2, 3, 1]
#     print '排序前:', l
#     length = len(l) - 1
#     quick_sort2(l, 0, len(l) - 1)
#     print '排序后:', l
