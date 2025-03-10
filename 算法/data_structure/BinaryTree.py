class BinaryTree():
    def __init__(self,note):
        root = note;
        lchild = None;
        rchild = None;

    def insertLeft(self,note):
        t = self.lchild;#获取左子树
        newNote = BinaryTree(note);#创建结点
        newNote.lchild = t;
        self.lchild = newNote;

    def insertRight(self,root,note):
        t = self.rchild;#获取右子树
        newNote = BinaryTree(note);
        newNote.rchild(t);
        self.rchild = t;

    def getRight(self):#获取右子树
        return self.rchild;

    def getLeft(self):#获取左子树
        return self.lchild;

    def getRoot(self):#获取根结点
        return self.root;

    def setRoot(self,note):#设置根节点
        self.root = note;

