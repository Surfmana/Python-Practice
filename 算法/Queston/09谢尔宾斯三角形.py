'''
    大致思路为：通过三点填充来绘制三角形，省区计算角度的事情
    而点通过字典来分别表示左、顶、右三个顶点的坐标
    计算点则通过getMid函数进行计算
'''
import turtle
t = turtle.Turtle();

def getMid(p1,p2):#坐标可以理解为元组
    return((p1[0]+p2[0])/2,(p1[1]+p2[1])/2);

def drawTrangle(point,color):#绘画三角形
    t.fillcolor(color);
    t.penup();
    t.goto(point["top"]);
    t.pendown();
    t.begin_fill();
    t.goto(point["left"]);
    t.goto(point["right"]);
    t.goto(point["top"]);
    t.end_fill();

def pointSet(p1,p2,p3):#用于生成点的字典
    return {"left":p1,"top":p2,"right":p3}

def selTrangle(degree,point):#degree为谢尔宾斯三角形的阶 point为三个点的坐标
    color = ["red","yellow","green","blue","white","black"];
    drawTrangle(point,color[degree % 6]);
    p1 = getMid(point["left"],point["top"]);#用于计算左边中点
    p2 = getMid(point["top"],point["right"]);#右边中点
    p3 = getMid(point["left"],point["right"]);#下边重点
    if (degree > 0):
        selTrangle(degree-1,pointSet(p1,point["top"],p2));#顶部的三角形
        selTrangle(degree-1,pointSet(point["left"],p1,p3));#左边的三角形
        selTrangle(degree-1,pointSet(p3,p2,point["right"]));#右边的三角形

point = {"left":(-200,-100),"top":(0,200),"right":(200,-100)};
selTrangle(5,point);
turtle.done();