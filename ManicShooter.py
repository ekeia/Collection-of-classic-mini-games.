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
width = 640
hight = 640

ROW = 64
CLO = 64

direct = 'left'
window = pygame.display.set_mode((width, hight))
pygame.display.set_caption('贪吃蛇游戏')

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
while quit:
    # 帧率

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
        elif event.type == pygame.KEYDOWN:
            # 这里小细节蛇不可以直接左右上下 要判断当前是在什么状态下前行
            if event.key == pygame.K_w:
                body.row -= 1
            if event.key == pygame.K_a:
                body.clo -= 1
            if event.key == pygame.K_d:
                body.clo += 1
            if event.key == pygame.K_s:
                body.row += 1
            if event.key == pygame.K_SPACE:
                pause = not pause


    # 吃东西



    pygame.draw.rect(window, (245, 135, 155), (0, 0, width, hight))
    rect(body , body_color)



    pygame.display.flip()