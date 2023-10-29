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
        self.running = True # False when Game over

    @staticmethod
    def initialize():
        # Set up the screen (create a window)
        board = Board()
        screen = board.getScreen()
        game = Game(board, screen)
        game.clearScreen()
        return game

    def isRunning(self):
        return self.running
    
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
            print('COLLISION!')
            self.place_piece()
            self.clearCurrentTetromino()
        else: # if no collide move down the next position
            print("Move down")
            self.getCurrentTetromino().move_down()
            
        # 4- Checking for completed rows (deletes completed rows and replace new positions)
        # 5- Game over condition (checks if have end game condition)
        self.isGameOver()
    
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
       self.screen.fill((0, 0, 0))

    def getPiece(self):
        # Return a random Tetromino shape
        return random.choice(list(self.tetromino_shapes.keys()))

    def spawnTetromino(self):
        # Generate a new Tetromino and set it as the current one
        shape = self.getPiece()
        self.current_tetromino = Tetromino(shape)
        return self.current_tetromino

    def isCollision(self): 
        tetromino = self.getCurrentTetromino()
        board = self.getBoard().board
        board_w = self.getBoard().getWidth()
        board_h = self.getBoard().getHeight()
        if(not tetromino):
            return False
        
        for ri, row in enumerate(tetromino.shape):
            for ci, cell in enumerate(row):
                if(cell == 1): 
                    # Check if the cell is within the board boundaries
                    board_x = tetromino.x + ci
                    board_y = tetromino.y + ri
                    if (
                        board_x < 0
                        or board_x >= board_w
                        or board_y >= board_h
                        or board_y >= 0
                        and board[board_y][board_x] > 0
                    ):
                        return True
        return False

    def isGameOver(self):
        # Check if the top row of the board contains any filled cells
        top_row = self.getBoard().board[0]
        if (any(cell > 0 for cell in top_row)):
            self.running = False
    
    def place_piece(self):
        tetromino = self.getCurrentTetromino()
        if(not tetromino): return
        for ri, row in enumerate(tetromino.shape):
            for ci, cell in enumerate(row):
                if cell == 1:
                    # Check if the cell is within the board boundaries
                    if 0 <= tetromino.y + ri < self.getBoard().getHeight() and 0 <= tetromino.x + ci < self.getBoard().getWidth():
                        self.getBoard().board[tetromino.y + ri][tetromino.x + ci] = Tetromino(tetromino.type).getColorKey()  # Fill the cell with the piece
