# ping_pong
from pygame import *

width, height = size = (900, 500)

window = display.set_mode(size)
display.set_caption("Пинг-понг")
background = transform.scale (image.load("background.png"), size)
FPS = 60
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(70,70))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.center = (player_x, player_y)
    def recet(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.bottom < height:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.bottom < height:
            self.rect.y += self.speed

hero_l = Player('polovnik.png', 100, height//2, 20)
hero_r = Player('polovnik.png', width-100, height//2, 20)

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    hero_l.update_l()
    hero_r.update_r()

    window.blit(background, (0, 0))
    hero_l.recet()
    hero_r.recet()

    clock.tick(FPS)
    display.update()
