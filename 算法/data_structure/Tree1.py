
#该树的定义为嵌套递归的定义
class Tree1:
    def __init__(self,root):#定义一个树
        return [root,[],[]];

    def insertLeft(self,root,newNote):
        t = root.pop(1);#先获取左子树
        if(len(t) >= 1):#若原来的左子树不为空，则将该子树插入新节点的左子树
            root.insert(1,[newNote,t,[]]);
        else:
            root.insert(1,[newNote,[],[]]);

    def insertRight(self,root,newNote):
        t = root.pop(2);#获取原右子树
        if(len(t) >= 1):#同上，判断该子树是否为空
            root.insert(2,[newNote,[],t]);
        else:
            root.insert(2,[newNote,[],[]]);

    def getRoot(self,root):#获取该子树的根节点
        return root[0];

    def setRoot(self,root,note):#设置根节点
        root[0] = note;

    def getLeft(self,root):#获取左子树
        return root[1];

    def getRight(self,root):
        return root[2];
