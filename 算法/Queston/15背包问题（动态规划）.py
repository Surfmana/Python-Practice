'''
背包问题：设有一个小偷，他的背包只能承受 m kg的重量，现有n件不同重量，且价值不同的宝物，问求出此时他能盗取的最大的宝物价值数
'''
def maxValue(pressure,weight):#pressure用字典存储，weight为整数
#可以使用动态规划进行解题，其中使用列表来记录每个重量下的最大价值宝物，然后通过比较添加不同的宝物的价值取最大值作为结果
#1、声明列表用于存储
    count_value = [0];#当weight为0时，价值量也为0
    visit = [[],]#用于记录每个重量的组合
#2、统计每个重量的最忧解
    for wgt in range(1,weight+1):
        max_value = 0;#同于统计每个重量下的最大价值量
        max_visit = [];#用于记录每个重量下的最大价值的组合
        for value in pressure.keys():#获取添加每件宝物的价值，然后取最大值
           temp_visit = [];
           if(wgt - pressure[value] < 0):
                temp_value = 0;
           elif (wgt - pressure[value] == 0):
                temp_value = value;
                temp_visit.append(value);
           else:
                isHave = value in visit[wgt - pressure[value]];#用于判断该价值是否在该组合里
                if(isHave):
                    temp_value = count_value[wgt - pressure[value]];#若该宝物已在前面的最优解的组合里
                    temp_visit = visit[wgt - pressure[value]].copy();#那么该组合与上一个组合相同
                else:
                    temp_value = count_value[wgt - pressure[value]] + value;#用于记录每重量下的价值量，前提是该宝物还不在之前的最优解里
                    temp_visit = visit[wgt - pressure[value]].copy();
                    temp_visit.append(value);
           if(temp_value > max_value):
               max_value = temp_value;
               max_visit = temp_visit;

        count_value.append(max_value);
        visit.append(max_visit);
#3、返回最有解
    print(visit[weight]);
    return count_value[weight];

pressure = {1:1,2:2,3:3,4:5};
print(maxValue(pressure,4));



