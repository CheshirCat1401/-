# #Создай собственный Шутер!

# from pygame import *
# import random
# from random import randint

# window = display.set_mode((700,500))
# display.set_caption('shooter')
# background = transform.scale(image.load('sea.jpg'), (700, 500))

# FPS = 60
# clock = time.Clock()
# mixer.init()
# mixer.music.load('BeachParty.mp3')
# mixer.music.play()


# class GameSprite(sprite.Sprite):
#     def __init__(self, player_image, player_x, player_y, player_speed):
#         super().__init__()
#         self.image = transform.scale(image.load(player_image), (130,130))
#         self.speed = player_speed
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y
#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))

# class Player(GameSprite):
#     def __init__(self, player_image, player_x, player_y, player_speed):
#         super().__init__(player_image, player_x, player_y, player_speed)
      
#     def update(self):
#         keys_pressed = key.get_pressed()
#         if keys_pressed[K_a] and self.rect.x > 1:
#             self.rect.x -= 10
#         if keys_pressed[K_d] and self.rect.x < 595:
#             self.rect.x += 10
#     def fire(self):
#         bullet = Bullet('pearl.png', self.rect.centerx, self.rect.top, -5)
#         bullets.add(bullet)

# lost = 0 
# count = 0

# class Enemy(GameSprite):
#     def __init__(self, player_image, player_x, player_y, player_speed):
#         super().__init__(player_image,player_x, player_y, player_speed)
#         self.image = transform.scale(image.load(player_image), (100, 100))
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > 500:
#             self.rect.x = randint(80, 620)
#             self.rect.y = 0
#             lost = lost + 1

# class Bullet(GameSprite):
#     def __init__(self, player_image, player_x, player_y, player_speed):
#         super().__init__(player_image,player_x, player_y, player_speed)
#         self.image = transform.scale(image.load(player_image), (20, 20))
#     def update(self):
#         self.rect.y += self.speed
#         if self.rect.y <= 0:
#             self.kill()

# font.init()
# font = font.SysFont('Arial', 40)
# text_count = font.render('Счет:', 1, (255, 255, 255))
# text_lose = font.render('Пропущено:' + str(lost), 1, (255, 255, 255))
# winner = font.render('YOU WIN!', True, (252, 210, 0))
# lose = font.render('YOU LOSE!', True, (194, 0, 0))

# bullets = sprite.Group()

# monsters = sprite.Group()
# monster1 = Enemy('shark.png',randint(80,620),0,randint(0,3))
# monster2 = Enemy('shark.png',randint(80,620),0,randint(0,3))
# monster3 = Enemy('shark.png',randint(80,620),0,randint(0,3))
# monster4 = Enemy('shark.png',randint(80,620),0,randint(0,3))
# monster5 = Enemy('shark.png',randint(80,620),0,randint(0,3))
# monsters.add(monster1)
# monsters.add(monster2)
# monsters.add(monster3)
# monsters.add(monster4)
# monsters.add(monster5)
        
# sharks = Player('fish.png', 250, 350, 10)

# run = True
# finish = False
# while run:
#     for e in event.get():
#         if e.type == QUIT:
#             run = False
#         if e.type == KEYDOWN:
#             if e.key == K_SPACE:
#                 sharks.fire()

#     sprites_list = sprite.groupcollide(monsters, bullets, True, True)
#     for c in sprites_list:
#         count += 1
#         monster6 = Enemy('shark.png',randint(80,620),0,randint(1,2))
#         monsters.add(monster6)
    
#     if finish != True:
#         window.blit(background,(0, 0))                   
#         bullets.draw(window)   
#         sharks.reset()
#         sharks.update()
#         monsters.update()
#         bullets.update()

#     monsters.draw(window)
#     text_lose = font.render('Пропущено:' + str(lost), 1, (255, 255, 255))
#     text_count = font.render('Счет: ' + str(count), 1, (255, 255, 255))

#     window.blit(text_lose,(15, 37))
#     window.blit(text_count,(15, 5))

#     if lost >= 3 or sprite.spritecollide(sharks, monsters, False):
#         finish = True
#         window.blit(lose, (270, 220))
#     elif count >= 10:
#         finish = True
#         window.blit(winner, (270, 220)) 
            

#     clock.tick(60)
#     display.update()


