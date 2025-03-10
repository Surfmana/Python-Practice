import turtle

t = turtle.Turtle();

def tree(len):
    if(len > 5):
        t.forward(len);

        t.left(20);
        tree(len-15);#画出左子树

        t.right(40);
        tree((len-15));

        t.left(20);#回正
        t.backward(len);#回到每次画完原来的位置



t.left(90);
t.penup();
t.backward(100);
t.pendown();
t.pencolor("green");
t.pensize(2);
tree(75);
t.hideturtle();
turtle.done();

