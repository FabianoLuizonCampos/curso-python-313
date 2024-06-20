import pygame

class Shoot(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/shot.png")
        self.image = pygame.transform.scale(self.image, [50,50])
        self.rect = self.image.get_rect()

        self.speed = 4

        
        
    def update(self, *args):

        self.rect.x += self.speed
       
        if self.rect.right > 840:
            self.kill()