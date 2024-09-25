import pygame
from player import Player
from asteroid import Asteroid
from shot import Shot
from constants import *
from asteroidfield import AsteroidField

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
plr: Player
dt = 0.0

def init_objects():
    global plr

    AsteroidField.containers = updatable
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    ast_field = AsteroidField()
    plr = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 

def process_game():
    global screen, clock, dt, plr

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        for obj in updatable: obj.update(dt)
        for obj in drawable: obj.draw(screen)
        pygame.display.flip()

        for ast in asteroids:
            if ast.collides(plr):
                print("Game Over!")
                return
            for blt in shots:
                if ast.collides(blt):
                    ast.split()
                    blt.kill()

        dt = clock.tick(60)/1000
        

def main():
    pygame.init()
    print("Starting asteroids!")  
    init_objects()
    process_game()


if __name__ == "__main__":
    main()
