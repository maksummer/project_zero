from typing import Any
import pygame


WIDTH = 1000
HEIGH = 600
SIZE = (WIDTH, HEIGH)
FPS = 60

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
background = pygame.transform.scale( pygame.image.load("фон.jpg"), SIZE)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, size, coords ):
        self.image = pygame.transform.scale( pygame.image.load(filename), size)
        self.rect = self.image.get_rect()
        self.rect.center = coords

    def reset(self):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def update_l(self):
        if self.rect.bottom < 500:
            self.rect.y += 5

        key = pygame.key.get_pressed()
        if key [pygame.K_a]:
            self.rect.x -= 10
        elif key[pygame.K_d]:
            self.rect.x += 10
        


skorpion = Player("скорпион без фону.png", (290,290), (800,470))
subzero =  Player("subzero2.png", (250,250), (200,470))





game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    window.blit(background, (0,0))
    skorpion.reset()
    subzero.reset()
    subzero.update_l()
    pygame.display.update()
    
    clock.tick(FPS)