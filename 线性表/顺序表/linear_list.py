#顺序表
#-*- coding:utf-8 -*-
class Arr(object):
    #顺序表初始化
    def __init__(self,size=8):
        #最大索引max_index
        #初始arr的最大元素个数
        self.max_index = size - 1
        self.num = 0
        #基于list实现
        self.data = [None]*self.max_index
    #判断arr是否为空
    def is_empty(self):
        return self.num is 0
    #判断arr是否为满
    def is_full(self):
        return self.num is self.max_index+1
    #获取某个位置的元素
    def __getitem__(self, index):
        #判断index是否是int类型
        if not isinstance(index,int):
            raise TypeError
        #如果是int类型,向下进行
        #判断index是否越界
        if index >= self.num:
            raise IndexError
        else:return self.data[index]