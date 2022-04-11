import pygame

pygame.font.init()

size = (600, 600)

MINT = (193, 255, 196)
MINT_GREEN = (36, 183, 119)
WHITE = (220, 220, 220)
RED = (255, 0, 0)
ORANGE = (247, 131, 7)
PINK = (255, 0, 255)
GREEN = (50, 205, 50)
DARK_GREEN = (10, 114, 17)
YELLOW = (253, 208, 23)
BLACK = (0, 0, 0)


qtd_square = 8
space_square = 2
margin = space_square // 2
side_square = round((size[0] - (space_square * qtd_square + margin)) / qtd_square)
parameter = [margin, margin, side_square, side_square]


font = pygame.font.Font('fonts/Square.ttf', side_square)
font_standard = pygame.font.Font('fonts/Square.ttf', size[0] // 10)


qtd_mines = int(qtd_square * qtd_square * 0.15)
with_flag = {}
open_square = []

field = [None] * qtd_square
