N = int(input());
A = input();
B = input();
#  格式化输入，得到A的数组，即奶牛的初始队列
A = A.split();
A = [int(i) for i in A];

#得到体检官的要求队列
B = B.split();
B = [int(i) for i in B];
count = { i:0 for i in range(int(N)+1)};#得到一个记录字典
#直接暴力拆解，通过引用一个字典，然后将所有的翻转可能穷举，然后进行与B进行比较，得到相同的个数，则在字典对应的值+1
for i in range(N):
    for j in range(i,N):
        temp1 = A[i:j+1];
        temp1.reverse();
        temp = A[0:i] + temp1 + A[j+1:];#得到翻转序列
        sum = 0;#用于记录该翻转共有多少头牛可以被检查
        for k in range(N):
            if (temp[k] == B[k]):
                sum += 1;#说明索引k的牛可以体检，则sum+1
        count[sum] += 1;#说明这种翻转共有sum头牛可以体检，因此可以

for i in count.values():
    print(i ,"\n");


