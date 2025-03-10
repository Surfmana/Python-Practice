'''给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。'''

def deleteAndEarn(nums):
    #先进行排序

    list =sorted(nums);#用于临时去除的数组
    list1 = list.copy();
    #判断是否有相邻数
    while(isHave(list) !=-1):
        index = isHave(list);
        value = list[index];#用于记录要保留的数，既要删掉数组中存在与它相邻的所有数
        #去除其一
        #保留value
        list1 = removeValues(list,value-1);#小的必定存在
        if(value+1 in list):
            list1 = removeValues(list,value+1);

        #保留value-1;
        list = removeValues(list,value);

        if(sum(list) <= sum(list1)):
            list = list1;

    return sum(list);




def isHave(nums):#判断是否有相邻数
    for i in range(0,len(nums)-1):
        if(nums[i]+1 == nums[i+1] ):
            return i+1;
    return -1;

def removeValues(nums,values):#去除数组中所有值为value的值
    sum = 0;
    list = nums.copy();
    for i in range(0,len(list)):
        if(list[i] == values):
            sum +=1;
    for i in range(sum):
        list.remove(values);
    return list;

nums = [2,2,3,3,3,4];
print(deleteAndEarn(nums));
