import utils.Shapes as shapes

class Tetromino:
    def __init__(self, shape):
        self.shape = shape  # A list of cell coordinates (x, y)
        self.rotation = 0  # Current rotation state (0, 1, 2, or 3)
        self.x = 0  # Current x-coordinate
        self.y = 0  # Current y-coordinate

    def rotate(self):
        # Implement rotation logic based on the current rotation state
        pass

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1