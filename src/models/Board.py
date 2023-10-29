# Constants for the game board
import pygame
from ..utils.Shapes import getCellColor

# Board
BOARD_WIDTH = 10  # Number of columns
BOARD_HEIGHT = 20  # Number of rows
CELL_SIZE = 30  # Size of each cell in pixels
BOARD_POS_X = 30  # X-coordinate of the top-left corner of the board
BOARD_POS_Y = 30  # Y-coordinate of the top-left corner of the board
# Screen
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
class Board:
    def __init__(self):
        self.board_width = BOARD_WIDTH
        self.board_height = BOARD_HEIGHT
        self.board = self.emptyBoard() # Initialize the game board grid

    def emptyBoard(self):
        return [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
    
    def getWidth(self):
        return self.board_width
    
    def getHeight(self):
        return self.board_height

    def getScreen(self, height = SCREEN_HEIGHT, width = SCREEN_WIDTH):
        screen = pygame.display.set_mode((width, height)) # Set up the screen (create a window)
        return screen

    def setBoard(self, board): 
        self.board = board

    def drawBoard(self, screen):
        # Draw the game board
        for ri, row in enumerate(self.board):
            for ci, cell in enumerate(row):
                if(cell):
                    cell_color = getCellColor(cell)
                    cell_rect = pygame.Rect(
                        BOARD_POS_X + ci * CELL_SIZE,
                        BOARD_POS_Y + ri * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE
                    )
                    pygame.draw.rect(screen, cell_color, cell_rect)

    
