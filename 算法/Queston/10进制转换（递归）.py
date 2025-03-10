'''
    递归三要数：1、有结束条件，级最小规模的解决方案 ； 2、能够调用自身，级问题能够化为更小规模的同类问题；3、能够向最小规模问题演进的趋势

'''
def toString(num,base):
    covString="0123456789ABCDEF";
    if(num < base):
        return covString[num];
    return toString(num//base,base) + covString[num%base];

print(toString(100,16))