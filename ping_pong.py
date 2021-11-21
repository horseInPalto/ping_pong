from pygame import *
import random

width, height = size = (900, 500)

window = display.set_mode(size)
display.set_caption("Пинг-понг")
background = transform.scale (image.load("background.jpg"), size)
FPS = 60
clock = time.Clock()

font.init()
font2 = font.SysFont('Arial', 80)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (70, 70))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.center = (player_x, player_y)
    def recet(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, flip_x, *args):
        GameSprite.__init__(self, *args)
        self.image = transform.scale((transform.flip(self.image, flip_x, False)), [int(self.image.get_width()*2), int(self.image.get_height()*2)])
        rect = self.rect.copy()
        self.rect = self.image.get_rect()
        self.rect.center = rect.center

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

class Pelmen(GameSprite):
    def __init__(self, angle, player_image, player_x, player_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, player_speed)
        self.angle = angle
        self.pos = math.Vector2((player_x, player_y))
        self.start_pos = math.Vector2((player_x, player_y))
        self.vec = math.Vector2((random.choice([-1, 1]), random.uniform(-1, 1))).normalize() 
    def update(self):
        self.pos += self.vec * self.speed
        self.rect.center = self.pos
        if self.rect.top <= 0:
            self.rect.top = 0
            self.pos = self.rect.center
            self.vec = self.vec.reflect([0, -1])
        if self.rect.bottom >= height:
            self.rect.bottom = height
            self.pos = self.rect.center
            self.vec = self.vec.reflect([0, 1])
           
hero_l = Player(False, 'lozhka.png', width-100, height//2, 20)
hero_r = Player(True, 'lozhka.png', 100, height//2, 20)
pelmen = Pelmen(0, 'pelmen.png', width//2, height//2, 5)

game = True
score = [0, 0]

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    hero_l.update_l()
    hero_r.update_r()
    pelmen.update()

    if hero_l.rect.colliderect(pelmen.rect):
        pelmen.vec = pelmen.vec.reflect([1, 0])
    if hero_r.rect.colliderect(pelmen.rect):
        pelmen.vec = pelmen.vec.reflect([-1, 0])
    if pelmen.rect.left <= 0:
        score[1] += 1
        pelmen.pos = (width//2, height//2)
    if pelmen.rect.right >= width:
        score[0] += 1
        pelmen.pos = (width//2, height//2)

    window.blit(background, (0, 0))
    hero_l.recet()
    hero_r.recet()
    pelmen.recet()
    window.blit(font2.render(f"{score[0]}|{score[1]}", 1, Color('white')), (width//2, 50))

    clock.tick(FPS)
    display.update()
