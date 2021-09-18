from pygame import *

#создай окно игры
window = display.set_mode((700,500))
display.set_caption("Ping-Pong")
#задай фон сцены
background = transform.scale(image.load("background.png"),(700,500))
window.blit(background,(0,0))
#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load("sprite1.png"),(100,100))

sprite2 = transform.scale(image.load("sprite2.png"),(100,100))
x1 = -10
y1 = 10
x2 = 610
y2 = 10
#обработай событие «клик по кнопке "Закрыть окно"»


game = True 
while game :
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))
    keys_pressed = key.get_pressed()
    clock = time.Clock()
    FPS = 60
    clock.tick(FPS)
    speed = 5
    if keys_pressed[K_UP] and x1 > 5 :
        y1 -=speed
    if keys_pressed[K_DOWN] and x1 < 395 :
        y1 +=speed
   
    if keys_pressed[K_w] and x1 > 5 :
        y2 -=speed
    if keys_pressed[K_s ] and x1 < 395 :
        y2 +=speed

    for e in event.get():
        if e.type == QUIT:
            game = False
    for e in event.get():
        if e.type == QUIT:
            game = False
            

    display.update()