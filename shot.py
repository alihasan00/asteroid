import pygame
from constants import SHOT_RADIUS
from circle_shape import CircleShape  # Ensure CircleShape is in a separate file

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), self.position, self.radius)
