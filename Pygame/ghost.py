import pygame

class Ghost(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/ghost-x4.gif")
        self.image = pygame.transform.scale(self.image, [100,100])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.speed = 0
        self.acceleration = 0.1

        # self.speedX = 0
        # self.accelerationX = 0.1

    def update(self, *args):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.speed -= self.acceleration
        elif keys[pygame.K_s]:
            self.speed += self.acceleration
        # if keys[pygame.K_a]:
        #     self.speedX -= self.accelerationX
        # elif keys[pygame.K_d]:
        #     self.speedX += self.accelerationX
        else:
            self.speed *= 0.95
            # self.speedX *= 0.95

        self.rect.y += self.speed
        # self.rect.x += self.speedX

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speed = 0

        # Não façam - Somente EIXO X
        # if self.rect.left < 0:
        #     self.rect.left = 0
        #     self.speedX = 0
        # elif self.rect.right > 840:
        #     self.rect.right = 840
        #     self.speedX = 0