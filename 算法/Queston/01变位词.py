#变位词即两个单词所用的字母组合一样但排序不一样
def confirmVString(s1,s2):#O(n^2)
    #思路一：进行逐字比较，每次比较都
    #一：先判断两个的长度是否相同
    if len(s1) != len(s2):
        return False;
    #声明一个visit数组，用于记录已经被访问过的位置
    visit = [0]*len(s1);
    for i in range(0,len(s1)):
        for j in range(0,len(s2)):
            if s1[i] == s2[j] and visit[j] ==0:
                visit[j] = 1;#说明匹配成功，下次不在访问这个字符
                break;#跳出第二层循环
    for i in visit:
        if i==0:
            return False;
    return True;

def confirmVStringBySort(s1,s2):
    #思路二：先将两个字符串按照同样的排序规则进行排序，然后在按位置比较各字符是否相同 O(n)
    if len(s1) != len(s2):
        return False;
    arr_s1 = list(s1);
    arr_s2 = list(s2);
    arr_s1.sort();
    arr_s2.sort();
    for i in range(0,len(s1)):
        if arr_s1[i] != arr_s2[i]:
            return False;
    return True;

def confirmVStringByCount(s1,s2):
    #思路三：使用两个计数器，用于分别统计两个字符串中各字母出现的次数，最后在逐个比较个字母出现的次数
    if len(s1) != len(s2):
        return False;
    arr_s1 = [0] * len(s1);
    arr_s2 = [0] * len(s2);
    for i in s1:
        index = ord(i) - ord('a');
        arr_s1[index] += 1;

    for j in s2:
        index = ord(j) - ord('a');
        arr_s2[index] += 1;

    for i in range(26):
        if arr_s1[i] != arr_s2[i]:
            return False;
    return True;


j = confirmVString("hello","holle");
print(j);

j=confirmVStringBySort("hello","hollp");
print(j);

j = confirmVStringBySort("hello","hellpo");
print(j);



