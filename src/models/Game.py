import random
import utils.Shapes
import Tetromino

class Game:
    def __init__(self):
        self.tetromino_shapes = utils.Shapes.SHAPES  # List of all Tetromino shapes
        self.current_tetromino = None

    def getPiece(self):
        # Return a random Tetromino shape
        return random.choice(self.tetromino_shapes)

    def spawnTetromino(self):
        # Generate a new Tetromino and set it as the current one
        shape = self.getPiece()
        self.current_tetromino = Tetromino(shape)
        return self.current_tetromino