from 算法.data_structure.Queue import Queue
import random

class Printer():#打印机的几个重要参数：打印机的打印速度 打印任务 打印时间
    def __init__(self,pageRate):#初始化相关的参数
        self.pageRate = pageRate;#单位为页/分钟
        self.currentTask = None;#某个时间结点的任务
        self.timeRemaining = 0;#完成打印任务还所需的时间

    def startTask(self,nextTask):#开启新工作 其中nextTask为Task对象的实例
        self.currentTask = nextTask;
        self.timeRemaining = nextTask.getPages()*60 / self.pageRate;#由于timeRemaining的单位为秒

    def tick(self):#表示正在工作
        if self.currentTask != None:
            self.timeRemaining -=1 ;#在以秒流逝的过程中的完成任务的所需时间减1
            if(self.timeRemaining <= 0):#表明打印任务时间结束
                self.currentTask = None;

    def isBusy(self):#判断打印机是否空闲
        if(self.currentTask is None):
            return False;
        return True;

class Task():#任务类：重要参数: 页数（随机生成） 生成作业的时间戳
    def __init__(self,timestamp):
        self.page = random.randrange(1,21);#假如作业也得页数的范围为1到20页，且概率相等
        self.timestamp = timestamp;#获取时间戳

    def getPages(self):
        return self.page;

    def getTimestamp(self):
        return self.timestamp;

    def waitTime(self,currentTime):#计算等待时间
        return currentTime - self.timestamp;


def newPtrinTask():#用于模拟作业的生成
    if(random.randrange(1,181) == 90):
        return True;
    return False;


def simulate(time,pageRate):#用于模拟打印机打印场景 time:工作时间长短 pageRate:打印机效率
    newPtrinter = Printer(pageRate);
    waitTimes = [];#用于记录每个任务的等待时间
    taskQueue = Queue();#用于记录任务
    for currentTime in range(time):
        if (newPtrinTask()):
            task = Task(currentTime);
            taskQueue.enqueue(task);

        if(not newPtrinter.isBusy()) and (not taskQueue.isEmpty()):
            newtask = taskQueue.dequeeu();
            waitTimes.append(newtask.waitTime(currentTime));
            newPtrinter.startTask(newtask);

        newPtrinter.tick();
    sum = 0;
    for times in waitTimes:
        sum += times;
    averageTime = sum/len(waitTimes) ;
    print("Average wait %7.2f seconds %3d task is remaining " % (averageTime,taskQueue.size()));


for i in range(100):#模拟进行10次
    simulate(3600,10);











