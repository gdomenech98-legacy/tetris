def getCellColor(value):
    cell_colors = {
        0: (0, 0, 0),  # Black for empty cells
        1: (3, 65, 174),  # Blue for Tetromino piece 1
        2: (114, 203, 59),  # Green for Tetromino piece 2
        3: (255, 213, 0),  # Yellow for Tetromino piece 3
        4: (255, 151, 28),  # Orange for Tetromino piece 4
        5: (255, 50, 19),  # Red for Tetromino piece 5

        # Add more colors for other Tetrominoes
    }
    return cell_colors.get(value, (255, 255, 255))