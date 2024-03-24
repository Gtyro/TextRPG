import pygame

# 定义颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def replace_middle_spaces(space_count, replacement):
    # 计算需要替换的空格数量
    spaces_count = space_count - len(replacement)

    # 如果replacement长度大于空格数量，截取replacement的中间部分
    if len(replacement) > space_count:
        start_idx = (len(replacement) - space_count) // 2
        end_idx = start_idx + space_count
        replacement = replacement[start_idx:end_idx]

    # 计算左右两侧需要的空格数量
    left_spaces = spaces_count // 2
    right_spaces = spaces_count - left_spaces

    # 构建替换后的文本
    replaced_text = " " * left_spaces + replacement + " " * right_spaces

    return replaced_text

def dispText(screen, text, center = '', bottomleft = '', color = (255, 255, 255)):
    font = pygame.font.SysFont('simHei', 30)
    text_surface = font.render(text, True, color)  # 白色文本
    if center:
        text_rect = text_surface.get_rect(center=center)
    elif bottomleft:
        text_rect = text_surface.get_rect(bottomleft=bottomleft)
    screen.blit(text_surface, text_rect)