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
        #若不越界返回对应位置元素
        else:return self.data[index]
    #设置某个位置的元素(替换原位置的值)
    def __setitem__(self, index, value):
        if self.__getitem__(index):
            self.data[index] = value
            return True
    #清除arr的元素
    def clear(self):
        #初始化
        return self.__init__()
    #求arr中共有多少元素
    def count(self):
        return self.num
    #在末尾插入元素
    def append(self,value):
        #首先判断顺序表是否满了
        if self.is_full():
            print("list is full")
            return
        else:
            self.data[self.num] = value
            self.num += 1

    def insert(self, key, value):
        if not isinstance(key, int):
            raise TypeError
        if key < 0:  # 暂时不考虑负数索引
            raise IndexError
          # 当key大于元素个数时，默认尾部插入
        if key >= self.num:
            self.append(value)
        else:
            for i in range(self.num, key, -1):
                self.date[i] = self.date[i - 1]
      # 赋值
        self.date[key] = value
        self.num += 1
      # 删除元素的操作
        def pop(self, key=-1):
            if not isinstance(key, int):
              raise TypeError
        if self.num - 1 < 0:
            raise IndexError("pop from empty list")
        elif key == -1:
      # 原来的数还在，但列表不识别他
            self.num -= 1
        else:
            for i in range(key, self.num - 1):
                self.date[i] = self.date[i + 1]
                self.num -= 1
        def index(self, value, start=0):
            for i in range(start, self.num):
               if self.date[i] == value:
                   return i
        # 没找到
        raise ValueError("%d is not in the list" % value)
        # 列表反转
        def reverse(self):
            i, j = 0, self.num - 1
        while i < j:
            self.date[i], self.date[j] = self.date[j], self.date[i]
            i, j = i + 1, j - 1