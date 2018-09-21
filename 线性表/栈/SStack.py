#栈的顺序表实现
#用list对象存储堆栈的元素
#所有的栈操作都映射到list操作
class SStack():
    def __init__(self):
        self.data=[]
    #判断栈是否是空的
    def is_empty(self):
        return len(self.data) == 0
    #从栈的头部取出一个元素
    def top(self):
        if self.is_empty():
            print('Stack is empty')
            return
        return self.data[-1]
    #压堆
    def push(self,elem):
        self.data.append(elem)
    def pop(self):
        if self.is_empty():
            print('Stack is empty')
            return
        return self.data.pop()