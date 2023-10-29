import pygame
from src.models.Board import Board
from src.models.Game import Game


FPS = 3 # Set the desired frame rate (e.g., 1 frame per second)
clock = pygame.time.Clock() # Create a Clock object to control the frame rate

def main():
    # Initialize Pygame
    pygame.init()
    game = Game.initialize()
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        game.run()
        pygame.display.flip() # Update the display
        clock.tick(FPS) # Control the frame rate
    # Quit Pygame
    pygame.quit()


main()
