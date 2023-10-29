# Define Tetromino shapes as lists of cell coordinates
I_SHAPE = [[1, 1, 1, 1]]
L_SHAPE = [[1, 0],
           [1, 0],
           [1, 1]]
O_SHAPE = [[1, 1],
           [1, 1]]
T_SHAPE = [[0, 1, 0],
           [1, 1, 1]]
J_SHAPE = [[0, 1],
           [0, 1],
           [1, 1]]
S_SHAPE = [[0, 1, 1],
           [1, 1, 0]]
Z_SHAPE = [[1, 1, 0],
           [0, 1, 1]]
# Define array of shapes
SHAPES = {
    "I_SHAPE": I_SHAPE,
    "J_SHAPE": J_SHAPE,
    "L_SHAPE": L_SHAPE,
    "O_SHAPE": O_SHAPE,
    "T_SHAPE": T_SHAPE,
    "S_SHAPE": S_SHAPE,
    "Z_SHAPE": T_SHAPE,
}

SHAPE_COLORS = {
    0: (0, 0, 0),  # Black for empty cells
    1: (231, 76, 60),  # Red 
    2: (142, 68, 173),  # Purple
    3: (52, 152, 219),  # Blue
    4: (22, 160, 133),  # Green1
    5: (46, 204, 113),  # Green2
    6: (241, 196, 15), # yellow
    7: (243, 156, 18 ) # Orange
}

def getCellColor(value):
    return SHAPE_COLORS.get(value, (255, 255, 255))