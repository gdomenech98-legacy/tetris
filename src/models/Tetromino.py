from ..utils.Shapes import SHAPES
class Tetromino:
    def __init__(self, type):
        self.type = type
        self.shape = SHAPES[type]  # A list of cell coordinates (x, y)
        self.rotation = 0  # Current rotation state (0, 1, 2, or 3)
        self.x = 0 # Current x-coordinate
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

    def getColorKey(self):
        for index, key in enumerate(SHAPES):
            if key == self.type:
                return (index + 1) # Colors start from index 1
        return 0 # Return default value that its index 0 -> black