from shutil import move
from turtle import position
from numpy import square
import pygame
import os
import random

pygame.init()
pygame.font.init()

# Screen const

WIDTH = HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe!")
FPS = 60
CUT = WIDTH / 3 # Width and height of every of the 9 squares on the board.

# COLORS

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)  
BLACK = (0, 0, 0)

# LOAD IMAGES AND FONTS

X = pygame.transform.scale(pygame.image.load(os.path.join('images', 'X.png')), (CUT, CUT))
O = pygame.transform.scale(pygame.image.load(os.path.join('images', 'O.png')), (CUT, CUT))
WORD_FONT = pygame.font.SysFont('comicsnas', 80)

# USE FUNC

def draw(win, images):
    """Manages drawing in the screen."""

    # BACKGROUND
    win.fill(WHITE)

    # BOARD
    pygame.draw.rect(win, BLACK, pygame.Rect(CUT, 0, 5, HEIGHT))
    pygame.draw.rect(win, BLACK, pygame.Rect(CUT * 2, 0, 5, HEIGHT))
    pygame.draw.rect(win, BLACK, pygame.Rect(0, CUT, WIDTH, 5))
    pygame.draw.rect(win, BLACK, pygame.Rect(0, CUT * 2, WIDTH, 5))


    # DRAW PLAYS
    for i in range(len(images)):
        win.blit(images[i][0], images[i][1])

    
    pygame.display.update()

def need_to_cover(positions: list):
    """This function determinates if the computer needs to cover a possible win of the user and returns where the computer needs to move.
    Otherwhise, returns -1."""

    # CASE 0 1 2 WIN
    if positions[0] == 'o' and positions[1] == 'o' and type(positions[2]) == int:
        move_to = 2
    elif positions[1] == 'o' and positions[2] == 'o' and type(positions[0]) == int:
        move_to = 0
    elif positions[0] == 'o' and positions[2] == 'o' and type(positions[1]) == int:
        move_to = 1
    
    # CASE 0 3 6 WIN
    elif positions[0] == 'o' and positions[3] == 'o' and type(positions[6]) == int:
        move_to = 6
    elif positions[0] == 'o' and positions[6] == 'o' and type(positions[3]) == int:
        move_to = 3
    elif positions[3] == 'o' and positions[6] == 'o' and type(positions[0]) == int:
        move_to = 0
    
    # CASE 1 4 7 WIN
    elif positions[1] == 'o' and positions[4] == 'o' and type(positions[7]) == int:
        move_to = 7
    elif positions[4] == 'o' and positions[7] == 'o' and type(positions[1]) == int:
        move_to = 1
    elif positions[1] == 'o' and positions[7] == 'o' and type(positions[4]) == int:
        move_to = 4
    
    # CASE 2 5 8 WIN
    elif positions[2] == 'o' and positions[5] == 'o' and type(positions[8]) == int:
        move_to = 8
    elif positions[2] == 'o' and positions[8] == 'o' and type(positions[5]) == int:
        move_to = 5
    elif positions[5] == 'o' and positions[8] == 'o' and type(positions[2]) == int:
        move_to = 2
    
    # CASE 0 4 8 WIN
    elif positions[0] == 'o' and positions[4] == 'o' and type(positions[8]) == int:
        move_to = 8
    elif positions[4] == 'o' and positions[8] == 'o' and type(positions[0]) == int:
        move_to = 0
    elif positions[0] == 'o' and positions[8] == 'o' and type(positions[4]) == int:
        move_to = 4
    
    # CASE 2 4 6 WIN
    elif positions[2] == 'o' and positions[4] == 'o' and type(positions[6]) == int:
        move_to = 6
    elif positions[4] == 'o' and positions[6] == 'o' and type(positions[2]) == int:
        move_to = 2
    elif positions[2] == 'o' and positions[6] == 'o' and type(positions[4]) == int:
        move_to = 4
    
    # CASE 3 4 5 WIN
    elif positions[3] == 'o' and positions[4] == 'o' and type(positions[5]) == int:
        move_to = 5
    elif positions[4] == 'o' and positions[5] == 'o' and type(positions[3]) == int:
        move_to = 3
    elif positions[3] == 'o' and positions[5] == 'o' and type(positions[4]) == int:
        move_to = 4
    
    # CASE 6 7 8 WIN
    elif positions[6] == 'o' and positions[7] == 'o' and type(positions[8]) == int:
        move_to = 8
    elif positions[6] == 'o' and positions[8] == 'o' and type(positions[7]) == int:
        move_to = 7
    elif positions[7] == 'o' and positions[8] == 'o' and type(positions[6]) == int:
        move_to = 6

    # CASE 0 1 2 COVER
    elif positions[0] == 'x' and positions[1] == 'x' and type(positions[2]) == int:
        move_to = 2
    elif positions[1] == 'x' and positions[2] == 'x' and type(positions[0]) == int:
        move_to = 0
    elif positions[0] == 'x' and positions[2] == 'x' and type(positions[1]) == int:
        move_to = 1
    
    # CASE 0 3 6 COVER
    elif positions[0] == 'x' and positions[3] == 'x' and type(positions[6]) == int:
        move_to = 6
    elif positions[0] == 'x' and positions[6] == 'x' and type(positions[3]) == int:
        move_to = 3
    elif positions[3] == 'x' and positions[6] == 'x' and type(positions[0]) == int:
        move_to = 0
    
    # CASE 1 4 7 COVER
    elif positions[1] == 'x' and positions[4] == 'x' and type(positions[7]) == int:
        move_to = 7
    elif positions[4] == 'x' and positions[7] == 'x' and type(positions[1]) == int:
        move_to = 1
    elif positions[1] == 'x' and positions[7] == 'x' and type(positions[4]) == int:
        move_to = 4
    
    # CASE 2 5 8 COVER
    elif positions[2] == 'x' and positions[5] == 'x' and type(positions[8]) == int:
        move_to = 8
    elif positions[2] == 'x' and positions[8] == 'x' and type(positions[5]) == int:
        move_to = 5
    elif positions[5] == 'x' and positions[8] == 'x' and type(positions[2]) == int:
        move_to = 2
    
    # CASE 0 4 8 COVER
    elif positions[0] == 'x' and positions[4] == 'x' and type(positions[8]) == int:
        move_to = 8
    elif positions[4] == 'x' and positions[8] == 'x' and type(positions[0]) == int:
        move_to = 0
    elif positions[0] == 'x' and positions[8] == 'x' and type(positions[4]) == int:
        move_to = 4
    
    # CASE 2 4 6 COVER
    elif positions[2] == 'x' and positions[4] == 'x' and type(positions[6]) == int:
        move_to = 6
    elif positions[4] == 'x' and positions[6] == 'x' and type(positions[2]) == int:
        move_to = 2
    elif positions[2] == 'x' and positions[6] == 'x' and type(positions[4]) == int:
        move_to = 4
    
    # CASE 3 4 5 COVER
    elif positions[3] == 'x' and positions[4] == 'x' and type(positions[5]) == int:
        move_to = 5
    elif positions[4] == 'x' and positions[5] == 'x' and type(positions[3]) == int:
        move_to = 3
    elif positions[3] == 'x' and positions[5] == 'x' and type(positions[4]) == int:
        move_to = 4
    
    # CASE 6 7 8 COVER
    elif positions[6] == 'x' and positions[7] == 'x' and type(positions[8]) == int:
        move_to = 8
    elif positions[6] == 'x' and positions[8] == 'x' and type(positions[7]) == int:
        move_to = 7
    elif positions[7] == 'x' and positions[8] == 'x' and type(positions[6]) == int:
        move_to = 6
    
    # CASE NINGUNO
    else:
        move_to = -1
    
    return move_to


def player_move(click, squares, positions, images):
    """If a player makes a legal move, this function appends the correct image to the images list and adds 1 to the player."""

    legal = False

    for i in range(len(squares)):
        if pygame.Rect.colliderect(click, squares[i]):
            if type(positions[i]) == int:
                positions[i] = 'x'
                images.append((X, (squares[i].x, squares[i].y)))
                legal = True

    return legal

def computer_move(squares, positions, images):
    pygame.time.wait(500)

    move_to = need_to_cover(positions)
    if move_to == -1:
        moves = [positions.index(i) for i in positions if type(i) == int]
        if len(moves) > 0:
            move = random.choice(moves)
            positions[move] = 'o'
            images.append((O, (squares[move].x, squares[move].y)))
    else:
        positions[move_to] = 'o'
        images.append((O, (squares[move_to].x, squares[move_to].y)))
    


def checkstatus(positions: list):
    """This function returns 1 if there is a winner, 0 if it is a draw and -1 if game isn't over yet."""

    if positions[0] == positions[1] == positions[2]:
        result = 1
    elif positions[3] == positions[4] == positions[5]:
        result = 1
    elif positions[6] == positions[7] == positions[8]:
        result = 1
    elif positions[0] == positions[3] == positions[6]:
        result = 1
    elif positions[1] == positions[4] == positions[7]:
        result = 1
    elif positions[2] == positions[5] == positions[8]:
        result = 1
    elif positions[0] == positions[4] == positions[8]:
        result = 1
    elif positions[2] == positions[4] == positions[6]:
        result = 1
    elif positions[0] != 1 and positions[1] != 2 and positions[2] != 3 and positions[3] != 4 and positions[4] != 5 and positions[5] != 6 and positions[6] != 7 and positions[7] != 8 and positions[8] != 9:
        result = 0
    else:
        result = -1
    
    return result

def end_game(status: int, player_moved: bool, win):
    """Checks the status of the game and display the result if the game is over.
    Return 1 if game is over and 0 otherwise."""
    result = 0
    if status != -1: # Game done.
        if status == 1: # Have a winner
            if player_moved:
                msg = WORD_FONT.render(f"Computer wins!", 1, BLACK)
            else:
                msg = WORD_FONT.render(f"X Player wins!", 1, BLACK)
        elif status == 0: # Draw
            msg = WORD_FONT.render(f"Draw!", 1, BLACK)
        
        # End message display.
        win.fill(WHITE)
        win.blit(msg, (WIDTH / 2 - msg.get_width() / 2, HEIGHT / 2 - msg.get_height() / 2))
        pygame.display.update()
        pygame.time.wait(2000)

        result = 1

    return result

# MAIN FUNC

def main():
    """Main function."""

    run = True
    clock = pygame.time.Clock()
    player = [0] # Store player turn
    images = [] # Store images
    player_moved = False
    status = -1


    # SQUARES
    squares = [pygame.Rect(0, 0, CUT, CUT), pygame.Rect(CUT, 0, CUT, CUT), pygame.Rect(CUT * 2, 0, CUT, CUT), pygame.Rect(0, CUT, CUT, CUT), pygame.Rect(CUT, CUT, CUT, CUT), 
                pygame.Rect(CUT * 2, CUT, CUT, CUT), pygame.Rect(0, CUT * 2, CUT, CUT), pygame.Rect(CUT, CUT * 2, CUT, CUT), pygame.Rect(CUT * 2, CUT * 2, CUT, CUT)]
    # BOARD
    positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            if not player_moved:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    click = pygame.Rect(x, y, 1, 1)
                    if player_move(click, squares, positions, images):
                        status = checkstatus(positions)
                        if end_game(status, player_moved, WIN):
                            run = False
                        else:
                            player_moved = True
            else:
                computer_move(squares, positions, images)
                status = checkstatus(positions)
                if end_game(status, player_moved, WIN):
                    run = False
                else:
                    player_moved = False
        

        draw(WIN, images)

if __name__ == "__main__":
    main()

