import random
from ..utils.Shapes import SHAPES
from .Tetromino import Tetromino

class Game:
    def __init__(self, board, screen):
        self.tetromino_shapes = SHAPES  # Dictionary of all Tetromino shapes
        self.current_tetromino = None # Current non placed piece at board
        self.board = board # Board model
        self.screen = screen # Screen obj

    def update(self):
        # Update the game state in each frame, including:
        # - Moving the current Tetromino (down 1 position, user movements like rotate and down)
        # - Collision detection (detects when piece collides)
        # - Updating the game board (updates board with the piece)
        # - Checking for completed rows (deletes completed rows and replace new positions)
        # - Game over condition (checks if have end game condition)
        return

    def render(self):
        # Render the game board and the current Tetromino on the screen
        return
    
    def handle_input(self, event):
        # Handle user input, such as moving the current Tetromino left/right, rotating, etc.
        return
    
    def getCurrentTetromino(self):
        return self.current_tetromino
    
    def clearCurrentTetromino(self):
        self.current_tetromino = None

    def isCurrentTetromino(self):
        return self.current_tetromino
    
    def getBoard(self): # Returns a Board model
        return self.board
    
    def getScreen(self):
        return self.screen
    
    def clearScreen(self):
       # Clear the screen
       self.screen.fill((74, 74, 74))

    def getPiece(self):
        # Return a random Tetromino shape
        return random.choice(list(self.tetromino_shapes.keys()))

    def spawnTetromino(self):
        # Generate a new Tetromino and set it as the current one
        shape = self.getPiece()
        self.current_tetromino = Tetromino(shape)
        return self.current_tetromino