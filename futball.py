import pygame, time,random
from pygame import display, draw, event, key
pygame.init()
c=pygame.time.Clock()
vorota_left = (0, 0, 20, 680)
vorota_right = (1180, 0, 20, 680)

timer=event.custom_type()
dvigenie = pygame.Rect([500, 320, 100, 100])
screen = display.set_mode([1200, 680])
player_right = pygame.Rect(1000, dvigenie.centery, 3, 150)
player_left=pygame.Rect(200,300,3,150)

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
        if r.type==timer:
            speedx=random.randint(-5,5)
            speedy=random.randint(-5,5)
            if speedx==0:
                speedx = random.randint(-5, 5)
            if speedy==0:
                speedy = random.randint(-5, 5)
    keys = key.get_pressed()
    # if keys[pygame.K_UP]:
    #     player_right.y += -5
    # if keys[pygame.K_DOWN]:
    #     player_right.y +=5
    if keys[pygame.K_w]:
        player_left.y-=5
    if keys[pygame.K_s]:
        player_left.y+=5
    # движение

    dvigenie.x += speedx
    v=player_left.colliderect(dvigenie)
    t = player_right.colliderect(dvigenie)
    if t == 1:
        if speedx < 0:
            speedx = random.randint(5,10)
            dvigenie.left = player_right.right

        elif speedx > 0:
            speedx = random.randint(-10,-5)
            dvigenie.right = player_right.left
    if v==1:
        if speedx<0:
            speedx=random.randint(5,10)
            dvigenie.left=player_left.right
        elif speedx>0:
            speedx=random.randint(-10,-5)
            dvigenie.right=player_left.left
    if 1180 < dvigenie.right:
        dvigenie.centerx = 600
        dvigenie.centery=340
        pygame.time.set_timer(timer,1500,True)
        speedx = 0
        speedy=0
    if 19 > dvigenie.x:
        dvigenie.centerx = 600
        dvigenie.centery=340
        pygame.time.set_timer(timer,1500,True)
        speedx = 0
        speedy=0

    dvigenie.y += speedy
    if 0 > dvigenie.y:
        speedy = 3
        dvigenie.top = 0

    if 680 < dvigenie.bottom:
        speedy = -10
        dvigenie.bottom = 680
    player_right.y=dvigenie.y
    # рисование
    screen.fill([20, 30, 255])
    draw.rect(screen, [30, 200, 255], vorota_left)
    draw.rect(screen, [30, 200, 255], vorota_right)
    # draw.rect(screen, [255, 100, 155], dvigenie)
    draw.circle(screen, [100, 255, 155], [dvigenie.centerx, dvigenie.centery], 50)
    draw.rect(screen, [0, 0, 0], player_right)
    draw.rect(screen, [255, 255, 255], player_left)

    display.flip()
