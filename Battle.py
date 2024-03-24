import pygame
from TextSys import dispText, WHITE, RED, GREEN
from Enemy import enemies
from Character import player

class BattleSrc:
    def __init__(self, addpages:dict) -> None:
        pass
    
    def disp(self, screen:pygame.Surface, pages:list, addpages:dict, wmpos)->list:
        #初始化
        options = ["攻击","技能","物品","逃跑"]
        selected_option = 0
        actors = [player, enemies[0]]
        actor = player
        enemies[0].HP = enemies[0].MHP

        #循环体
        running = True
        Texting = True
        isReturn = False
        text = f"野生的{enemies[0].name}出现了"
        gif_image = pygame.image.load(r'resource\image\Slime\Slime_Front11.png')
        original_width, original_height = gif_image.get_size()
        gif_image = pygame.transform.scale(gif_image, (original_width * 8, original_height * 8))

        # 控制闪烁效果的透明度
        alpha = 255
        alpha_direction = -2  # 透明度改变的方向和速度
        
        while running:
            #接受操作
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # running = False
                    pass
                elif event.type == pygame.KEYDOWN:
                    if Texting:
                        if event.key == pygame.K_SPACE:
                            Texting = False
                            if isReturn:
                                pages.pop()
                                return [wmpos]
                            
                            if actor == enemies:
                                # 敌方行动
                                damage = [enemies[0].attack if not player.armor else enemies[0].attack-player.armor.attack][0]
                                text = f"{enemies[0].name}对你造成了{damage}点伤害"
                                Texting = True
                                player.HP-=damage
                                actor = player
                    else:
                        if actor == player:
                            if event.key == pygame.K_UP:
                                selected_option -= 1
                            elif event.key == pygame.K_DOWN:
                                selected_option += 1
                            elif event.key == pygame.K_SPACE:
                                if selected_option == 0:
                                    damage = [2 if not player.weapon else player.weapon.attack-enemies[0].defense][0]
                                    text = f"你对{enemies[0].name}造成了{damage}点伤害"
                                    Texting = True
                                    enemies[0].HP-=damage
                                    actor = enemies
                                

            selected_option %= len(options)

            # 清屏
            screen.fill((0, 0, 0))
            # 绘制文本
            dispText(screen, text, bottomleft=(128, 128*3), color=[(255, 255, 255) if Texting else (128, 128, 128)][0])

            # 绘制己方状态
            # 计算血量百分比
            health_percentage = player.getHPpct()

            # 绘制血量条
            HPbarpos = (128*6,128*3)
            health_bar_width = 200
            health_bar_height = 20
            health_bar_fill_width = int((health_percentage / 100) * health_bar_width)
            health_bar_rect = pygame.Rect(HPbarpos[0], HPbarpos[1], health_bar_width, health_bar_height)
            health_bar_fill_rect = pygame.Rect(HPbarpos[0], HPbarpos[1], health_bar_fill_width, health_bar_height)

            pygame.draw.rect(screen, RED, health_bar_rect)
            pygame.draw.rect(screen, GREEN, health_bar_fill_rect)

            # 显示血量百分比
            # font = pygame.font.SysFont(None, 30)
            # # hptext = f"Health: {health_percentage}%"
            # text_surface = font.render(hptext, True, WHITE)
            # screen.blit(text_surface, (HPbarpos[0], HPbarpos[1]))

            # 绘制敌方状态
            # 计算血量百分比
            health_percentage = enemies[0].getHPpct()
            # 绘制敌方血量条
            HPbarpos = (16*26,16*17)
            health_bar_width = 200
            health_bar_height = 20
            health_bar_fill_width = int((health_percentage / 100) * health_bar_width)
            health_bar_rect = pygame.Rect(HPbarpos[0], HPbarpos[1], health_bar_width, health_bar_height)
            health_bar_fill_rect = pygame.Rect(HPbarpos[0], HPbarpos[1], health_bar_fill_width, health_bar_height)

            pygame.draw.rect(screen, RED, health_bar_rect)
            pygame.draw.rect(screen, GREEN, health_bar_fill_rect)
            
            # 绘制行动选项
            for i in range(len(options)):
                optext = options[i]
                if i == selected_option and not Texting:
                    color = (255, 255, 255)  # 白色
                else:
                    color = (128, 128, 128)  # 灰色
                dispText(screen, optext, bottomleft=(64, 64 + i * 64), color=color)

            
            
            # 绘制敌方
            alpha += alpha_direction
            if alpha <= 0 or alpha >= 255:
                alpha_direction *= -1

            gif_image.set_alpha(alpha)
            gif_rect = gif_image.get_rect()
            gif_rect.center = (screen.get_size()[0] // 2, screen.get_size()[1] // 2-gif_image.get_height()/2)
            screen.blit(gif_image, gif_rect)

            # 死亡事件
            if enemies[0].HP <= 0:
                text = f"{enemies[0].name}倒下了"
                Texting = True
                isReturn = True

            pygame.display.flip()