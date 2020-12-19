import pygame
from sys import exit
import random


class Point():
    row = 0
    clo = 0

    def __init__(self, row, clo):
        self.row = row
        self.clo = clo

    def copy(self):
        return Point(row=self.row, clo=self.clo)


# 初始化
pygame.init()
width = 1280
hight = 720

ROW = 36
CLO = 64

direct = 'left'
window = pygame.display.set_mode((width, hight))
pygame.display.set_caption('ManicShooter')

# 身体坐标定在最下方的中间
body = Point(row=int(ROW - 3), clo=int(CLO / 2))


# 这是身体的颜色
body_color = (0, 158, 128)

# 需要执行很多步画图操作 所以定义一个函数
def rect( point, color):
    # 定位 画图需要left和top
    left = point.clo * width / CLO
    top = point.row * hight / ROW
    # 将方块涂色
    pygame.draw.rect(window, color, (left, top, width / CLO, hight / ROW))
quit = True
clock = pygame.time.Clock()

# 移动函数

key_right_status = False
key_left_status = False
key_up_status = False
key_down_status = False

def move() :
    if key_right_status:
        body.clo += 1
    if key_left_status:
        body.clo -= 1
    if key_down_status:
        body.row += 1
    if key_up_status:
        body.row -= 1





# 射击函数

shoot = False

cum = False

i = 1



while quit:

    # 帧率

    clock.tick(30)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
        elif event.type == pygame.KEYDOWN:
            # 这里小细节蛇不可以直接左右上下 要判断当前是在什么状态下前行
            if event.key == pygame.K_w:
                key_up_status = True
            if event.key == pygame.K_a:
                key_left_status = True
            if event.key == pygame.K_d:
                key_right_status = True
            if event.key == pygame.K_s:
                key_down_status = True
            if event.key == pygame.K_SPACE:
                shoot = True
                cum = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                key_up_status = False
            if event.key == pygame.K_a:
                key_left_status = False
            if event.key == pygame.K_d:
                key_right_status = False
            if event.key == pygame.K_s:
                key_down_status = False


    # 吃东西

    move()

    pygame.draw.rect(window, (245, 135, 155), (0, 0, width, hight))
    rect(body , body_color)


    if cum :
        bullerow = body.row-1
        bulleclo = body.clo
        cum = False
        i = 0

    if shoot :

        a = Point(bullerow - i, bulleclo)
        i += 1
        rect(a, body_color)




    pygame.display.flip()