import random
from ..utils.Shapes import SHAPES
from .Tetromino import Tetromino

class Game:
    def __init__(self, board, screen):
        self.tetromino_shapes = SHAPES  # List of all Tetromino shapes
        self.current_tetromino = None # Current non placed piece at board
        self.board = board # Board 
        self.screen = screen # Screen

    def getCurrentTetromino(self):
        return self.current_tetromino
    
    def clearCurrentTetromino(self):
        self.current_tetromino = None

    def isCurrentTetromino(self):
        return self.current_tetromino
    
    def getBoard(self):
        return self.board
    
    def getScreen(self):
        return self.screen
    
    def clearScreen(self):
       # Clear the screen
       self.screen.fill((255, 255, 255))

    def getPiece(self):
        # Return a random Tetromino shape
        return random.choice(self.tetromino_shapes)

    def spawnTetromino(self):
        # Generate a new Tetromino and set it as the current one
        shape = self.getPiece()
        self.current_tetromino = Tetromino(shape)
        return self.current_tetromino