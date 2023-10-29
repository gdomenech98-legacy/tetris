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
                        hasCollision = True
                        print("Collision detected with placed board pieces!")
                    # Collision type 2: inferior border of board
                    elif(cell and (currentPiece.x == game.getBoard().getWidth() or currentPiece.y == game.getBoard().getHeight())):
                        hasCollision = True
                        print("Collision detected with bottom wall")
                    else:
                        print("Previous board:: ",game.getBoard().board)
                        game.getBoard().board[row_index+currentPiece.x][col_index+currentPiece.y] = 3 # Replace index for the color of the piexe
                        print("Previous board 2222:: ",game.getBoard().board)

        if(not hasCollision): # if no collide move_down due to frame
            currentPiece.move_down()
        else: # Remove currentPiece
            game.clearCurrentTetromino()
        pygame.display.flip() # Update the display
        clock.tick(FPS) # Control the frame rate
    # Quit Pygame
    pygame.quit()


main()
