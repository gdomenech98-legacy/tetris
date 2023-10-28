# Constants for the game board
import pygame
from src.utils.Cells import getCellColor

BOARD_WIDTH = 10  # Number of columns
BOARD_HEIGHT = 20  # Number of rows
CELL_SIZE = 30  # Size of each cell in pixels
BOARD_POS_X = 50  # X-coordinate of the top-left corner of the board
BOARD_POS_Y = 50  # Y-coordinate of the top-left corner of the board


class Board:
    def __init__(self):
        # Initialize the game board grid
        self.board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

    def getScreen(self):
        # Set up the screen (create a window)
        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        return screen

    def drawBoard(self):
        screen = self.getScreen()
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

    
