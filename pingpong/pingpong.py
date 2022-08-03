from pygame import*

class GameSprite(sprite.Sprite): #class GameSprite ke thua Sprite co san trong pygame
    def __init__(self, player_image, player_x, player_y, play_speed):#nhan vat, toa do x, y, speed
        super().__init__()#chinh
        self.image = transform.scale(image.load(player_image), (xx, yy))#tao hinh anh nhan vat, kick co
        self.speed = play_speed
        self.rect = self.image.get_rect() #luu toa do vao bien rect
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))#ve nhan vat len man hinh
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
 
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    


class Computer(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed            

class Ball(GameSprite): #inheritance gamesprite
    def update(self):
        self.rect.y -= self.speed
        
        if self.rect.y < 0:
            self.kill() #delete sprite in pygame

win_width = 1000
win_height = 700

window = display.set_mode((win_width, win_height))#dat kick co
display.set_caption("Ping Pong")#ten game
background = transform.scale(image.load("C:/Users/Admin/Documents/Ping-Pong/pingpong/back.jpg"), (win_width, win_height))#set background


xx = 120
yy = 120
player = Player("paddle.png", 5, win_height - 300, 20)#tao nhan vat, x, y, toc do
com = Computer("paddle2.png", 850, win_height - 300, 20)
xx = 50
yy = 50
ball = Ball("ball.png", 500, win_height - 300, 50)

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if run:
        window.blit(background, (0,0)) #set background
        player.draw()
        player.update()

        com.draw()
        com.update()

        ball.draw()



    display.update()