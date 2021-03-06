#链表
class Node(object):
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.next = newdata
    def setNext(self,nextNode):
        self.next = nextNode
temp = Node(90)
temp.setData(20)
print(temp.getNext())
#定义一个无序链表
class UnorderedList:
    def __init__(self):
        self.head = None
    #判断链表是否为空
    def isEmpty(self):
        return self.head == None
    #追加元素
    #此方法是新建的节点挂在head上
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    def search(self,item):
        current = self.head
        found = False
        while current.getData() == item:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())