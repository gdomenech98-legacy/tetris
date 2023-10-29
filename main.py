import pygame
from src.models.Board import Board
from src.models.Game import Game


FPS = 1 # Set the desired frame rate (e.g., 1 frame per second)
clock = pygame.time.Clock() # Create a Clock object to control the frame rate

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
            game.spawnTetromino()
        
        print('CURRENT BOARD', game.getBoard().board)
        currentPiece = game.getCurrentTetromino()
        # Checks that current tetromino doesn't collide with board
        print("SHAPEEEE", currentPiece.shape)
        hasCollision = False
        for row_index, row in enumerate(currentPiece.shape):
            for col_index, cell in enumerate(row):
                if(cell == 1):
                    # Collision type 1: 
                    if(cell and game.getBoard().board[row_index + currentPiece.x][col_index + currentPiece.y]): # checks that cell is fullfilled 1
                        print("Collision")
                    #     game.clearCurrentTetromino()

                    # Collision type 2: inferior border of board
                    elif(cell and (currentPiece.x == game.getBoard().getWidth() or currentPiece.y == game.getBoard().getHeight())):
                        print("Collision")
                    #     game.clearCurrentTetromino()
                    else:
                        print(f"x,y::: {row_index} : {col_index}")
                        game.getBoard().board[currentPiece.x + row_index ][currentPiece.y+ col_index] = 3 # Replace index for the color of the piexe
                        currentPiece.move_down()

        pygame.display.flip() # Update the display
        clock.tick(FPS) # Control the frame rate
    # Quit Pygame
    pygame.quit()


main()
