# coding=utf-8

# 树

# 树的基本构造
Tree1=[2,3,[58,6,[5]]]
#print Tree1[0]
#print Tree1[1]
#print Tree1[2]
Tree2=Tree1[2]
#print Tree2[0]


# 二叉树的构造
'''
比如要构造一个二叉树：
    7
 8     9
   23    36
57    58
可以这样分析：
base=(-->8也就是jd2,-->9也就是jd3,base)
jd2=(no,-->23也就是jd4,8)
jd3=(no,-->36也就是jd5,9)
jd4=(-->57也就是jd6,-->58Ҳ也就是jd7,23)
jd5=(no,no,36)
jd6=(no,no,57)
jd7=(no,no,58)
但是要注意，写的时候倒过来写
'''


class Node(object):
    def __init__(self, left=0, right=0, data=0):
        self.left = left
        self.right = right
        self.data = data


class Btree(object):
    def __init__(self, base=0):
        self.base = base

    def empty(self):
        if self.base is 0:
            return True
        else:
            return False

    def preorder(self, node):
        """前序遍历，NLR，根左右"""
        if node == 0:
            return
        print node.data
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        """中序遍历，LNR，左根右"""
        if node == 0:
            return
        self.inorder(node.left)
        print node.data
        self.inorder(node.right)

    def postorder(self,node):
        """后序遍历，LRN，左右根"""
        if node == 0:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print node.data


if __name__ == "__main__":
    node1 = Node(data=8)
    node2 = Node(data=9)
    root = Node(node1, node2, 7)
    x = Btree(root)
    print "前序遍历:"
    x.preorder(x.base)
    print "中序遍历:"
    x.inorder(x.base)
    print "后序遍历:"
    x.postorder(x.base)
