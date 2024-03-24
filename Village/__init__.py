from typing import Callable

import pygame

from TextSys import dispText
from WeaponShop import WeaponShopScr

class village_page:
    def __init__(self, addpages:dict[Callable,list]) -> None:
        addpages[self] = [WeaponShopScr(addpages)]
        pass
    
    def disp(self, screen, pages:list, addpages:dict, wmpos):
        options = ["武器店", "防具店", "道具店", "旅馆", "离开村庄"]
        selected_option = 0
        # dispText(screen, "game start", center=(screen.get_width() // 2, screen.get_height() // 2))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_option -= 1
                    elif event.key == pygame.K_DOWN:
                        selected_option += 1
                    elif event.key == pygame.K_SPACE:
                        if selected_option == 0:
                            pages.append(addpages[self][0])
                            return [wmpos]
                        elif selected_option == 4:
                            pages.pop()
                            return [wmpos]
                            
                                

            selected_option %= len(options)

            # 清屏
            screen.fill((0, 0, 0))

            # 显示主菜单
            for i in range(len(options)):
                text = options[i]
                if i == selected_option:
                    color = (255, 255, 255)  # 白色
                else:
                    color = (128, 128, 128)  # 灰色
                dispText(screen, text, bottomleft=(0, 50 + i * 50), color=color)
            pygame.display.flip()