'''
动态规划的实质类似于缓存的思想，解决更大问题的规模可以使用先前已经解决好的小规模的最优解的数据进行辅助计算以得到该规模的最优解，
本质依旧是贪心算法的一种
'''

def minCoin(coins,money):#假设coins的排序为从小到大
    checkList = [0,1];
    #求解从1一直循环到money，求出每一个找零的最优解
    for count in range(2,money+1):
        #先初始化每个金额的解的最大值
        min_count = count;
        #然后再去判断一次减去coins的数额，再查表，然后得到4个结果，去最小值最为最优解
        for  i in coins:
            if count - i < 0:
                break;

            if(count == i):
                min_count = 1;

            if(checkList[count - i] + 1 < min_count):
                #更新
                min_count=checkList[count-i]+1;
        checkList.append(min_count);
    return checkList[money];


def print_minCoin(coins,money):
    checkList = [0,1];#用于存放每个数字的最优解

    dic = developDic(coins);
    dic[coins[0]] = 1;#用于记录1的最优组合

    printList = [developDic(coins),dic];#用于存放每个数字的最有解的组合，存放的内容为一个字典
    #求解从1一直循环到money，求出每一个找零的最优解
    for count in range(2,money+1):
        #先初始化每个金额的解的最大值
        min_count = count;
        dic = developDic(coins);#生成该数字的最优解组合
        index = count;#用于记录上一个最优解的下标
        #然后再去判断一次减去coins的数额，再查表，然后得到4个结果，去最小值最为最优解
        for  i in coins:
            if count - i < 0:
                break;
            if(count == i ):
                dic[i] = 1;
                index = count;
                min_count = 1;
                break;

            if(count == 2):
                dic[i]=2;
                index = count ;

            if(checkList[count - i] + 1 < min_count ):
                #更新
                min_count=checkList[count-i]+1;
                index = count - i;
                basic_change = i;

        if(index != count):#说明是可以通过上文的信息得到的最优解组合
            dic = printList[index].copy();
            dic[basic_change] += 1;

        printList.append(dic);
        checkList.append(min_count);

    return printList[money];


def developDic(coins):
    dic = {};
    for i in coins:
        dic[i] = 0;
    return dic;


coins = [1,5,10,21,20,50,100];
print(minCoin(coins,2));
print(print_minCoin(coins,60));

