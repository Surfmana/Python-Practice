from 算法.data_structure.BinaryTree import BinaryTree
from 算法.data_structure.Stack import Stack

def buildParseTree(fpexp):#创建解析树
    fplist = fpexp.split();#先将解析式分割
    pStack = Stack();#创建数据栈，用于存储上升的子树
    etree = BinaryTree(" ");#先声明一个空结点,并且用于记录头结点
    pStack.push(etree);#第一个比为数字，因此首结点必要进行下调
    currentNode = etree;
    for i in fplist:#遍历解析式
        if(i == "("):#如果是左括号，则要进行结点下移
            currentNote.insertLeft(" ");#创建一个新的子树来存放该节点
            pStack.push(currentNote);
            currentNote = currentNote.lchild;
        elif(i not in ["+","-","*","/",")"]):#如果是数字的话，则要进行结点上移
            currentNote.setRoot(int(i));#当前结点的值就是为该数字
            currentNote = pStack.pop();#数字下一个必然是运算符，因此要出栈上移
        elif(i in ["+","-","*","/"]):#如果是运算符，则当前结点的值则为该运算符，然后说明一个下一个是数字，因此要设置右子树
            currentNote.setRoot(i);
            currentNote.insertRight(" ");
            pStack.push(currentNote);#要入栈下移
            currentNote = currentNote.rchild;
        elif(i == ")"):#如果是右括号，则说明表达式解析完毕，要出栈上移
            currentNote = pStack.pop();
        else:#否则解析式错误
            raise ValueError;
    return etree;

def countParseTree(etree):
    if (etree.getRoot() not in ["+","-","*","/"]):#说明该节点是数字
        return etree.getRoot();
    elif(etree.getRoot() in ["+","-","*","/"]):#说明结点是运算符
        left = countParseTree(etree.getLeft());#得到左子树的结果
        right = countParseTree(etree.getRight());#得到右子树的结果
        parse = etree.getRoot();#得到运算符
        if(parse == "+"):
            return left + right;
        elif(parse == "-"):
            return left - right;
        elif(parse == "*"):
            return left * right;
        elif(parse == "/"):
            return left / right;
        



