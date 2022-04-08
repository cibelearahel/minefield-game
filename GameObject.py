import pygame


class GameObject(pygame.sprite.Sprite):

    def __init__(self, sub):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/bomb.jpg')
        self.image = pygame.transform.scale(self.image, (sub, sub))
