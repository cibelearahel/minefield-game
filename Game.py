import random
from Config import *
from Bomb import Bomb
from Flag import Flag


class Game:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Minesweeper")

        sub = side_square - space_square
        bomb = Bomb(sub).image1
        flag = Flag(sub).image2

        def generate_square():
            for i in range(qtd_square):
                for j in range(qtd_square):
                    pygame.draw.rect(screen, BLUE, parameter)
                    parameter[0] += side_square + space_square
                    pygame.display.flip()
                parameter[1] += side_square + space_square
                parameter[0] = margin

        def define_fields():
            for i in range(qtd_square):
                field[i] = [False] * qtd_square

        def generate_mines():
            for i in range(qtd_mines):
                rows = random.randrange(0, qtd_square)
                columns = random.randrange(0, qtd_square)
                while field[rows][columns]:
                    rows = random.randrange(0, qtd_square)
                    columns = random.randrange(0, qtd_square)
                field[rows][columns] = True

        def control_mouse():
            mouse = pygame.mouse.get_pos()
            search_x = side_square + margin
            column = 0

            while search_x < mouse[0]:
                column += 1
                search_x += side_square + space_square
            search_y = side_square + margin
            row = 0
            while search_y < mouse[1]:
                row += 1
                search_y += side_square + space_square

            return row, column

        def update_qtd_bombs(row_square, col_square, cord_x, cord_y, call):
            cont = 0
            for k in range(-1, 2):
                for n in range(-1, 2):
                    if 0 <= row_square + k <= qtd_square - 1 and 0 <= col_square + n <= qtd_square - 1:
                        if field[row_square + k][col_square + n]:
                            cont += 1

            create_text(cont, cord_x, cord_y, side_square)
            open_square.append((row_square, col_square))

            if cont == 0:
                for p in range(-1, 2):
                    for q in range(-1, 2):
                        if 0 <= row_square + p <= qtd_square - 1 and 0 <= col_square + q <= qtd_square - 1:
                            if not ((row_square + p, col_square + q) in call) and not (
                                    field[row_square + p][col_square + q]):
                                call.append((row_square + p, col_square + q))
                                update_qtd_bombs(row_square + p, col_square + q,
                                                 cord_x + (q * (side_square + space_square)),
                                                 cord_y + (p * (side_square + space_square)),
                                                 call)

        def create_text(cont, coord_x, coord_y, sq):
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

        def lost():
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
            screen.blit(text,
                        (size[0] // 2 - (text.get_rect().width // 2), size[1 // 2] - text.get_rect().height * 5))
            end()

        def win():

            for t in range(qtd_square):
                for u in range(qtd_square):
                    if not ((t, u) in open_square) and not (field[i][j]):
                        update_qtd_bombs(t, u, margin + (u * (side_square + space_square)),
                                         margin + (t * (side_square + space_square)), [])

            text = font_win.render("YOU WON!", True, GREEN)
            screen.blit(text,
                        (size[0] // 2 - (text.get_rect().width // 2), size[1] // 2 - text.get_rect().height * 5))
            end()

        def finished_flag():
            text = font_flag.render("Flags over!", True, RED)
            screen.blit(text,
                        (size[0] // 2 - (text.get_rect().width // 2), size[1] // 2 - (text.get_rect().height // 2)))
            end()

        def end():
            pygame.display.update()
            pygame.time.wait(1000)
            exit()
            pygame.quit()

        def game_loop():
            flags = qtd_mines
            corrects = 0
            generate_square()
            define_fields()
            generate_mines()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        row, col = control_mouse()
                        if not ((row, col) in with_flag) or with_flag[(row, col)] is False:
                            if not (field[row][col]):
                                x = margin + (side_square * col) + (space_square * col)
                                y = margin + (side_square * row) + (space_square * row)
                                update_qtd_bombs(row, col, x, y, [])
                            else:
                                lost()

                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                        row, col = control_mouse()
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
                                    win()
                                if flags == 0:
                                    finished_flag()

        game_loop()
