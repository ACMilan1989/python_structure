#基于链表实现完全 二叉树

#先构建一个链表结点
class BinTNode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
class BinaryTree:
    def __init__(self):
        self.root = None
    def is_empty(self):
        return self.root is None
    def insertLeft(self,newNode):
        if self.root is not None:
            self.root = BinTNode(newNode)
        elif self.root.left is None:
            self.root.left = BinTNode(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.l