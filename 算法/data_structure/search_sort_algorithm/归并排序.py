def merge_sort(alist):
    if len(alist) <= 1:
        return alist;
    left = merge_sort(alist[:len(alist)//2]);#得到向左归并好的数列
    right = merge_sort(alist[len(alist)//2:]);#得到右归并好的数列

    left_index = 0;#用于记录左数列的位置
    right_index = 0;#用于记录右数列的位置

    new_list = [];
    while (left_index < len(left)) and (right_index < len(right)):
            if(left[left_index] <= right[right_index]):
                new_list.append(left[left_index]);
                left_index += 1;
            else:
                new_list.append(right[right_index]);
                right_index += 1;

    while (left_index < len(left)):#若左边有剩余，则将左边的数组全部添加到新数组去
        new_list.append(left[left_index]);
        left_index +=1;

    while (right_index < len(right)):
        new_list.append(right[right_index]);
        right_index += 1;

    return new_list;

alist = [9,8,7,6,5,4,3,2,1];
print(merge_sort(alist));
print(alist);