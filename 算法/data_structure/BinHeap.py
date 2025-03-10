class Binheap:
    def __init__(self):
        self.heap = [0];
        self.size = 0;

    def insert(self,data):
        self.heap.append(data);#插入大根堆里面
        self.size = self.size+1;#个数加一
        self.pearUp(self.size);

    def pearUp(self,index):#用于更新后的大根堆，其中i时对应的次序
        i = index;
        while i > 0:
            if(self.heap[i] > self.heap[i // 2] ):
                temp = self.heap[i];
                self.heap[i] = self.heap[i // 2];
                self.heap[i // 2] = temp;
            i = i // 2;

    def delMax(self):#删除最大值，即删除根节点，此时需要删除根结点
        revital = self.heap[1];#获取大根堆的根值
        #跟新根堆
        self.heap[1] = self.heap[self.size];#将最后子节点移上来
        self.heap.pop();
        self.size = self.size - 1;
        #更新大根堆，需要下沉
        self.pearDown(1);
        return revital;

    def pearDown(self,k):
        i = k;
        while (i * 2 <= self.size):
            index = i*2;#获取左孩子的坐标
            if (index + 1 <= self.size) and(self.heap[index] < self.heap[index+1]):
                index = index+1;#如果右孩子比左孩子大，则要于左孩子交换
            if(self.heap[i] < self.heap[index]):
                #如果比最大的孩子小，则要进行交换
                temp = self.heap[i];
                self.heap[i] = self.heap[i+1];
                self.heap[i+1] = temp;
            i = index;#进行索引移位

    def buildHeap(self,lst):#建立二叉堆
        self.size = len(lst);
        self.heap = self.heap[0] + lst[:];
        index = self.size // 2;#先获取该堆的非叶子结点的位置，进行每个小根堆的更新
        print(len(self.heap),i);
        while(index > 0):#更新每个小根堆
            print(self.heap,index);
            self.pearDown(index);
            index = index - 1;
        print(self.heap,index);



