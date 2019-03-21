# coding=utf-8

"""

// 二分查找的循环实现

public int bsearch(int[] a, int n, int value) {
  int low = 0;
  int high = n - 1;

  while (low <= high) {
    int mid = (low + high) / 2;
    if (a[mid] == value) {
      return mid;
    } else if (a[mid] < value) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return -1;
}




// 二分查找的递归实现
public int bsearch(int[] a, int n, int val) {
  return bsearchInternally(a, 0, n - 1, val);
}

private int bsearchInternally(int[] a, int low, int high, int value) {
  if (low > high) return -1;

  int mid =  low + ((high - low) >> 1);
  if (a[mid] == value) {
    return mid;
  } else if (a[mid] < value) {
    return bsearchInternally(a, mid+1, high, value);
  } else {
    return bsearchInternally(a, low, mid-1, value);
  }
}

"""


def bin_search(l, n):
    # Time: O(log(n))
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = left + (right - left) // 2
        # mid = left + (right - left)>>2
        if n == l[mid]:
            return mid
        elif n > l[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def bin_search1(l, n):
    return _recursion(l, 0, len(l) - 1, n)


def _recursion(l, left, right, n):
    if left > right:
        return -1

    mid = left + (right - left) >> 2

    if n == l[mid]:
        return mid
    elif n > l[mid]:
        return _recursion(l, mid+1, right, n)
    else:
        return _recursion(l, left, mid-1, n)




""" 二分查找

二分搜索算法的复杂度是对数级别的，意味着用bisect来搜索包含一百万个元素的列表，与用index来搜索包含14个元素的列表，所耗的时间差不多

"""


import time

t0 = time.time()
x = list(range(10**6))
i = x.index(991234)
print i

t1 = time.time()
print t1 - t0


from bisect import bisect_left
j = bisect_left(x, 991234)
print j

t2 = time.time()
print t2 - t1

