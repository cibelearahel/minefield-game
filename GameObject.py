import pygame


class GameObject(pygame.sprite.Sprite):

    def __init__(self, sub):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load('image/bomb.jpg')
        self.image1 = pygame.transform.scale(self.image1, (sub, sub))
        self.image2 = pygame.image.load('image/flag.jpg')
        self.image2 = pygame.transform.scale(self.image2, (sub, sub))
