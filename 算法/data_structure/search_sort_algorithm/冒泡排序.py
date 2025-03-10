def bubble_sort(alist):
    for i in range(len(alist)-1,0,-1):
        for j in range(0,i):
            if(alist[j] > alist[j+1]):
                temp = alist[j];
                alist[j] = alist[j+1];
                alist[j+1] = temp;
    return alist;

alist = [9,8,7,6,5,4,3,2,1];
print(bubble_sort(alist));
print(alist);