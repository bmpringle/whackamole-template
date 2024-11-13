import pygame
import random

def main():
    # Run game code.
    try:
        # Initialize pygame.
        pygame.init()

        # Load the mole image, create the screen with a resolution of 640 x 512, and create a pygame clock to keep the game running at 60 fps.
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        # Initialize the mole_location variable. This will store the mole's current location.
        mole_location = (0, 0)

        # Initialize the running boolean variable. This will be used to determine if the program should halt.
        running = True

        # This will loop until pygame recieves a quit event.
        while running:
            # Handle pygame events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Set the running variable to false if pygame recieves a QUIT event.
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    # Check if the user clicked on the square that the mole is in if pygame recieves a MOUSEBUTTONDOWN event. 
                    # If the user did click on the mole's square, use random.randrange to generate a new location for the mole 
                    # that's inside the boundaries of the screen. The mole_location variable uses a 20 x 16 grid to split the screen into different
                    # locations, so the new location should be (0-19, 0-15) inclusive.
                    if mole_location == (event.pos[0] // 32, event.pos[1] // 32):
                        mole_location = (random.randrange(20), random.randrange(16))

            # Fill the screen with a light green background
            screen.fill("light green")

            # Draw all the vertical lines for the 20 x 16 grid.
            for x in range(20):
                pygame.draw.line(screen, "black", (x * 32, 0), (x * 32, 512))

            # Draw all the horizontal lines for the 20 x 16 grid.
            for x in range(16):
                pygame.draw.line(screen, "black", (0, x * 32), (640, x * 32))

            # Copy the mole image onto the screen in correct location specified by mole_location. Converts from the grid
            # location to the pixel location by multiplying the x and y values by 32 since each grid is 32 x 32 pixels.
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_location[0] * 32, mole_location[1] * 32)))

            # Displays the newly drawn frame.
            pygame.display.flip()

            # Frame limit the application to 60 fps.
            clock.tick(60)
    finally: # If the application throws an exception, quit pygame before exiting.
        pygame.quit()


if __name__ == "__main__":
    main()
