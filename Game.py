import pygame
import sys
import random
import os
import platform

pygame.init()

BLUE = (0, 0, 139)
WHITE = (220, 220, 220)
RED = (255, 0, 0)
ORANGE = (247, 131, 7)
PINK = (255, 0, 255)
GREEN = (50, 205, 50)
YELLOW = (253, 208, 23)
BLACK = (0, 0, 0)

size = (600, 600)
screen = pygame.display.set_mode(size)
screen.fill((50, 50, 50))
pygame.display.set_caption("Minesweeper")
pygame.display.flip()

bomb = pygame.image.load(os.path.join('image', 'bomb.jpg'))
flag = pygame.image.load(os.path.join('image', 'flag.jpg'))

qtd_square = 8
space_square = 2
margin = space_square // 2
side_square = round((size[0] - (space_square * qtd_square + margin)) / qtd_square)
parameter = [margin, margin, side_square, side_square]

for i in range(qtd_square):
    for j in range(qtd_square):
        pygame.draw.rect(screen, BLUE, parameter)
        parameter[0] += side_square + space_square
        pygame.display.flip()
    parameter[1] += side_square + space_square
    parameter[0] = margin

font = pygame.font.SysFont('Time New Roman', side_square)
font_lost = pygame.font.SysFont('Tahoma', size[0] // 10)
font_win = pygame.font.SysFont('Tahoma', size[0] // 8)
font_flag = pygame.font.SysFont('Times New Roman', size[0] // 20)

sub = side_square - space_square
bomb = pygame.transform.scale(bomb, (sub, sub))
flag = pygame.transform.scale(flag, (sub, sub))

qtd_mines = int(qtd_square * qtd_square * 0.15)
flags = qtd_mines
corrects = 0
with_flag = {}
open_square = []

field = [None] * qtd_square

for i in range(qtd_square):
    field[i] = [False] * qtd_square

for i in range(qtd_mines):
    rows = random.randrange(0, qtd_square)
    columns = random.randrange(0, qtd_square)

    while field[rows][columns]:
        rows = random.randrange(0, qtd_square)
        columns = random.randrange(0, qtd_square)

    field[rows][columns] = True


def controlMouse():
    mouse = pygame.mouse.get_pos()
    searchX = side_square + margin
    column = 0

    while searchX < mouse[0]:
        column += 1
        searchX += side_square + space_square

    searchY = side_square + margin
    Row = 0

    while searchY < mouse[1]:
        Row += 1
        searchY += side_square + space_square

    return Row, column


def UpdateQtdBombs(row_square, col_square, cord_x, cord_y, call):
    cont = 0
    for k in range(-1, 2):
        for n in range(-1, 2):
            if 0 <= row_square + k <= qtd_square - 1 and 0 <= col_square + n <= qtd_square - 1:
                if field[row_square + k][col_square + n]:
                    cont += 1

    createText(cont, cord_x, cord_y, side_square)
    open_square.append((row_square, col_square))

    if cont == 0:
        for p in range(-1, 2):
            for q in range(-1, 2):
                if 0 <= row_square + p <= qtd_square - 1 and 0 <= col_square + q <= qtd_square - 1:
                    if not ((row_square + p, col_square + q) in call) and not (field[row_square + p][col_square + q]):
                        call.append((row_square + p, col_square + q))
                        UpdateQtdBombs(row_square + p, col_square + q, cord_x + (q * (side_square + space_square)),
                                       cord_y + (p * (side_square + space_square)),
                                       call)


def createText(cont, coord_x, coord_y, sq):
    global color
    pygame.draw.rect(screen, WHITE, (coord_x, coord_y, sq, sq))
    if cont == 1:
        color = PINK
    elif cont == 2:
        color = YELLOW
    elif cont == 3:
        color = GREEN
    elif cont == 4:
        color = RED
    elif cont in range(5, 8):
        color = ORANGE
    elif cont == 8:
        color = BLACK
    if cont != 0:
        text = font.render(str(cont), True, color)
        position = (coord_x + (sq // 2) - (text.get_rect().width // 2), coord_y + (sq // 2) - (
                text.get_rect().height // 2))
        screen.blit(text, position)
    pygame.display.update()


def Lost():
    for r in range(qtd_square):
        for s in range(qtd_square):
            if field[r][s]:
                if not ((r, s) in with_flag) or not (with_flag[(r, s)]):
                    pygame.draw.rect(screen, WHITE, (
                        margin + (side_square * s) + (space_square * s),
                        margin + (side_square * r) + (space_square * r), side_square, side_square))
                    screen.blit(bomb, (margin + (side_square * s) + (space_square * s),
                                       margin + (side_square * r) + (space_square * r)))
                    pygame.display.update()

    text = font_lost.render("YOU LOST!", True, RED)
    screen.blit(text, (size[0] // 2 - (text.get_rect().width // 2), size[1 // 2] - (text.get_rect().height // 2)))
    end()


def Win():
    for t in range(qtd_square):
        for u in range(qtd_square):
            if not ((t, u) in open_square) and not (field[i][j]):
                UpdateQtdBombs(t, u, margin + (u * (side_square + space_square)),
                               margin + (t * (side_square + space_square)), [])

    text = font_win.render("YOU WON!", True, GREEN)
    screen.blit(text, (size[0] // 2 - (text.get_rect().width // 2), size[1] // 2 - (text.get_rect().height // 2)))
    end()


def finishedFlag():
    text = font_flag.render("Flags over!", True, RED)
    screen.blit(text, (size[0] // 2 - (text.get_rect().width // 2), size[1] // 2 - (text.get_rect().height // 2)))
    end()


def end():
    pygame.display.update()
    if platform.system() == "Windows":
        exit()
        pygame.quit()
    else:
        pygame.quit()
        exit()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            row, col = controlMouse()
            if not ((row, col) in with_flag) or with_flag[(row, col)] is False:
                if not (field[row][col]):
                    x = margin + (side_square * col) + (space_square * col)
                    y = margin + (side_square * row) + (space_square * row)
                    UpdateQtdBombs(row, col, x, y, [])
                else:
                    Lost()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            row, col = controlMouse()
            if not ((row, col) in open_square):
                if (row, col) in with_flag:
                    if with_flag[(row, col)]:
                        flags += 1
                        if field[row][col]:
                            corrects -= 1
                        pygame.draw.rect(screen, BLUE, (margin + (side_square * col) + (space_square * col),
                                                        margin + (side_square * row) + (space_square * row),
                                                        side_square, side_square))
                        pygame.display.update()
                        with_flag[(row, col)] = False
                    else:
                        with_flag[(row, col)] = True
                        screen.blit(flag, margin + (side_square * col) + (space_square * col),
                                    margin + (side_square * row) + (space_square * row))
                        pygame.display.update()

                        if field[row][col]:
                            corrects += 1
                        flags -= 1

                else:
                    with_flag[(row, col)] = True
                    screen.blit(flag, (margin + (side_square * col) + (space_square * col),
                                       margin + (side_square * row) + (space_square * row)))
                    pygame.display.update()

                    if field[row][col]:
                        corrects += 1
                    flags -= 1

                    if corrects == qtd_mines:
                        Win()
                    if flags == 0:
                        finishedFlag()
