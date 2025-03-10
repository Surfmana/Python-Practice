from 算法.data_structure.Stack import Stack
def parChecker(string):
    s = Stack();
    left = "([{";
    right = ")]}";
    for i in string:
        if i in left:
            s.push(i);
        elif i in right:
            if s.isEmpty():
                return False;
            else:
                if left.index(s.pop()) != right.index(i):
                    return False;

    if not s.isEmpty():
        return False;
    return True;



j = "(a+b)+(a+v){[]}";
print(parChecker(j));


