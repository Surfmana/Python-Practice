from 算法.data_structure.Deque import Deque

def palchecker(str):
    s = Deque();
    for c in str:#获取字符串的双端队列
        s.addFront(c);
    while(s.size()>1):
        c1 = s.removeRear();
        c2 = s.removeFront();
        if(c1 != c2):
            return False;
    return True;

c = "113311";
print(palchecker(c));