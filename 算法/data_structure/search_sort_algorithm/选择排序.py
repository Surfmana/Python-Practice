def choose_sort(alist):

    for i in range(len(alist)-1,0,-1):
        max_index = 0;
        for j in range(0,i+1):
            if(alist[j] > alist[max_index]):
                max_index = j;

        temp = alist[i];
        alist[i] = alist[max_index];
        alist[max_index] = temp;
    return alist;

alist = [9,8,7,6,5,4,3,2,1];
print(choose_sort(alist));
print(alist);
print(alist[0:1]);