from 算法.data_structure.Node import Node

class UnorderList():#使用链表结构实现无序表
    def __init__(self):
        self.head = None;#采用头插法实现链表的添加,不同于平时所学，这里的头结点不是没有数据 而是插入的第一个数据作为头结点

    def add(self,data):#使用头插法
        temp = Node(data);#先初始化结点
        temp.setNext(self.head);
        self.head = temp;

    def size(self):
        temp = self.head;
        sum = 0;
        while(temp != None):
            sum += 1;
            temp = temp.getNext();
        return sum;

    def search(self,item):
        temp = self.head;
        while(temp != None):
            if(temp.gerData() == item):
                return True;
            temp = temp.getNext();
        return False;

    def remove(self,item):
        if self.head == None:
            return False;

        if (self.head.getData == item):
            self.head = self.head.getNext();
            return True;

        pre = self.head;
        cur = pre.getNext();
        while(cur != None):
            if(cur.getData() == item):
                pre.setNext(cur.getNext());
                return True;
            pre = cur;
            cur = pre.getNext();

        return False;



