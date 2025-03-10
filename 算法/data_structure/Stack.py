class Stack:
    def __init__(self):
        self.items = [];#初始化栈

    def isEmpty(self):
        return self.items == [];

    def push(self,data):#入栈
        self.items.append(data);

    def pop(self):
        if self.isEmpty():
            return None;
        return self.items.pop();#出栈

    def peek(self):
        if len(self.items)-1<0:
            return None;
        return self.items[len(self.items)-1];#查看栈顶元素

    def size(self):
        return len(self.items);
