from 算法.data_structure.Queue import Queue

def hotPotato(nameList,num):#初始版
    simQuenen = Queue();#用于存储人名。同时通过入队与出队实现每传递num次就少一个人
    for i in nameList:
        simQuenen.enqueue(i);

    while simQuenen.size() > 1:
        for i in range(num):
            simQuenen.enqueue(simQuenen.dequeeu());#进行num次传递
        simQuenen.dequeeu();#num次传递后队头的人出局
    return simQuenen.dequeeu();

nameList=[1,2,3,4,5,6,7,8,9];
j = hotPotato(nameList,3);
print(j);
