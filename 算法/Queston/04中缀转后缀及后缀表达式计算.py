#中缀转后缀其本质是由于优先级高的部分先计算，坡坏了原来的顺序计算，因此此时需要使用栈进行反转
from 算法.data_structure.Stack import Stack
def infixToPostfix(str):
    prec={};#用于存储个字符的计算优先级
    prec["+"]=1;
    prec["-"]=1;
    prec["*"]=2;
    prec["/"]=2;
    prec["("]=0;
    operator = "+-*/";
    opStack = Stack();#用于存储运算及的栈
    postList = "";#用于存储结果

    for c in str:
        if( c== "("):#若是左括号，则直接压栈
            opStack.push(c);
        elif(c == ")"):#若是右括号则一直出栈直到遇到左括号
            k = opStack.pop();
            while(k != "("):
                postList+=k;
                k = opStack.pop();
        elif(c in operator):#如果是运算符，则要与栈顶元素进行比较,直到栈为空或者运算符优先级比它小的入栈
            k = opStack.peek();
            if(opStack.isEmpty()):
                opStack.push(c);
            else:
                while( not prec[k] < prec[c]):
                    if(opStack.isEmpty()):
                        break;
                    k=opStack.pop();
                    postList+=k;
                opStack.push(c);
        else:#剩下的为数字，则直接进入列表
            postList += c;

    while(not opStack.isEmpty()):#将栈里的元素全部弹入结果的列表里
        postList+=opStack.pop();

    return postList;

def calculatePostfix(str):#计算后缀表达式
    numStack = Stack();#用于存储数据
    operator = "+-*/";#用于判断是否是运算符
    for c in str:
        if(c not in operator):#数字直接入栈：
            numStack.push(c);
        else:
            if(c == "+"):
                num1=int(numStack.pop());
                num2=int(numStack.pop());
                numStack.push(num1+num2);
            elif c == "-":
                num1=int(numStack.pop());
                num2=int(numStack.pop());
                numStack.push(num2-num1);
            elif c=="*":
                num1 = int(numStack.pop());
                num2 = int(numStack.pop());
                numStack.push(num2 * num1);
            elif c=="/":
                num1 = int(numStack.pop());
                num2 = int(numStack.pop());
                numStack.push(num2 / num1);
    return numStack.pop();


j = infixToPostfix("1+2*3+(4+5)");
print(j);


k = calculatePostfix(j);
print(k);






