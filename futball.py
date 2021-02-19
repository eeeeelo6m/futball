import pygame, time
from pygame import display, draw, event, key
c=pygame.time.Clock()
vorota_left = (0, 0, 20, 680)
vorota_right = (1180, 0, 20, 680)

screen = display.set_mode([1200, 680])
player_right = pygame.Rect(1000, 300, 1, 300)
player_left=pygame.Rect(200,300,1,300)
dvigenie = pygame.Rect([500, 320, 100, 100])
speedx = -10
speedy = 5
while 1 == 1:
    c.tick(100)
    print(c.get_fps())

    # управление
    e = event.get()
    for r in e:
        if r.type == pygame.QUIT:
            exit()

    keys = key.get_pressed()
    if keys[pygame.K_w]:
        player_right.y += -10
    if keys[pygame.K_s]:
        player_right.y +=10
    # движение

    dvigenie.x += speedx
    v=player_left.colliderect(dvigenie)
    t = player_right.colliderect(dvigenie)
    if t == 1:
        if speedx < 0:
            speedx = 20
            dvigenie.left = player_right.right

        elif speedx > 0:
            speedx = -30
            dvigenie.right = player_right.left
    if v==1:
        if speedx<0:
            speedx=20
            dvigenie.left=player_left.right
        elif speedx>0:
            speedx=-20
            dvigenie.right=player_left.left
    if 1180 < dvigenie.right:
        dvigenie.right = 1180
        speedx = -10
    if 19 > dvigenie.x:
        dvigenie.x = 20
        speedx = 5

    dvigenie.y += speedy
    if 0 > dvigenie.y:
        speedy = 3
        dvigenie.top = 0

    if 680 < dvigenie.bottom:
        speedy = -10
        dvigenie.bottom = 680

    # рисование
    screen.fill([20, 30, 255])
    draw.rect(screen, [30, 200, 255], vorota_left)
    draw.rect(screen, [30, 200, 255], vorota_right)
    # draw.rect(screen, [255, 100, 155], dvigenie)
    draw.circle(screen, [100, 255, 155], [dvigenie.centerx, dvigenie.centery], 50)
    draw.rect(screen, [0, 0, 0], player_right)
    draw.rect(screen, [255, 255, 255], player_left)

    display.flip()
