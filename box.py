from random import randint
'''
一个简易的扫雷游戏
玩家输入坐标值和相应的操作代码完成相应的操作，例：2,5,0 
2,5 为坐标点   0 代表点击(1为标记地雷)  
'''
def prepre_list():    
    # 创建一个二维列表
    return [[""]*10 for i in range(10)]

def set_one_num(i,j):
    # 根据目标点周围的地雷的数量确定目标点的数字
    r = [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]
    sum = 0
    for x in r:
        if 10 > x[0] > -1 and 10 > x[1] > -1:
            if h[x[0]][x[1]] == "[x]":
                sum += 1
    h[i][j] = "["+str(sum)+"]"  

def set_m(num):
    # 随机位置设定最多num数量的地雷   
    for x in range(num):
        h[randint(0,9)][randint(0,9)] = "[x]" 

def set_all_num():
    # 将界面上所有的空的位置确定好相应的数字
        for i in range(10):
            for j in range(10):
                if h[i][j] == "":
                    set_one_num(i,j)
def show(h):
    # 遍历显示目标列表
    for j in h:
        print(j)

def set_position_message():
    # 设置 temp中的每个元素的信息
    for i in range(10):
        for j in range(10):
            temp[i][j] = str(i)+"-"+str(j)

def show_around(x,y):
    # 显示目标点周围的所有未被显示的元素
    p = [[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]]
    for i in p:
        if 10 > i[0] > -1 and 10 > i[1] > -1:
            if "-" in temp[i[0]][i[1]]:
                temp[i[0]][i[1]] = h[i[0]][i[1]]
                if h[i[0]][i[1]] == "[0]":
                    show_around(i[0],i[1])
def judge(lst):
    # 根据玩家输入的信息完成相应的操作
    x, y, action = int(lst[0]), int(lst[1]), int(lst[2])
    if action == 1:
        temp[x][y] = "[M]"
    elif h[x][y] == "[x]":
        print("失败了，游戏结束") 
        show(h)
        return 0
    elif h[x][y] == "[0]":
        temp[x][y] = "[0]"
        show_around(x,y)
    else:
        temp[x][y] = h[x][y]

if __name__ == "__main__":
    # 展示二维列表
    temp = prepre_list()
    set_position_message()
    show(temp)
    # 存储信息的二维列表
    h = prepre_list()
    set_m(15)
    set_all_num()
    # 进行游戏
    while True:
        target = input("请输入x,y,操作代码（1:标记地雷 0:点击该位置):").split(",") 
        result = judge(target)
        if result == 0:
            break      
        show(temp)
