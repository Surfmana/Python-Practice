from 算法.data_structure.Stack import  Stack

def DecimalCovertBinary(num):#从用除2取余的逆来进行计算
    s = Stack();#用于存储余数
    mod = num % 2;
    count = num // 2;#用于存储整除的结果
    result = ""#用于储存结果
    s.push(mod);
    while(count != 0):
        mod = count % 2;
        count//= 2;
        s.push(mod);
    while(not s.isEmpty()):
        j = s.pop();
        result += str(j);
    return result;

def baseConverter(decNum,base):#实现任意16以下进制的转换
    digits="0123456789ABCDEF";#用于确定余数对应的进制数
    result="";#用于记录最终结果
    s = Stack();#用于存储余数的结果
    mod = decNum % base;
    count = decNum // base;
    s.push(mod);
    while(count != 0):
        mod = count % base;
        count //= base;
        s.push(mod);
    while(not s.isEmpty()):
        i = s.pop();
        res = digits[i];
        result += res;
    return result;








n = DecimalCovertBinary(100);
print(n);

m = baseConverter(100,16);
print(m);

