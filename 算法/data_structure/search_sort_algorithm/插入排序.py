def insert_sort(alist):
    for i in range(1,len(alist)):#假设起始的有序区为从0开始
        temp = alist[i];
        j=i-1;#从有序区的末端开始寻找合适的区间
        while(j >= 0) and (alist[j] > temp ):
            alist[j+1] = alist[j];
            j-=1;
        alist[j+1] = temp;
    return alist;

alist = [9,8,7,6,5,4,3,2,1];
print(insert_sort(alist));
print(alist);


