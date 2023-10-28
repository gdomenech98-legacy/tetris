import pygame
from src.models.Board import Board
from src.utils.Shapes import L_SHAPE
from src.models.Tetromino import Tetromino
from src.models.Game import Game


def initialize():
    # Initialize Pygame
    pygame.init()
    # Set up the screen (create a window)
    board = Board()
    screen = board.getScreen()
    game = Game(board, screen)
    game.clearScreen()
    return game

def main():
    game = initialize()
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # draw board
        game.getBoard().drawBoard(game.getScreen())
        # Draw the Tetromino on the game board
        if (not game.isCurrentTetromino()): # Checks that has current tetromino
            print("Has no tetromino spawning new one")
            game.spawnTetromino()
        
        currentPiece = game.getCurrentTetromino()
        for row_index, row in enumerate(currentPiece.shape):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    # Draw a cell of the Tetromino at the appropriate position on the board
                    cell_x = currentPiece.x + col_index
                    cell_y = currentPiece.y + row_index
                    pygame.draw.rect(game.screen, (255, 255, 0),
                                     (cell_x * 30, cell_y * 30, 30, 30))
        # Update the display
        pygame.display.flip()
    # Quit Pygame
    pygame.quit()


main()
