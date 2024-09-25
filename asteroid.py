from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from random import uniform
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return

        angle = uniform(20.0, 50.0)
        vel1, vel2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y, new_rad)
        ast1.velocity = vel1 * 1.2
        
        ast2 = Asteroid(self.position.x, self.position.y, new_rad)
        ast2.velocity = vel2 * 1.2

