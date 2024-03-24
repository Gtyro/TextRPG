import pygame
from Item.Weapon import swords
from TextSys import dispText

class WeaponShopScr:
    #初始化
    def __init__(self, addpages:dict):
        pass

    def disp(self, screen, pages, addpages:dict, args):
        #初始化
        options = swords
        selected_option = 0
        
        #循环体
        running = True

        while running:
            #接受操作
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("quit from weapon shop")
                    return []
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_option -= 1
                    elif event.key == pygame.K_DOWN:
                        selected_option += 1
                    elif event.key == pygame.K_SPACE:
                        pass
                    elif event.key == pygame.K_x:
                        pages.pop()
                        return []

            selected_option %= len(options)

            # 清屏
            screen.fill((0, 0, 0))

            # 绘制武器选项
            for i in range(len(options)):
                if i == selected_option:
                    text = options[i].name + " <-"
                    color = (255, 255, 255)  # 白色
                else:
                    text = options[i].name
                    color = (128, 128, 128)  # 灰色

                dispText(screen, text, bottomleft=(16, 64 + i * 64), color=color)
            # 绘制说明
            dispText(screen, options[selected_option].info(), bottomleft=(128, 64),color=(128, 128, 128))

            #显示
            pygame.display.flip()