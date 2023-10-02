import pygame

# TODO: errors fixen


class Player:

    def __init__(self, x: int, y: int, image_name: str = "Player1F"):
        self.x = x
        self.y = y
        self._image = pygame.image.load(f"assets/{image_name}.png")
        self.rect = pygame.get_rect

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x += 10

        if keys[pygame.K_d]:
            self.x -= 10

        # waar komt jump vandaam?
        if jump is False and keys[pygame.K_SPACE]:
            jump = True

        # wat is vel en jump?
        if jump is True:
            self.y -= vel * 4
            vel -= 1
            if vel < -10:
                jump = False
                vel = 10
