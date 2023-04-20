import pygame
import pygame_menu
from constants import WIDTH, HEIGHT, SQUARE_SIZE, LIGHTSLATEBLUE, WHITE, GREEN, RED, BLACK
from game import Game
from minimax import minimax

pygame.init()

FPS = 60
AI = WHITE

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def set_player(value, player):
    global AI
    if player == 0:
        AI = WHITE
    else:
        AI = LIGHTSLATEBLUE


def game_loop():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == AI:
            value, new_board = minimax(game.get_board(), 4, WHITE, game, AI)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            game_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.reset()
        game.update()
    

def game_menu():
    menu = pygame_menu.Menu("Simple Checkers", WIDTH, HEIGHT)
    menu = pygame_menu.Menu('Welcome', WIDTH, HEIGHT,
                        theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input('Name :', default='Alice')
    menu.add.selector('Play as :', [('Blue', 0), ('White', 1)], onchange=set_player)
    menu.add.button('Play', game_loop)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(WIN)





def main():
    game_menu()
    pygame.quit()



if __name__ == "__main__":
    main()