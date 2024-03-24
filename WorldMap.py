import random

import pygame

from Village import village_page
from Battle import BattleSrc

class WorldMap_page:
    def __init__(self, addpages) -> None:
        addpages[self] = [village_page(addpages), BattleSrc(addpages)]
        # 读取地图文件
        map_filename = "WorldMap.csv"
        try:
            with open(map_filename, "r") as file:
                self.map_data = [line.strip().replace(",",'') for line in file.readlines()]
        except FileNotFoundError:
            print(f"Error: Cannot find file '{map_filename}'")
            return

        # 确定行数和列数
        c = len(self.map_data)
        r = len(self.map_data[0])
        self.player_pos = [(x,y) for x in range(c) for y in range(r) if self.getmap((x,y))=="初"][0]
        
        pass
    def getmap(self, pos):
        return self.map_data[pos[0]][pos[1]]
    
    def disp(self, screen, pages, addpages:dict, pos)->list:
        #初始化

        # 设置单元大小和字体
        unit_size = 32
        font = pygame.font.SysFont('simHei', unit_size)
        
        # 确定行数和列数
        c = len(self.map_data)
        r = len(self.map_data[0])

        # 计算地图绘制区域的大小
        map_area_width = r * unit_size
        map_area_height = c * unit_size

        # 计算地图绘制区域的左上角坐标
        map_area_x = (screen.get_width() - map_area_width) // 2
        map_area_y = (screen.get_height() - map_area_height) // 2
        
        player_pos = self.player_pos  # 初始化人物位置

        #循环体
        running = True
        isMoved = False

        while running:
            # 位置处理
            if isMoved and self.getmap(player_pos) == "村":
                pages.append(addpages[self][0])
                return [player_pos]
            
            # 事件处理
            if isMoved and random.randint(1, 16) == 1:
                # 遇敌
                pages.append(addpages[self][1])
                return [player_pos]
            isMoved = False
            
            # 接受操作
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exit()
                elif event.type == pygame.KEYDOWN:
                    dirkeys = [pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT]
                    movposs = [[-1,0],[1,0],[0,-1],[0,1]]
                    for i in range(len(dirkeys)):
                        if event.key != dirkeys[i]:
                            continue
                        newPos = [x+y for x,y in zip(player_pos,movposs[i])]
                        # print(newPos)
                        if not 0 <= newPos[0] < c or not 0<=newPos[1] <r:
                            print("出界")
                            break
                        if self.getmap(newPos) == "无":
                            print("无")
                            break
                        player_pos = newPos
                        self.player_pos = player_pos
                        isMoved = True

            # 清屏
            screen.fill((0, 0, 0))
            # 绘制土黄区域作为地图背景
            pygame.draw.rect(screen, (205, 133, 63), (map_area_x, map_area_y, map_area_width, map_area_height))

            # 绘制
            # 在黑色区域中绘制地图内容
            for i in range(c):
                for j in range(r):
                    char = self.map_data[i][j]
                    if char == "村":
                        text_surface = font.render(char, True, (255, 255, 255))
                        text_rect = text_surface.get_rect()
                        text_rect.topleft = (map_area_x + j * unit_size, map_area_y + i * unit_size)
                        screen.blit(text_surface, text_rect)
                    elif char == "无":
                        pygame.draw.rect(screen, (0, 0, 0), (map_area_x + j * unit_size, map_area_y + i * unit_size, unit_size, unit_size))

            # 绘制人物位置
            player_char = "♀"
            text_surface = font.render(player_char, True, (255, 0, 0))  # 红色表示人物
            text_rect = text_surface.get_rect()
            text_rect.topleft = (map_area_x + player_pos[1] * unit_size, map_area_y + player_pos[0] * unit_size)
            screen.blit(text_surface, text_rect)

            pygame.display.flip()