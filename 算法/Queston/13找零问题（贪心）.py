'''
    贪心算法：通过实现局部最优解以实现整体最优解
    对于找零问题：可以通过通过尽可能使用大值的数额进行拼凑，这样所得到的第一个凑齐的组合必是最优的解之一
'''
def minCoin(coins,money,count):#其中coins为货币的组成问题，money为要找零的数额,count为要找零对应的数额的钱数
    if money == 0:
        return count;

    if money < 0:#如果组成的数额小于零，说明这种组合无法找零，那就规定为最大值
        return None;

    min_count = count;#用来存储最小结果
    min_len = 2*money+1;#用来存储最小结果的长度

    for i in range(len(coins)):
        temp_count = count.copy(); #临时存储count的
        temp_count[i] += 1;
        res_count = minCoin(coins,money-coins[i],temp_count);
        if(res_count is None):
            continue;
        sumMoney = sum_money(coins,res_count);
        if(sumMoney == money):#已经找到最忧解
            return res_count;
        if(sum(res_count) <= min_len):#如果货币数小于当前的最小货币数，则进行替换
            min_count = res_count;
            min_len = sum(res_count);

    return min_count;

def sum_money(coins,count):
    sum = 0;
    for i in range(len(coins)):
        sum += coins[i]*count[i];
    return sum;


coins = [25,10,5,1];
count = [0 for i in range(len(coins))];
money = 51;
login = [0 for i in  range(money)];

minCoins = minCoin(coins,money,count);
print(minCoins);
