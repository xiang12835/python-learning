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


def bin_search(l, val):
    """
    二分查找的循环实现

    """
    # Time: O(log(n))
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = left + (right - left) >> 2
        # mid = left + (right - left) // 2
        if val == l[mid]:
            return mid
        elif val > l[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def bin_search1(l, val):
    """
    二分查找的递归实现

    """
    return _recursion(l, 0, len(l) - 1, val)


def _recursion(l, left, right, val):
    if left > right:
        return -1

    mid = left + (right - left) >> 2

    if val == l[mid]:
        return mid
    elif val > l[mid]:
        return _recursion(l, mid+1, right, val)
    else:
        return _recursion(l, left, mid-1, val)


def bin_search2(l, val):
    """
    二分查找的递归实现

    """
    def _recursion(l, left, right, val):
        if left > right:
            return -1

        mid = left + (right - left) >> 2

        if val == l[mid]:
            return mid
        elif val > l[mid]:
            return _recursion(l, mid + 1, right, val)
        else:
            return _recursion(l, left, mid - 1, val)

    return _recursion(l, 0, len(l) - 1, val)


""" 变体一：查找第一个值等于给定值的元素

public int bsearch(int[] a, int n, int value) {
  int low = 0;
  int high = n - 1;
  while (low <= high) {
    int mid =  low + ((high - low) >> 1);
    if (a[mid] > value) {
      high = mid - 1;
    } else if (a[mid] < value) {
      low = mid + 1;
    } else {
      if ((mid == 0) || (a[mid - 1] != value)) return mid;
      else high = mid - 1;
    }
  }
  return -1;
}

"""


def bsearch1(l, val):
    """
    变体一：查找第一个值等于给定值的元素

    """
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = left + (right - left) >> 2
        if val < l[mid]:
            right = mid - 1
        elif val > l[mid]:
            left = mid + 1
        else:
            if mid == 0 or l[mid-1] != val:
                return mid
            else:
                right = mid - 1

    return -1


'''变体二：查找最后一个值等于给定值的元素

public int bsearch(int[] a, int n, int value) {
  int low = 0;
  int high = n - 1;
  while (low <= high) {
    int mid =  low + ((high - low) >> 1);
    if (a[mid] > value) {
      high = mid - 1;
    } else if (a[mid] < value) {
      low = mid + 1;
    } else {
      if ((mid == n - 1) || (a[mid + 1] != value)) return mid;
      else low = mid + 1;
    }
  }
  return -1;
}

'''


def bsearch2(l, val):
    """
    变体二：查找最后一个值等于给定值的元素

    """
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = left + (right - left) >> 2
        if val < l[mid]:
            right = mid - 1
        elif val > l[mid]:
            left = mid + 1
        else:
            if mid == len(l)-1 or l[mid+1] != val:
                return mid
            else:
                left = mid + 1

    return -1


"""变体三：查找第一个大于等于给定值的元素

public int bsearch(int[] a, int n, int value) {
  int low = 0;
  int high = n - 1;
  while (low <= high) {
    int mid =  low + ((high - low) >> 1);
    if (a[mid] >= value) {
      if ((mid == 0) || (a[mid - 1] < value)) return mid;
      else high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return -1;
}

"""


def bsearch3(l, val):
    """
    变体三：查找第一个大于等于给定值的元素

    比如，数组中存储的这样一个序列：3，4，6，7，10。如果查找第一个大于等于 5 的元素，那就是 6。

    """
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = left + (right - left) >> 2
        if l[mid] < val:
            left = mid + 1
        else:
            if mid == 0 or l[mid-1] < val:
                return mid
            else:
                right = mid - 1

    return -1


"""变体四：查找最后一个小于等于给定值的元素

public int bsearch7(int[] a, int n, int value) {
  int low = 0;
  int high = n - 1;
  while (low <= high) {
    int mid =  low + ((high - low) >> 1);
    if (a[mid] > value) {
      high = mid - 1;
    } else {
      if ((mid == n - 1) || (a[mid + 1] > value)) return mid;
      else low = mid + 1;
    }
  }
  return -1;
}

"""


def bsearch4(l, val):
    """
    变体四：查找最后一个小于等于给定值的元素

    比如，数组中存储了这样一组数据：3，5，6，8，9，10。最后一个小于等于 7 的元素就是 6。是不是有点类似上面那一种？实际上，实现思路也是一样的。

    """
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = left + (right - left) >> 2
        if l[mid] > val:
            right = mid - 1
        else:
            if mid == len(l)-1 or l[mid+1] > val:
                return mid
            else:
                left = mid + 1

    return -1





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

