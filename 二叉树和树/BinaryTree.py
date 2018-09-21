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
    def find_none_node(self,node,way=left):
        #way的值left或right
        self.way = way
        if self.way == 'left':
            self.p = node.left
            if self.p.left is None:
                return self.p.left
        elif self.way == 'right':
            self.p = node.right
            if self.p.right is None:
                return self.p.right
        else:
            raise  TypeError
        self.find_none_node(self.p,self.way)

    def insertLeft(self,newNode):
        if self.root is not None:
            self.root = BinTNode(newNode)
        else:
            self.N = self.find_none_node(self.root,way = left)
            self.N.left = BinTNode(newNode)
    def insertright(self,newNode):
        if self.root is not None:
            self.root = BinTNode(newNode)
        else:
            self.N = self.find_none_node(self.root,way = right)
            self.N.right = BinTNode(newNode)