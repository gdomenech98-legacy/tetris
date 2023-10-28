import pygame
from src.models.Board import Board

def initialize():
    # Initialize Pygame
    pygame.init()

def main():
    initialize()
    # Set up the screen (create a window)
    board = Board()
    screen = board.getScreen()
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((0, 0, 0))
        # draw board
        board.drawBoard(screen)
        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

main()