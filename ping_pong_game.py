import pygame, sys
from random import randint
import json

clock = pygame.time.Clock()
FPS = 60

pygame.init()

window = pygame.display.set_mode((1000, 600))
# , pygame.RESIZABLE

# background = pygame.transform.scale(pygame.image.load("image_shuter/galaxy.jpg"), (1000, 600))

pygame.display.set_caption("Пинг Понг")

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, sixe_x, size_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (sixe_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move_rocket_one(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.x > 50:
            self.rect.x -= self.speed

        if keys[pygame.K_s] and self.rect.x < 100:
            self.rect.x += self.speed

    def move_rocket_two(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.x > 900:
            self.rect.x -= self.speed

        if keys[pygame.K_DOWN] and self.rect.x < 100:
            self.rect.x += self.speed

# class Enemy(GameSprite):
#     def auto_move(self): 
#         self.rect.x += self.speedx
#         self.rect.y += self.speedy 



game = True

while game:

    window.fill((255, 255, 255))

    pygame.display.update()
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False



    clock.tick(FPS)