import pygame
import os

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

def clicked(click, squares, positions, player, images):
    """If a player makes a legal move, this function appends the correct image to the images list and adds 1 to the player."""
    for i in range(len(squares)):
        if pygame.Rect.colliderect(click, squares[i]):
            if player[0] % 2 == 0 and type(positions[i]) == int:
                positions[i] = 'x'
                images.append((X, (squares[i].x, squares[i].y)))
                player[0] += 1
            elif player[0] % 2 == 1 and type(positions[i]) == int:
                positions[i] = 'o'
                images.append((O, (squares[i].x, squares[i].y)))
                player[0] += 1

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

def end_game(status: int, player: list, win):
    """Checks the status of the game and display the result if the game is over.
    Return 1 if game is over and 0 otherwise."""
    result = 0
    if status != -1: # Game done.
        if status == 1: # Have a winner
            if player[0] % 2 == 0:
                msg = WORD_FONT.render(f"O Player wins!", 1, BLACK)
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
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                click = pygame.Rect(x, y, 1, 1)
                clicked(click , squares, positions, player, images)
                status = checkstatus(positions)

                if end_game(status, player, WIN):
                    run = False
    

        draw(WIN, images)

if __name__ == "__main__":
    main()

