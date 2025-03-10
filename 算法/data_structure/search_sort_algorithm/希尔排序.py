def shell_sort(alist):
    gap = len(alist)//2;
    while(gap>0):
        print("间隔为%d的排序过程" % gap);
        for i in range(gap):#对每个子数列进行排序
            for j in range(i+gap,len(alist),gap):#对子数列进行插入排序,有序区依旧是以第一个元素开始
                temp = alist[j];
                index = j - gap;#用于确定子数列的有序区
                while (index >= 0) and (alist[index] > temp):
                    alist[index+gap] = alist[index];
                    index -= gap;
                alist[index + gap] = temp;
            print_alist(alist,gap,i);
        gap //=2;
        print("");

    return alist;


def print_alist(alist,gap,first):
    new_list = [];
    for i in range(first,len(alist),gap):
        new_list.append(alist[i]);
    print(new_list);


alist = [9,8,7,6,5,4,3,2,1];
print(shell_sort(alist));
print(alist);