from tkinter import *
from tkinter.messagebox import *
import  copy
root = Tk()
root.title(" 推箱子--夏敏捷")

imgs= [PhotoImage(file='bmp\\Wall.gif'),
       PhotoImage(file='bmp\\Worker.gif'),
       PhotoImage(file='bmp\\Box.gif'),
       PhotoImage(file='bmp\\Passageway.gif'),
       PhotoImage(file='bmp\\Destination.gif'),
       PhotoImage(file='bmp\\WorkerInDest.gif'),
       PhotoImage(file='bmp\\RedBox.gif') ]
#0代表墙，1代表人，2代表箱子，3代表路，4代表目的地
#5代表人在目的地，6代表放到目的地的箱子
Wall = 0
Worker = 1 
Box = 2
Passageway = 3
Destination = 4
WorkerInDest = 5
RedBox = 6
#原始地图
myArray1 = [[0,3,1,4,3,3,3],
           [0,3,3,2,3,3,0],  
           [0,0,3,0,3,3,0],
           [3,3,2,3,0,0,0],
           [3,4,3,3,3,0,0],
           [0,0,3,3,3,3,0],
           [0,0,0,0,0,0,0]]
#绘制整个游戏区域图形
def drawGameImage( ):
    global x,y
     
    for i in range(0,7) :#0--6
       for j in range(0,7) :#0--6
            if myArray[i][j] == Worker :
               x=i  #工人当前位置(x,y)
               y=j
               print("工人当前位置:",x,y)
            img1= imgs[myArray[i][j]]
            cv.create_image((i*32+20,j*32+20),image=img1)
            cv.pack()
    #print (myArray)

def callback(event) :#按键处理
    global x,y,myArray
    print ("按下键：", event.char)
    KeyCode = event.keysym
    #工人当前位置(x,y)	        
    if KeyCode=="Up":#分析按键消息
    #向上
            x1 = x;
            y1 = y - 1;
            x2 = x;
            y2 = y - 2;
            #将所有位置输入以判断并作地图更新
            MoveTo(x1, y1, x2, y2);
    #向下
    elif KeyCode=="Down":
            x1 = x;
            y1 = y + 1;
            x2 = x;
            y2 = y + 2;
            MoveTo(x1, y1, x2, y2);
    #向左
    elif KeyCode=="Left":
            x1 = x - 1;
            y1 = y;
            x2 = x - 2;
            y2 = y;
            MoveTo(x1, y1, x2, y2);
    #向右
    elif KeyCode=="Right":
            x1 = x + 1;
            y1 = y;
            x2 = x + 2;
            y2 = y;
            MoveTo(x1, y1, x2, y2);
    elif KeyCode=="space": #空格键
       print ("按下键：空格", event.char)
       myArray=copy.deepcopy(myArray1)  #恢复原始地图
       drawGameImage( )

#判断是否在游戏区域
def IsInGameArea(row, col) :
    return (row >= 0 and row < 7 and col >= 0 and col < 7) 
def MoveTo(x1, y1, x2, y2) :
        global x,y
        P1=None
        P2=None
        if IsInGameArea(x1, y1) : #判断是否在游戏区域
            P1=myArray[x1][y1];
        if IsInGameArea(x2, y2) :
            P2 = myArray[x2][y2]
        if P1 ==  Passageway :#P1处为通道
            MoveMan(x,y);
            x = x1; y = y1;
            myArray[x1][y1] =  Worker; 
        if P1 ==  Destination :#P1处为目的地
            MoveMan(x, y);
            x = x1; y = y1;
            myArray[x1][y1] =  WorkerInDest;
        if P1 ==  Wall or  not IsInGameArea(x1, y1) :
            #P1处为墙或出界
            return;
        
        #以下P1处为箱子
        if P1 ==  Box  :#P1处为箱子
           if P2 ==  Wall or  not IsInGameArea(x1, y1) or P2 ==  Box :##P2处为墙或出界
              return;
        

        #P1处为箱子,P2处为通道
        if P1 ==  Box and P2 ==  Passageway :
            MoveMan(x, y);
            x = x1; y = y1;
            myArray[x2][y2]= Box;
            myArray[x1][y1] =  Worker;
        if P1 ==  Box and P2 ==  Destination :
            MoveMan(x, y);
            x = x1; y = y1;
            myArray[x2][y2]= RedBox;
            myArray[x1][y1] =  Worker;
        #P1处为放到目的地的箱子,P2处为通道
        if P1 ==  RedBox and P2 ==  Passageway :
            MoveMan(x, y);
            x = x1; y = y1;
            myArray[x2][y2] =  Box;
            myArray[x1][y1] =  WorkerInDest;
        #P1处为放到目的地的箱子,P2处为目的地
        if P1 ==  RedBox and P2 ==  Destination :
            MoveMan(x, y);
            x = x1; y = y1;
            myArray[x2][y2] =  RedBox;
            myArray[x1][y1] =  WorkerInDest;
        drawGameImage()
        #这里要验证是否过关
        if IsFinish() :
            showinfo(title="提示",message=" 恭喜你顺利过关" ) 
            print("下一关")

def  MoveMan(x, y) :
    if myArray[x][y] == Worker :
        myArray[x][y] = Passageway;
    elif myArray[x][y] == WorkerInDest :
        myArray[x][y] = Destination;

           
def IsFinish( ):#验证是否过关
    bFinish = True;
    for i in range(0,7) :#0--6
       for j in range(0,7) :#0--6
            if  (myArray[i][j] == Destination
                   or myArray[i][j] == WorkerInDest) :
                bFinish = False;
    return bFinish;

 

def drawQiPan( ) :#画棋盘
    for i in range(0,15) :
        cv.create_line(20,20+40*i,580,20+40*i,width=2)
    for i in range(0,15) :
        cv.create_line(20+40*i,20,20+40*i,580,width=2)
    cv.pack()
    
 
def print_map( ) :#输出map地图
    for i in range(0,15) :#0--14 
       for j in range(0,15) :#0--14
           print (map[i][j],end=' ')
       print ('w')
    
cv = Canvas(root, bg = 'green', width = 226, height = 226)
#drawQiPan( )
myArray=copy.deepcopy(myArray1) 
drawGameImage()

cv.bind("<KeyPress>", callback)
cv.pack()
cv.focus_set() #将焦点设置到cv上
root.mainloop()
