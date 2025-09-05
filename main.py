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
    Player.containers = (updateable, drawable)
    player = Player(
        x=SCREEN_WIDTH / 2, 
        y=SCREEN_HEIGHT / 2,
    )


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        BLACK = (0, 0, 0)
        screen.fill(BLACK)
        # player.update(dt)
        # player.draw(screen=screen)
        updateable.update(dt)
        for item in drawable:
            item.draw(screen=screen)

        pygame.display.flip()
        conversion_factor_milliseconds_to_seconds = 1 / 1000
        time_since_last_tick_seconds = clock.tick(60) * conversion_factor_milliseconds_to_seconds
        dt += time_since_last_tick_seconds
        

if __name__ == "__main__":
    main()
