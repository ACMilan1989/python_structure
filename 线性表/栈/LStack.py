#基于链表实现栈磊，用LNode作为节点
class Node(object):
    def __init__(self,initdata,next_=None):
        self.data = initdata
        self.next = next_
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.next = newdata
    def setNext(self,nextNode):
        self.next = nextNode
class LStack():
    def __init__(self):
        #初始化一个链表节点
        self._top = None
    #判断是否为空
    def is_empty(self):
        return self._top is None
    def top(self):
        if self._top is None:
            raise Exception
        return self._top.elem
    #压栈(新的node挂载在top上)
    def push(self,elem):
        self._top = Node(elem,self.top)
    def pop(self):
        #判断是否栈为空
        if self.is_empty():
            raise Exception
        p = self._top
        self._top = p.next
        return p.elem
