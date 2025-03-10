class Node():#声明一个结点类型，用于实现无序表的链表操作
    def __init__(self,data):
        self.data=data;
        self.next=None;

    def getData(self):
        return self.data;

    def getNext(self):
        return self.next;

    def setData(self,data):
        self.data = data;

    def setNext(self,next):
        self.next = next;
