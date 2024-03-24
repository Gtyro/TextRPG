'''
主程序入口
'''
import sys
import time
from collections import deque

import pygame

from MainMenu import main_menu_scr

def blink_text(text, duration=5):
    while True:
        # ANSI转义码：\033[属性;颜色;背景m 文本 \033[0m
        blink = "\033[5m"  # 5表示闪烁效果
        reset = "\033[0m"  # 重置属性，取消闪烁

        print(f"{blink}{text}{reset}", end="", flush=True)

        # 等待一段时间，模拟闪烁效果
        time.sleep(duration)

        # 清除闪烁文本
        print("\033[2K", end="", flush=True)
        print("\r", end="", flush=True)
    
def init():
    pygame.init()
    
    clock = pygame.time.Clock()
    clock.tick(30)
    screen = pygame.display.set_mode((1024, 512))
    pygame.display.set_caption('TextRPG')
    return screen

def load_map_and_draw(screen):
    # 读取地图文件
    map_filename = "WorldMap.map"
    try:
        with open(map_filename, "r") as file:
            map_data = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: Cannot find file '{map_filename}'")
        return

    # 确定行数和列数
    c = len(map_data)
    r = len(map_data[0])

    # 绘制白色背景
    screen.fill((255, 255, 255))

    # 设置单元大小和字体
    unit_size = 32
    font = pygame.font.SysFont('simHei', unit_size)

    # 计算地图绘制区域的大小
    map_area_width = r * unit_size
    map_area_height = c * unit_size

    # 计算地图绘制区域的左上角坐标
    map_area_x = (screen.get_width() - map_area_width) // 2
    map_area_y = (screen.get_height() - map_area_height) // 2

    # 绘制黑色区域作为地图背景
    pygame.draw.rect(screen, (0, 0, 0), (map_area_x, map_area_y, map_area_width, map_area_height))

    # 在黑色区域中绘制地图内容
    for i in range(c):
        for j in range(r):
            char = map_data[i][j]
            if char != "地":
                text_surface = font.render(char, True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.topleft = (map_area_x + j * unit_size, map_area_y + i * unit_size)
                screen.blit(text_surface, text_rect)

    # 更新屏幕显示
    pygame.display.flip()

def templatePage(screen:pygame.Surface, pages:list, addpages)->list:
    #初始化
    options = ["TODO"]
    selected_option = 0

    #循环体
    running = True

    while running:
        #接受操作
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option -= 1
                elif event.key == pygame.K_DOWN:
                    selected_option += 1
                elif event.key == pygame.K_SPACE:
                    pass

        selected_option %= len(options)

        # 清屏
        screen.fill((0, 0, 0))

        # 绘制
        for i in range(len(options)):
            text = options[i]
            if i == selected_option:
                color = (255, 255, 255)  # 白色
            else:
                color = (128, 128, 128)  # 灰色
            # dispText(screen, text, bottomleft=(0, 50 + i * 50), color=color)

        pygame.display.flip()

if __name__ == "__main__":
    pages = deque()
    addpages = {
    }
    
    screen = init()
    main_menu = main_menu_scr(addpages)
    pages.append(main_menu)
    args = []
    while len(pages)>0:
        args = pages[-1].disp(screen, pages, addpages, args)
    pygame.quit()
    sys.exit()