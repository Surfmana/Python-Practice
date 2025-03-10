def binary_search(alist,data):
    first = 0;
    last = len(alist)-1;
    mid = (first+last)//2;
    while (first <= last):
        if(alist[mid] == data):
            return mid;
        else:
            if(alist[mid] < data):
                first = mid +1;
            else:
                last = mid - 1;

            mid = (first + last) // 2;

    return -1;

list = [1,3,5,7,9];
print(binary_search(list,3));


