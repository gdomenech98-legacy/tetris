# Constants for the game board
import pygame
from ..utils.Shapes import getCellColor

# Board
CELL_SIZE = 30  # Size of each cell in pixels
# Screen
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
class Board:
    def __init__(self):
        self.board_width = int(SCREEN_WIDTH/CELL_SIZE)
        self.board_height = int(SCREEN_HEIGHT/CELL_SIZE)
        self.board = self.emptyBoard() # Initialize the game board grid

    def emptyBoard(self):
        return [[0] * self.board_width for _ in range(self.board_height)]
    
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
                        ci * CELL_SIZE,
                        ri * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE
                    )
                    pygame.draw.rect(screen, cell_color, cell_rect)

    
