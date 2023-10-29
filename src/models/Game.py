import random

from .Board import Board
from ..utils.Shapes import SHAPES
from .Tetromino import Tetromino

class Game:
    def __init__(self, board, screen):
        self.tetromino_shapes = SHAPES  # Dictionary of all Tetromino shapes
        self.current_tetromino = None # Current non placed piece at board
        self.board = board # Board model
        self.screen = screen # Screen obj


    def run(self):
        self.clearScreen()
        self.render()
        self.update()

    def update(self):
        # Update the game state in each frame, including:
        # 0- Check that have current Tetromino (if not spawn new one)
        if (not self.isCurrentTetromino()): # Checks that has current tetromino
            self.spawnTetromino()
        # 1- Moving the current Tetromino (down 1 position, user movements like rotate and down)
        # 2- Collision detection: Checks that current tetromino doesn't collide with board
        # 3- Update game board with piece
        if(self.isCollision()):  # Place piece if collide
            self.place_piece()
        else: # if no collide move down the next position
            self.getCurrentTetromino().move_down()
            

        # 4- Checking for completed rows (deletes completed rows and replace new positions)
        # 5- Game over condition (checks if have end game condition)

    def render(self):
        self.renderBoard()
        self.renderCurrentTetromino()
    
    def renderBoard(self):
        self.getBoard().drawBoard(self.getScreen())

    def renderCurrentTetromino(self):
        # Render the game board and the current Tetromino on the screen
        tmpBoard = Game(Board(), self.screen)
        tmpBoard.current_tetromino = self.getCurrentTetromino()
        tmpBoard.place_piece()
        tmpBoard.getBoard().drawBoard(self.getScreen())

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

    def isCollision(self): 
        collide = False
        tetromino = self.getCurrentTetromino()
        
        if(not tetromino):
            return collide
        
        for ri, row in enumerate(tetromino.shape):
            for ci, cell in enumerate(row):
                if(cell == 1): 
                    # Check if the cell is within the board boundaries
                    if (
                        tetromino.y + ri >= self.getBoard().getHeight()
                        or tetromino.x + ci < 0
                        or tetromino.x + ci >= self.getBoard().getWidth()
                        or self.getBoard().board[tetromino.y + ri][tetromino.x + ci] == 1
                    ):
                        collide = True
        return collide

    def place_piece(self):
        tetromino = self.getCurrentTetromino()
        if(not tetromino): return
        for ri, row in enumerate(tetromino.shape):
            for ci, cell in enumerate(row):
                if cell == 1:
                    # Check if the cell is within the board boundaries
                    if 0 <= tetromino.y + ri < self.getBoard().getHeight() and 0 <= tetromino.x + ci < self.getBoard().getWidth():
                        self.getBoard().board[tetromino.y + ri][tetromino.x + ci] = 3  # Fill the cell with the piece
