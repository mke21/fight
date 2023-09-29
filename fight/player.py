import pygame 

class Player1():
    
    def image(x,y):
        Player1 = pygame.image.load("assets/Player1F.png")
        Player1.rect = pygame.get_rect

    def move():
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            Player1.x + 10
        
        if keys[K_d]:
            Player1.x - 10
        
        if jump is False and keys[pygame.K_SPACE]:
            jump = True

        if jump is True:
            Player1.y -= vel * 4
            vel -= 1
            if vel < -10:
                jump = False
                vel = 10

        


