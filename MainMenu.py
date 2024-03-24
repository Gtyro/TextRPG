'''
主菜单类
'''
import pygame

from WorldMap import WorldMap_page

class main_menu_scr:
    def __init__(self, addpages:dict) -> None:
        addpages[self] = [WorldMap_page(addpages)]
        pass
    
    def disp(self, screen, pages, addpages:dict, *args):
        options = ["开始游戏", "结束游戏"]
        selected_option = 0


        running = True
        game_started = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_option -= 1
                    elif event.key == pygame.K_DOWN:
                        selected_option += 1
                    elif event.key == pygame.K_SPACE:
                        if selected_option == 0 and not game_started:
                            # print("游戏开始了")
                            game_started = True
                            pages.append(addpages[self][0])
                            return
                        elif selected_option == 1:
                            running = False

            selected_option %= len(options)

            # 清屏
            screen.fill((0, 0, 0))

            # 显示主菜单
            for i in range(len(options)):
                if i == selected_option:
                    text = "-> " + options[i] + " <-"
                    color = (255, 255, 255)  # 白色
                else:
                    text = options[i]
                    color = (128, 128, 128)  # 灰色

                font = pygame.font.SysFont('simHei', 32)  # 使用系统中可用的 "simHei" 字体
                text_surface = font.render(text, True, color)
                text_rect = text_surface.get_rect(center=(screen.get_size()[0]/2, screen.get_size()[1]/2 + i * 50))
                screen.blit(text_surface, text_rect)

            pygame.display.flip()