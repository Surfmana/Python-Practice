#给出一个三角形，给出从顶端到地段的数字和最大的路径


#思路：使用一个二维数组用于储存该三角形，
Num = [];#用于存放数据三角形
Path = [];#用于存放路径
Mem = [];#用于存放最大值信息
N = int(input());#输入的行数
for i in range(N):
    scanf = input().split();
    scanf = [int(i) for i in scanf];
    Num.append(scanf);

for i in range(len(Num)):#用于获取路径和最大值的存储空间
    Path.append([0 for i in range(len(Num[i]))]);
    Mem.append([0 for i in range(len(Num[i]))]);

Mem[0][0] = Num[0][0];#初始化Mem数组
for i in range(1,N):
    for j in range(len(Num[i])):
        sum = 0;
        if(j == 0):
            sum = Mem[i-1][j]+Num[i][j];
            Path[i][j] = Num[i-1][j];
        elif(j == i):
            sum = Mem[i-1][j-1]+Num[i][j];
            Path[i][j] = Num[i-1][j-1];
        else:
            maxNum = max(Mem[i-1][j-1],Mem[i-1][j]);
            sum = maxNum + Num[i][j];
            if(Mem[i-1][j-1] == maxNum):
                Path[i][j]= Num[i-1][j-1];
            else:
                Path[i][j]=Num[i-1][j];

        Mem[i][j] = sum;

max = Mem[N-1][0];
index = 0;
for i in range(1,N):
    if(Mem[N-1][i] > max):
        max = Mem[N-1][i];
        index = i;


def print_path(Path,index,level):
        if(level <= 0):
            print(Num[0][0]," ");
            return;
        num = Path[level][index];
        if (index < level)and(Num[level-1][index] == num):
            print_path(Path,index,level-1);

        elif(index > 0 )and (Num[level-1][index-1] == num):
            print_path(Path,index-1,level-1);

        elif(index == level):
            print_path(Path,index-1,level-1);
        elif(index == 0):
            print_path(Path,index,level);
        print(Num[level][index]," ");

print_path(Path,index,N-1);