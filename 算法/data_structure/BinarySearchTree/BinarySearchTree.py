from 算法.data_structure.BinarySearchTree.TreeNode import TreeNode

class BinarySearchTree:
    def __init__(self):
        self.root = None;
        self.size = 0;

    def length(self):
        return self.size;

    def __len__(self):
        return self.size;

    def __iter__(self):
        return self.root.__iter__();

    def _put(self,key,value,currentNode):
        currentNode = TreeNode();
        if(key < currentNode.key):#若标识小于当前节点的标识，则要插入左子树
            if(currentNode.hasLeftChild()):#如果由左子树，则要插入其左子树上
                self._put(key,value,currentNode.lchild);
            else:#若无，则直接插入
                currentNode.lchild = TreeNode(key,value,None,None,currentNode);
        else:
            if(currentNode.hasRightChild()):
                self._put(key,value,currentNode.rchild);
            else:
                currentNode.rchild = TreeNode(key,value,None,None,currentNode);


    def __setitem__(self, key, value):
         self.put(key,value);

    def put(self,key,value):
        if(self.root):
            self._put(key,value,self.root);
        else:
            self.root = TreeNode(key,value);
            self.size += 1;

    #def get(self,key):#获取key值


