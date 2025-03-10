from 算法.data_structure.BinaryTree import BinaryTree

def preorder(eTree):#先序遍历
    if(eTree is not None):
        print(eTree.getRoot());
        preorder(eTree.lchild);
        preorder(eTree.rchild);

def postorder(eTree):#中序遍历
    if(eTree is not None):
        postorder(eTree.lchild);
        print(eTree.getRoot);
        postorder(eTree.rchild);

def inorder(eTree):#后序遍历
    if(eTree is not None):
        postorder(eTree.lchild);
        postorder(eTree.rchild);
        print(eTree.getRoot);
