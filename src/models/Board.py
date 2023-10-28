# Constants for the game board
import pygame
from src.utils.Cells import getCellColor
# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Board
BOARD_WIDTH = 10  # Number of columns
BOARD_HEIGHT = 20  # Number of rows
CELL_SIZE = 30  # Size of each cell in pixels
BOARD_POS_X = 50  # X-coordinate of the top-left corner of the board
BOARD_POS_Y = 50  # Y-coordinate of the top-left corner of the board

class Board:
    def __init__(self, height=BOARD_HEIGHT, width = BOARD_WIDTH):
        self.board = [[0] * width for _ in range(height)] # Initialize the game board grid

    def getScreen(self, height = SCREEN_HEIGHT, width = SCREEN_WIDTH):
        screen = pygame.display.set_mode((width, height)) # Set up the screen (create a window)
        return screen

    def drawBoard(self, screen):
        # Draw the game board
        for row in range(BOARD_HEIGHT):
            for col in range(BOARD_WIDTH):
                cell_value = self.board[row][col]
                cell_color = getCellColor(cell_value)  # Implement this function
                cell_rect = pygame.Rect(
                    BOARD_POS_X + col * CELL_SIZE,
                    BOARD_POS_Y + row * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
                pygame.draw.rect(screen, cell_color, cell_rect)

    
