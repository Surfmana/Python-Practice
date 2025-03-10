def quick_sort(alist,left,right):
    if(left >= right):
        return;

    left_mark = left+1;
    right_mark = right;
    signal_num = alist[left];#确认首值为中值

    while(left_mark <= right_mark):#将要该部分已经分为已知大小的两部分
        while left_mark < len(alist)and (alist[left_mark] <= signal_num):
            left_mark += 1;

        while(right_mark >= 0) and (alist[right_mark] > signal_num):
            right_mark -= 1;

        alist[left] = alist[right_mark];
        alist[right_mark] = signal_num;


    quick_sort(alist,left,right_mark);
    quick_sort(alist,right_mark + 1,right);



alist = [9,8,7,6,5,4,3,2,1];
print(alist);
