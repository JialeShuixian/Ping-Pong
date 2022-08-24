from pygame import*
from random import randint

class GameSprite(sprite.Sprite): #class GameSprite ke thua Sprite co san trong pygame
    def __init__(self, player_image, player_x, player_y, play_speed):#nhan vat, toa do x, y, speed
        super().__init__()#chinh
        self.image = transform.scale(image.load(player_image), (xx, yy))#tao hinh anh nhan vat, kick co
        self.speed = play_speed
        self.rect = self.image.get_rect() #luu toa do vao bien rect
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed_x = play_speed
        self.speed_y = play_speed

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
        global run
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        
        if self.rect.y < 0 or self.rect.y > win_height - self.rect.height:
            self.speed_y *=-1 
            
        if self.rect.x < 0 or self.rect.x > win_width - self.rect.width:
        #     if self.rect.x == win_width:
        #         return 2
            self.speed_x *=-1 



        if self.rect.x <= 0:
            return 1

        if self.rect.x >= win_width - self.rect.width:
            return 2

        

#
    # def cnt(self):
    #     global player_score, com_score
    #     if self.rect.x < 0:
    #         com_score += 1
        
    #     if self.rect.x > win_width:
    #         player_score +=1


        # if self.rect == player.rect:
        #     player_score +=1 

        # if self.rect == com.rect:
        #     com_score += 1

    # def count(self):
    #     if self.rect.x <= 0: #and self.rect.y == player.rect.y:
    #         player_score +=1 
    #     if self.rect.x >= win_width: #and self.rect.y == com.rect.y:
    #         com_score += 1

    

#Size
win_width = 1000
win_height = 700

#Window
window = display.set_mode((win_width, win_height))#dat kick co
display.set_caption("Ping Pong")#ten game
background = transform.scale(image.load("C:/Users/Admin/Documents/Ping-Pong/pingpong/back.jpg"), (win_width, win_height))#set background



#Sprites
xx = 120
yy = 120
player = Player("paddle.png", 5, win_height - 300, 20)#tao nhan vat, x, y, toc do
com = Computer("paddle2.png", 850, win_height - 300, 20)


xx = 50
yy = 50

#ball1 = play.new_circle(color="light blue", x=-350, y=120, radius=25)
ball = Ball("ball.png", 500, win_height - 250, 10)
clock = time.Clock()

#Font
font.init()
font = font.Font("Roboto-Bold.ttf", 50) 
aw = font.render("Player A wins!", True, (0, 0, 204))
bw = font.render("Player B wins!", True, (0, 0, 204))

#Run

player_score = 0
score_txt = font.render(f"Score: {player_score}", True, (255, 255, 0))

com_score = 0
cscore_txt = font.render(f"Score: {com_score}", True, (255, 255, 0))
run = True
finish = False

rect = Rect(win_width/2, 0, 20, win_height)
while run:
    
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                finish = False
                player_score = 0
                com_score = 0
                ball.rect.x =  win_width/2
                ball.rect.y = win_height/2

        


    if not finish:
        window.blit(background, (0,0)) #set background
        window.fill((0,0,0))
        draw.rect(window, (128,128,128), rect)
        ball.draw()
        ball.update()

        player.draw()
        player.update()

        com.draw()
        com.update()

        score_txt = font.render(f"A Score: {player_score}", True, (255, 255, 0))
        window.blit(score_txt, (150, 5))

        cscore_txt = font.render(f"B Score: {com_score}", True, (0, 153, 0))
        window.blit(cscore_txt, (600, 5))

        
        if sprite.collide_rect(ball, player):
            ball.speed_x *=-1
        
            #print(player_score)
        
        if sprite.collide_rect(ball, com):
            ball.speed_x *=-1


        a = ball.update()
        if a == 1:
            com_score +=1
        elif a == 2:
            player_score +=1

#           WIN
        if player_score >= 11:
            window.blit(aw, (150, win_height/2))
            finish = True

        if com_score >= 11:
            window.blit(bw, (win_width/2, win_height/2))     
            finish = True
            

        
        clock.tick(60)

    display.update()