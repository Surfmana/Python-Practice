class Queue():
    def __init__(self):
        self.items = [];

    def isEmpty(self):
        return self.items == [];

    def enqueue(self,data):#采用列表尾作队尾
        self.items.append(data);

    def dequeeu(self):#采用列表头作为头部
        return self.items.pop(0);

    def size(self):
        return len(self.items);
