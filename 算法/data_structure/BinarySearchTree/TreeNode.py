class TreeNode:
    def __init__(self,key,value,left = None,right = None,parent = None):
        self.key = key;
        self.value = value;
        self.lchild = left;
        self.rchild = right;
        self.parent = parent;

    def hasLeftChild(self):
        return self.lchild;

    def hasRightChild(self):
        return self.rchild;

    def isLeftChild(self):
        return self.parent and self.parent.lchild == self;

    def isRightChild(self):
        return self.parent and self.parent.rchild == self;

    def isRoot(self):
        return not self.parent;

    def isLeaf(self):
        return not (self.lchild or self.rchild);

    def hasAnyChild(self):
        return self.rchild or self.lchild;

    def hasBothChild(self):
        return self.lchild and self.rchild;

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key;
        self.value = value;
        self.lchild = lc;
        self.rchild = rc;
        if(self.hasLeftChild()):
            self.lchild.parent = self;
        if(self.hasRightChild()):
            self.rchild.parent = self;
    def iter(self):#重新编写迭代器，相当于中序遍历算法
        if self:
            if(self.hasLeftChild()):
                for item in self.lchild:
                    yield item;
            yield self.key;
            if(self.hasRightChild()):
                for item in self.rchild:
                    yield item;


