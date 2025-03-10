import turtle

t = turtle.Turtle;
t.shape("turtle");


class Maze():
    def __init__(self,fileName):#通过文本文件获取迷宫：
        rowSize = 0;
        columnSize = 0;
        MazeList = [];
        MazeFile = open("Maze.txt","r");#规定以 + 代表墙壁，以“ ”代表通道 以 s 代表起始点
        for line in MazeFile:
            column = 0;#每完读一行，列都要重新归为
            rowList = [];#用来记录每行的字符
            for ch in line[:-1]:
                rowList.append(ch);
                if(ch == 's'):
                    self.startRow = rowSize;
                    self.startColumn = col;
                column += 1;
            rowSize += 1;
            MazeList.append(rowList);
            columnSize = len(rowList);


