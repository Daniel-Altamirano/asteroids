import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MAX_RADIUS,
    PLAYER_RADIUS,
)
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    player = Player(
        x=SCREEN_WIDTH / 2, 
        y=SCREEN_HEIGHT / 2,
    )
    asteroid_field = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        BLACK = (0, 0, 0)
        screen.fill(BLACK)
        updateable.update(dt)
        for item in drawable:
            item.draw(screen=screen)

        pygame.display.flip()
        MS_TO_SECONDS = 1 / 1000
        time_since_last_tick_seconds = clock.tick(60) * MS_TO_SECONDS
        dt = time_since_last_tick_seconds
        

if __name__ == "__main__":
    main()
