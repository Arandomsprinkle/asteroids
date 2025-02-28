import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, position):
        # Pass position.x, position.y to the CircleShape constructor
        super().__init__(position.x, position.y, SHOT_RADIUS)
        # No need to initialize velocity again as CircleShape already does it
        # But we can set it to a specific value if needed
        self.velocity = pygame.Vector2(0, 0)  # Optional, as the parent already initializes it

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius)

    def update(self, dt):
        # Update position based on velocity
        self.position += self.velocity * dt