
def moveDist(height,fromPole,toPole):
    print(f"Moving disk[{height}] from {fromPole} to {toPole}")

def moveTower(height,fromPole,withPole,toPole):#四个参数分别为层数，当前层数的起始柱，目标柱，经过柱
    if height > 0:
        moveTower(height-1,fromPole,toPole,withPole);
        moveDist(height,fromPole,toPole);
        moveTower(height-1,withPole,fromPole,toPole);


moveTower(64,"#1","#2","#3");