import pygame

pygame.font.init()

size = (600, 600)

BLUE = (0, 0, 139)
WHITE = (220, 220, 220)
RED = (255, 0, 0)
ORANGE = (247, 131, 7)
PINK = (255, 0, 255)
GREEN = (50, 205, 50)
YELLOW = (253, 208, 23)
BLACK = (0, 0, 0)

qtd_square = 8
space_square = 2
margin = space_square // 2
side_square = round((size[0] - (space_square * qtd_square + margin)) / qtd_square)
parameter = [margin, margin, side_square, side_square]

font = pygame.font.SysFont('Time New Roman', side_square)
font_lost = pygame.font.SysFont('Tahoma', size[0] // 10)
font_win = pygame.font.SysFont('Tahoma', size[0] // 8)
font_flag = pygame.font.SysFont('Times New Roman', size[0] // 20)

qtd_mines = int(qtd_square * qtd_square * 0.15)
with_flag = {}
open_square = []

field = [None] * qtd_square
