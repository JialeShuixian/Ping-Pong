import play
import pygame
from random import randint

play.set_backdrop('light green')
coin_sound = pygame.mixer.Sound('coin.wav')
sea_sound = pygame.mixer.Sound('sea.ogg')
pygame.display.set_caption('Platformer: the harderst game ever!')

score_txt = play.new_text(words='Score:', x=play.screen.right-100, y=play.screen.top-30, size=70)
score = play.new_text(words='0', x=play.screen.right-30, y=play.screen.top-30, size=70)
text = play.new_text(words='Tap SPACE to jump, LEFT/RIGHT to move', x=0, y=play.screen.bottom+60, size=70)
sprite = play.new_circle(color='white', x=play.screen.left+20, y=play.screen.top-20, border_color='grey', border_width=3, radius=15)
platforms = []
coins = []

sea = play.new_box(
        color='blue', width=play.screen.width, height=50, x=0, y=play.screen.bottom+20
    )

def draw_platforms():
    platform1 = play.new_box(
        color='brown', border_width=1, border_color='black', width=150, height=30, x=play.screen.left+70, y=play.screen.top-170
        )
    platforms.append(platform1)
    platform2 = play.new_box(
        color='brown', border_width=1, border_color='black', width=250, height=30, x=play.screen.left+330, y=play.screen.top-170
        )
    platforms.append(platform2)
    platform3 = play.new_box(
        color='brown', border_width=1, border_color='black', width=100, height=30, x=play.screen.left+550, y=play.screen.top-120
        )
    platforms.append(platform3)
    platform4 = play.new_box(
        color='brown', border_width=1, border_color='black', width=130, height=30, x=play.screen.left+670, y=play.screen.top-170
    )
    platforms.append(platform4)

    for platform in platforms:
        platform.start_physics(can_move=False, stable=True, obeys_gravity=False, mass=10)

def draw_coins():
    coin1 = play.new_circle(
        color='yellow', x=play.screen.left+330, y=play.screen.top-130, radius=10
    )
    coins.append(coin1)
    coin2 = play.new_circle(
        color='yellow', x=play.screen.left+700, y=play.screen.top-130, radius=10
    )
    coins.append(coin2)

@play.when_program_starts
def start():
    pygame.mixer_music.load('soundtrack.mp3')
    pygame.mixer_music.play()

    sprite.start_physics(can_move=True, stable=False, obeys_gravity=True, mass=50, friction=1.0, bounciness=0.5)
    
    draw_platforms()
    draw_coins()
    
@play.repeat_forever
async def game():
    for c in coins:
        if c.is_touching(sprite):
            coin_sound.play()
            sprite.physics.y_speed = -1 *sprite.physics.y_speed
            coins.remove(c)
            c.hide()
            score.words=str(int(score.words) + 1)

    if sprite.is_touching(sea):
        sea_sound.play()
        sprite.hide()
        await play.timer(seconds=2.0)
        quit()

    if play.key_is_pressed('right'):
        sprite.physics.x_speed = 10
    elif play.key_is_pressed('left'):
        sprite.physics.x_speed = -10
    elif play.key_is_pressed('space'):
        sprite.physics.y_speed = 50
        await play.timer(seconds=1)
        sprite.physics.y_speed = 0
    else:
        sprite.physics.x_speed=0

    await play.timer(seconds=1/48)

play.start_program()
