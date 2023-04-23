import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the window dimensions
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300

# Set the colors
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
RED = (255, 0, 0)

# Set the font
font = pygame.font.SysFont(None, 50)

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Create the Tic Tac Toe board
board = [[None, None, None], [None, None, None], [None, None, None]]

# Set the current player
current_player = "X"

# Set the game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            pos = pygame.mouse.get_pos()
            x = pos[0] // 100
            y = pos[1] // 100
            # Check if the cell is empty
            if board[y][x] is None:
                # Mark the cell with the current player
                board[y][x] = current_player
                # Switch to the other player
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"
    
    # Clear the window
    window.fill(WHITE)
    
    # Draw the Tic Tac Toe board
    for y in range(3):
        for x in range(3):
            pygame.draw.rect(window, BLACK, (x * 100, y * 100, 100, 100), 2)
            if board[y][x] is not None:
                text = font.render(board[y][x], True, BLACK)
                window.blit(text, (x * 100 + 30, y * 100 + 30))
    
    # Check for a win
    for y in range(3):
        if board[y][0] == board[y][1] == board[y][2] is not None:
            pygame.draw.line(window, RED, (0, y * 100 + 50), (300, y * 100 + 50), 4)
            game_over = True
        if board[0][y] == board[1][y] == board[2][y] is not None:
            pygame.draw.line(window, RED, (y * 100 + 50, 0), (y * 100 + 50, 300), 4)
            game_over = True
    if board[0][0] == board[1][1] == board[2][2] is not None:
        pygame.draw.line(window, RED, (50, 50), (250, 250), 4)
        game_over = True
    if board[0][2] == board[1][1] == board[2][0] is not None:
        pygame.draw.line(window, RED, (250, 50), (50, 250), 4)
        game_over = True
    
    # Update the window
    pygame.display.update()
