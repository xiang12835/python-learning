## 算法


### 排序

Kth Element：215 Kth Largest Element in an Array (Medium)

出现频率最多的 k 个数：347 Top K Frequent Elements (Medium)

按照字符出现次数对字符串排序：451


### 顺序查找

### 二分查找

求开方：69 Sqrt(x)

摆硬币：441 Arranging Coins

有序数组的 Single Element：540


### 贪心思想

> 概念

贪心思想保证每次操作都是局部最优的，并且最后得到的结果是全局最优的。


> 题目

分配饼干：455

投飞镖刺破气球：452

股票的最大收益：122 Best Time to Buy and Sell Stock II (Easy)

种植花朵：605

修改一个数成为非递减数组：665 Non-decreasing Array (Easy)

判断是否为子串：392 Is Subsequence (Medium)

分隔字符串使同种字符出现在一起：763 Partition Labels (Medium)

根据身高和序号重组队列：406 Queue Reconstruction by Height(Medium)


### 双指针

> 概念

双指针主要用于遍历数组，两个指针指向不同的元素，从而协同完成任务。

> 技巧

1 双索引技巧 - 对撞指针

有一些 LeetCode 题目，我们可以采用对撞指针进行求解：指针 left 和 right 分别指向数组的第一个元素和最后一个元素，然后指针 left 不断向前， 指针 right 不断递减，知道 left = right（当然具体的逻辑操作根据题目的变化而变化）。

示例：

 - 回文与反转问题


2 双索引技巧 - 滑动窗口

一些题目用滑动窗口方法解题，可以将时间复杂度控制在 O(n) 级别，最重要的是定义好滑动窗口，明确它要表达的意思，当然边界和初始值非常重要。

使用两个指针：一个仍然用于迭代(i)，而第二个指针（pos）总是指向下一次添加的位置。

示例：

 - 移除元素：27.
 - 长度最小的子数组：209.


3 双索引技巧 - 慢快指针

链表中的慢指针和快指针问题

示例：

- 环形链表：141.
- 环形链表 II：142.
- 相交链表：160.
- 删除链表的倒数第N个节点：19.


> 题目

有序数组的 Tow Sum：167 Two Sum II - Input array is sorted (Easy)

反转字符串中的元音字符：345 Reverse Vowels of a String (Easy)

两数平方和：633 Sum of Square Numbers (Easy)

回文字符串：680 Valid Palindrome II (Easy)

归并两个有序数组：88 Merge Sorted Array (Easy)

判断链表是否存在环：141 Linked List Cycle (Easy)

最长子序列：524 Longest Word in Dictionary through Deleting (Medium)


### 搜索

BFS | DFS

查找最大的连通面积：695

图的连通分量：547

矩阵中的连通区域数量：200

输出二叉树中所有从根到叶子的路径：257 Binary Tree Paths (Easy)

IP 地址划分：93

填充封闭区域：130

从两个方向都能到达的区域：417


## 数据结构


### 字符串

> 概念

字符串是一个由字符构成的数组

> 题目

两个字符串包含的字符是否完全相同：242 Valid Anagram (Easy)

字符串同构：205 Isomorphic Strings (Easy)

计算一组字符集合可以组成的回文字符串的最大长度：409 Longest Palindrome (Easy)

判断一个整数是否是回文数：9 Palindrome Number (Easy)

回文子字符串：647 Palindromic Substrings (Medium)

统计二进制字符串中连续 1 和连续 0 数量相同的子字符串个数：696


### 数组

> 数组相关的技术

你可能想要了解更多与数组相关的数据结构或技术。我们不会深入研究这张卡片中的大多数概念，而是在本文中提供相应卡片的链接。

1. 这里有一些其他类似于数组的数据结构，但具有一些不同的属性：

  - 字符串（已包含在本卡片中）
  - 哈希表
  - 链表
  - 队列
  - 栈

2. 正如我们所提到的，我们可以调用内置函数来对数组进行排序。但是，理解一些广泛使用的排序算法的原理及其复杂度是很有用的。

3. 二分查找也是一种重要的技术，用于在排序数组中搜索特定的元素。

4. 我们在这一章中引入了双指针技巧。想要灵活运用该技技巧是不容易的。这一技巧也可以用来解决：

    链表中的慢指针和快指针问题
    滑动窗口问题

5. 双指针技巧有时与贪心算法有关，它可以帮助我们设计指针的移动策略。 在不久的将来，我们会提供更多的卡片来介绍上面提到的这些技术，并更新链接。

示例：

- 最大连续1的个数：485.


> 题目

把数组中的 0 移到末尾：283. Move Zeroes (Easy)

调整矩阵：566. Reshape the Matrix (Easy)

找出数组中最长的连续 1：485. Max Consecutive Ones (Easy)

数组相邻差值的个数：667

数组的度：697

对角元素相等的矩阵：766

嵌套数组：565

分隔数组：769

一个数组元素在 [1, n] 之间，其中一个数被替换为另一个数，找出丢失的数和重复的数：645

寻找所有丢失的元素：448

寻找所有重复的元素：442

找出数组中重复的数，数组值在 [1, n] 之间：287

有序矩阵查找：240

有序矩阵的 Kth Element：378

帕斯卡三角形 118. Pascal's Triangle


### 栈和队列

用栈实现队列：232 Implement Queue using Stacks (Easy)

用队列实现栈：225 Implement Stack using Queues (Easy)

最小值栈：155 Min Stack (Easy)

用栈实现括号匹配：20 Valid Parentheses (Easy)

数组中元素与下一个比它大的元素之间的距离：739 Daily Temperatures (Medium)

在另一个数组中比当前元素大的下一个元素：496 Next Greater Element I (Easy)

循环数组中比当前元素大的下一个元素：503 Next Greater Element II (Medium)


### 哈希表

> 概念

哈希表是一种使用哈希函数组织数据，以支持快速插入和搜索的数据结构。

有两种不同类型的哈希表：**哈希集合**和**哈希映射**。

  - 哈希集合是集合数据结构的实现之一，用于存储非重复值。
  - 哈希映射是映射数据结构的实现之一，用于存储(key, value)键值对。

在标准模板库的帮助下，哈希表是易于使用的。大多数常见语言（如Java，C ++ 和 Python）都支持哈希集合和哈希映射。

通过选择合适的哈希函数，哈希表可以在插入和搜索方面实现出色的性能。

> 哈希表的原理

哈希表的关键思想是**使用哈希函数将键映射到存储桶**。更确切地说，

1. 当我们插入一个新的键时，哈希函数将决定该键应该分配到哪个桶中，并将该键存储在相应的桶中；
2. 当我们想要搜索一个键时，哈希表将使用相同的哈希函数来查找对应的桶，并只在特定的桶中进行搜索。

> 设计哈希表的关键

1. 哈希函数

哈希函数是哈希表中最重要的组件，该哈希表用于将键映射到特定的桶。在上一篇文章中的示例中，我们使用 y = x % 5 作为散列函数，其中 x 是键值，y 是分配的桶的索引。

散列函数将取决于键值的范围和桶的数量。

哈希函数的设计是一个开放的问题。其思想是尽可能将键分配到桶中，理想情况下，完美的哈希函数将是键和桶之间的一对一映射。然而，在大多数情况下，哈希函数并不完美，它需要在桶的数量和桶的容量之间进行权衡。

2. 冲突解决

理想情况下，如果我们的哈希函数是完美的一对一映射，我们将不需要处理冲突。不幸的是，在大多数情况下，冲突几乎是不可避免的。

冲突解决算法应该解决以下几个问题：

- 如何组织在同一个桶中的值？
- 如果为同一个桶分配了太多的值，该怎么办？
- 如何在特定的桶中搜索目标值？

根据我们的哈希函数，这些问题与**桶的容量**和可能映射到**同一个桶中键的数目**有关。

让我们假设存储最大键数的桶有 N 个键。

通常，如果 N 是常数且很小，我们可以简单地使用一个**数组**将键存储在同一个桶中。如果 N 是可变的或很大，我们可能需要使用**高度平衡的二叉树**来代替。


> 复杂度分析 - 哈希表

1 复杂度分析

如果总共有 M 个键，那么在使用哈希表时，可以很容易地达到 O(M) 的空间复杂度。

但是，你可能已经注意到哈希表的时间复杂度与设计有很强的关系。

我们中的大多数人可能已经在每个桶中使用数组来将值存储在同一个桶中，理想情况下，桶的大小足够小时，可以看作是一个常数。插入和搜索的时间复杂度都是 O(1)。

但在最坏的情况下，桶大小的最大值将为 N。插入时时间复杂度为 O(1)，搜索时为 O(N)。

2 内置哈希表的原理

内置哈希表的典型设计是：

- 键值可以是任何可哈希化的类型。并且属于可哈希类型的值将具有哈希码。此哈希码将用于映射函数以获取存储区索引。
- 每个桶包含一个数组，用于在初始时将所有值存储在同一个桶中。
- 如果在同一个桶中有太多的值，这些值将被保留在一个高度平衡的二叉树搜索树中。

插入和搜索的平均时间复杂度仍为 O(1)。最坏情况下插入和搜索的时间复杂度是 O(logN)，使用高度平衡的 BST。这是在插入和搜索之间的一种权衡。


> 题目

数组中的两个数和为给定值：1 Two Sum (Easy)

判断数组是否含有相同元素：217 Contains Duplicate (Easy)

最长和谐序列：594 Longest Harmonious Subsequence (Easy)

最长连续序列：128


### 链表

> 概念

与数组相似，链表也是一种线性数据结构。

链表中的每个元素实际上是一个单独的对象，而所有对象都通过每个元素中的引用字段链接在一起。

链表有两种类型：单链表和双链表。

双链表：与单链表不同的是，双链表的每个结点中都含有两个引用字段。

> 双指针技巧

慢指针和快指针问题

> 题目

找出两个链表的交点：160. Intersection of Two Linked Lists (Easy)

链表反转：206. Reverse Linked List (Easy)

归并两个有序的链表：21. Merge Two Sorted Lists (Easy)

从有序链表中删除重复节点：83. Remove Duplicates from Sorted List (Easy)

删除链表的倒数第 n 个节点：19. Remove Nth Node From End of List (Medium)

交换链表中的相邻结点：24

根据有序链表构造平衡的 BST：109

链表求和：445

分隔链表：725

回文链表：234. Palindrome Linked List (Easy)

链表元素按奇偶聚集：328

移除链表元素：203.


### 树

树的高度：104. Maximum Depth of Binary Tree (Easy)

翻转树：226. Invert Binary Tree (Easy)

归并两棵树：617. Merge Two Binary Trees (Easy)

判断路径和是否等于一个数：112. Path Sum (Easy)

统计路径和等于一个数的路径数量：437. Path Sum III (Easy)

树的对称：101. Symmetric Tree (Easy)

平衡树：110. Balanced Binary Tree (Easy)

最小路径：111. Minimum Depth of Binary Tree (Easy)

统计左叶子节点的和：404. Sum of Left Leaves (Easy)

修剪二叉查找树：669. Trim a Binary Search Tree (Easy)

子树：572. Subtree of Another Tree (Easy)

从有序数组中构造二叉查找树：108. Convert Sorted Array to Binary Search Tree (Easy)

两节点的最长路径：543. Diameter of Binary Tree (Easy)

找出二叉树中第二小的节点：671. Second Minimum Node In a Binary Tree (Easy)

二叉查找树的最近公共祖先：235. Lowest Common Ancestor of a Binary Search Tree (Easy)

二叉树的最近公共祖先：236. Lowest Common Ancestor of a Binary Tree (Medium)

相同节点值的最大路径长度：687. Longest Univalue Path (Easy)

间隔遍历：337. House Robber III (Medium)

一棵树每层节点的平均数：637. Average of Levels in Binary Tree (Easy)

得到左下角的节点：513. Find Bottom Left Tree Value (Easy)

非递归实现二叉树的前序遍历：144. Binary Tree Preorder Traversal (Medium)

非递归实现二叉树的后序遍历：145. Binary Tree Postorder Traversal (Medium)

非递归实现二叉树的中序遍历：94. Binary Tree Inorder Traversal (Medium)

在 BST 中寻找两个节点，使它们的和为一个给定值：653. Two Sum IV - Input is a BST (Easy)

在 BST 中查找两个节点之差的最小绝对值：530. Minimum Absolute Difference in BST (Easy)

把 BST 每个节点的值都加上比它大的节点的值：538. Convert BST to Greater Tree

寻找 BST 中出现次数最多的节点：501. Find Mode in Binary Search Tree (Easy)

寻找 BST 的第 k 个元素：230. Kth Smallest Element in a BST (Medium)

实现一个 Trie：208. Implement Trie (Prefix Tree) (Medium)

实现一个 Trie，用来求前缀和：677. Map Sum Pairs (Medium)


### 位

位1的个数 191. Number of 1 Bits.py

汉明距离

颠倒二进制位 190. Reverse Bits.py

### 数学

Fizz Buzz

计数质数

3的幂 326. Power of Three

罗马数字转整数 13. Roman to Integer
