import play
import pygame #tao ra am thanh, tieu de cho cua so game
 
 
coin_sound = pygame.mixer.Sound("coin.wav")
sea_sound = pygame.mixer.Sound("sea.ogg")
pygame.display.set_caption("Platformer: the hardest game ever!")
 
platforms = []
coins = []
 
ball = play.new_circle(color="light blue", x=-350, y=120, radius=25)
 
play.set_backdrop("salmon")
 
score = play.new_text(words="0", x=play.screen.right-30, y=play.screen.top-50)
score_txt = play.new_text(words="Score: ", x=play.screen.right-100, y=play.screen.top-50)
 
 
 
sea=play.new_box(color="light blue", x=0, y=play.screen.bottom+30, width=play.screen.width, height=80 )
 
txt = play.new_text(words="Tap SPACE to jump, LEFT/RIGHT to move", x=0, y=-260, color="black")
 
def platforms_v():
    box1 = play.new_box(color="orange", x=-350, y=100, border_color="black", border_width=5, width=100, height=50)
 
 
    platforms.append(box1)
    box2 = play.new_box(color="orange", x=-150, y=150, border_color="black", border_width=5, width=200, height=50)
 
 
    platforms.append(box2)
    box3 = play.new_box(color="orange", x=60, y=50, border_color="black", border_width=5, width=150, height=50)
 
 
    platforms.append(box3)
    box4 = play.new_box(color="orange", x=280, y=140, border_color="black", border_width=5, width=200, height=50)
 
 
    platforms.append(box4)
    box5 = play.new_box(color="orange", x=-50, y=-50, border_color="black", border_width=5, width=60, height=50)
 
 
    platforms.append(box5)
    box6 = play.new_box(color="orange", x=-50, y=-50, border_color="black", border_width=5, width=60, height=50)
 
 
    platforms.append(box6)
 
    box7 = play.new_box(color="orange", x=-150, y=-150, border_color="black", border_width=5, width=80, height=50)
 
 
    platforms.append(box7)
 
    box8 = play.new_box(color="orange", x=-310, y=-100, border_color="black", border_width=5, width=150, height=50)
 
 
    platforms.append(box8)
 
    for i in platforms:
        i.start_physics(can_move=False, stable=True, obeys_gravity=True, mass=10)
 
 
 
 
def coins_v():
    coin = play.new_circle(color="yellow", x=-150, y=200, radius=15)
    coins.append(coin)
 
    #coin2 = play.new_circle(color="yellow", x=60, y=100, radius=15)
    #coins.append(coin2)
 
    coin = play.new_circle(color="yellow", x=280, y=220, radius=15)
    coins.append(coin)
 
    coin = play.new_circle(color="yellow", x=-50, y=0, radius=15)
    coins.append(coin)
 
    #coin5 = play.new_circle(color="yellow", x=-150, y=-111, radius=15)
    #coins.append(coin5)
 
    coin = play.new_circle(color="yellow", x=-310, y=-60, radius=15)
    coins.append(coin)
 
 
@play.when_program_starts
def start():
    pygame.mixer_music.load("soundtrack.mp3")
    pygame.mixer_music.play()
 
    ball.start_physics(can_move=True, stable=False, obeys_gravity=True, mass=50, friction=1.0, bounciness=0.5)
 
 
    platforms_v()
    coins_v()
 
 
 
@play.repeat_forever
async def do():
    # ball.start_physics(can_move=True, bounciness=0.1
    
 
 
    if play.key_is_pressed("right"):
        ball.physics.x_speed = 10
    elif play.key_is_pressed("left"):
        ball.physics.x_speed = -10
 
    elif play.key_is_pressed("space"):
        ball.physics.y_speed = 50
        await play.timer(seconds=1)
        ball.physics.y_speed=0
    
    else:
        ball.physics.x_speed=0
    
    await play.timer(seconds=1/48)
 
    for coin in coins:
    
        if coin.is_touching(ball):
            score.words= int(score.words) + 5
            score.show()
            coin.hide()
            coins.remove(coin)
    #pass
 
play.start_program()
 
#khi nhay xuong bac nao thi mat cai do
#thiet ke đạn (doi lai)
#khien cho man hinh game to hon
#screen_width, height
#coin
#bua sau demo
 
 

