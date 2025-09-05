import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
print("player.py loaded!")
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) # call parent constructor
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        triangle_vertices = self.triangle()
        WHITE = (255, 255, 255)
        pygame.draw.polygon(
            surface=screen, 
            color=WHITE, 
            points=triangle_vertices, 
            width=2,
        )
        
