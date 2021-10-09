from pygame import *
from random import randint
from time import sleep

#создай окно игры
window = display.set_mode((700,500))
display.set_caption("Ping-Pong")
#задай фон сцены
background = transform.scale(image.load("black.jpg"),(700,500))
window.blit(background,(0,0))
#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load("wall.png"),(1,100))

sprite2 = transform.scale(image.load("wall.png"),(1,100))

sprite3 = transform.scale(image.load("white.jpg"),(10,10))
x1 = 12
y1 = 252
x2 = 692
y2 = 252
x3 = 320
y3 = 250
speedx = 0
speedy = 0
speedb = 4
rand1 = randint(1,2)
rand2 = randint(1,2)
if rand1 == 1:
    speedx -= speedb
else:
    speedx += speedb
if rand2 == 1:
    speedy -= speedb
else:
    speedy += speedb
#обработай событие «клик по кнопке "Закрыть окно"»


game = True 
while game :
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))
    window.blit(sprite3,(x3,y3))
    keys_pressed = key.get_pressed()
    clock = time.Clock()
    FPS = 60
    clock.tick(FPS)
    speed = 5
    x3 += speedx
    y3 += speedy

    if x3>750:
        x3 = 320
        y3 = 250
        speedx = 0
        speedy = 0
        rand1 = randint(1,2)
        rand2 = randint(1,2)
        if rand1 == 1:
            speedx -= speedb
        else:
            speedx += speedb
        if rand2 == 1:
            speedy -= speedb
        else:
            speedy += speedb
        sleep(1)
    if x3<-50:
        x3 = 320
        y3 = 250
        speedx = 0
        speedy = 0
        rand1 = randint(1,2)
        rand2 = randint(1,2)
        if rand1 == 1:
            speedx -= speedb
        else:
            speedx += speedb
        if rand2 == 1:
            speedy -= speedb
        else:
            speedy += speedb
        sleep(1)
    if y3 <0:
        speedy = speedy * -1
    if y3 >495:
        speedy = speedy * -1
    if x3-4==x1:
        if y3+5>=y1 and y3+5<=y1+100:
            speedx *= -1
            print("1")
    elif x3+4==x2:
        if y3+5>=y2 and y3+5<=y2+100:
            speedx *= -1
            print("2")
        print(x3,y3)
        

    if keys_pressed[K_UP] and y2 > 5 :
        y2 -=speed
    if keys_pressed[K_DOWN] and y2 < 395 :
        y2 +=speed
   
    if keys_pressed[K_w] and y1 > 5 :
        y1 -=speed
    if keys_pressed[K_s ] and y1 < 395 :
        y1 +=speed

    for e in event.get():
        if e.type == QUIT:
            game = False
            

    display.update()