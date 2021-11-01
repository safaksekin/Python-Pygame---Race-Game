import pygame
import sys
import random
from pygame import mixer

pygame.init()
clock=pygame.time.Clock()

score=0
score_list=[]

window=pygame.display.set_mode((600,800))

menu_bg=pygame.image.load("materials_data/sadt.jpg")
menu_bg=pygame.transform.scale(menu_bg,(600,800))

'''background1=pygame.image.load("materials_data/bg1.jpg")
background1=pygame.transform.scale(background1,(600,800))'''
bg_y=0

mycar=pygame.image.load("materials_data/car7_red.png")
mycar=pygame.transform.scale(mycar,(50,75))
mycar_x_change=4
mycar_x=280
mycar_y=650
mycar_rectangle=(mycar_x+1,mycar_y,49,75)
mycar_rect=mycar.get_rect(center=(280,650))

car1=pygame.image.load("materials_data/car1_blue.png")
car2=pygame.image.load("materials_data/car4_purple.png")
car3=pygame.image.load("materials_data/car5_orange.png")
car4=pygame.image.load("materials_data/car1_yellow.png")
car5=pygame.image.load("materials_data/car4_green.png")
car6=pygame.image.load("materials_data/car7_purple.png")
car7=pygame.image.load("materials_data/car6_blue.png")
car8=pygame.image.load("materials_data/car7_yellow.png")

car1=pygame.transform.scale(car1,(50,75))
car2=pygame.transform.scale(car2,(50,75))
car3=pygame.transform.scale(car3,(50,75))
car4=pygame.transform.scale(car4,(50,75))
car5=pygame.transform.scale(car5,(50,75))
car6=pygame.transform.scale(car6,(50,75))
car7=pygame.transform.scale(car7,(50,75))
car8=pygame.transform.scale(car8,(50,75))

carlist=[car1,car2,car3,car4,car5,car6,car7,car8]
car_y_change=5

carlist1=[]
carlist2=[]
carlist3=[]
carlistleft=[]
carlistright=[]


cor1=[-75,-120,-180,-240]
cor2=[-80,-150,-200,-280]
cor3=[-170,-230]
corleft=[-120,-300]
corright=[-250,-420]


coordlist=[105,280,445]

coin_list=[]
coin_y_change=6

#------------------------------------
press_space=pygame.image.load("text_data/press_space.png")
press_space=pygame.transform.scale(press_space,(450,210))

press_space2=pygame.image.load("text_data/press_space.png")
press_space2=pygame.transform.scale(press_space2,(360,168))

logo=pygame.image.load("text_data/png real logo.png")
logo=pygame.transform.scale(logo,(200,200))

logo2=pygame.image.load("text_data/png real logo.png")
logo2=pygame.transform.scale(logo2,(120,120))

resume=pygame.image.load("text_data/resume.png")
resume=pygame.transform.scale(resume, (36,36))

pause=pygame.image.load("text_data/stop.png")
pause=pygame.transform.scale(pause, (55,55))

high_score_img=pygame.image.load("text_data/high-score-5f2d19bc08b81.png")
high_score_img=pygame.transform.scale(high_score_img,(210,90))

game_over=pygame.image.load("text_data/game_over.png")
game_over=pygame.transform.scale(game_over, (540,225))
game_over_rect=game_over.get_rect(center= (300,200))

score_img=pygame.image.load("text_data/unnamed.png").convert_alpha()
score_img=pygame.transform.scale(score_img, (105,50))

pause_img=pygame.image.load("text_data/pause_img.png").convert_alpha()
pause_img=pygame.transform.scale(pause_img,(220,100))

'''background1_glow=pygame.image.load("materials_data/background1_glow.jpg")
background1_glow=pygame.transform.scale(background1_glow,(600,800))'''

bg1dark=pygame.image.load("materials_data/bg1dark.png")
bg1dark=pygame.transform.scale(bg1dark,(100,100))

bg2dark=pygame.image.load("materials_data/bg2dark.jpg")
bg2dark=pygame.transform.scale(bg2dark,(100,100))

bg1=pygame.image.load("materials_data/asdfgh.png")
bg1=pygame.transform.scale(bg1,(100,100))

bg2=pygame.image.load("materials_data/xyzxxxzv.jpg")
bg2=pygame.transform.scale(bg2,(100,100))

bggr=pygame.image.load("download.png")
bggr=pygame.transform.scale(bggr,(600,800))

def rect():
    return pygame.Rect(mycar_x+1,mycar_y,49,75)

def floor_loop(bg_y):
    window.blit(background1, (0,bg_y))
    window.blit(background1, (0, bg_y-800))

def get_car1(x,y):
    value=random.randint(0,2)
    if value==0:
        car = pygame.image.load("materials_data/car1_blue.png")
        car = pygame.transform.scale(car, (50,75))
    elif value==1:
        car = pygame.image.load("materials_data/car1_yellow.png")
        car = pygame.transform.scale(car, (50,75))
    elif value==2:
        car = pygame.image.load("materials_data/car5_orange.png")
        car = pygame.transform.scale(car, (50,75))
    return [car, x, y, (x+4, y+3, 11, 10)]
carlist1.append(get_car1(103,0))

def get_car2(x,y):
    value=random.randint(0,2)
    if value == 0:
        car = pygame.image.load("materials_data/car4_purple.png")
        car = pygame.transform.scale(car, (50,75))
    elif value == 1:
        car = pygame.image.load("materials_data/car4_green.png")
        car = pygame.transform.scale(car, (50,75))
    elif value == 2:
        car = pygame.image.load("materials_data/car5_red.png")
        car = pygame.transform.scale(car, (50,75))
    return [car, x, y, (x+4, y+3, 11, 10)]
carlist2.append(get_car2(280,-100))

def get_car3(x,y):
    value = random.randint(0, 2)
    if value == 0:
        car = pygame.image.load("materials_data/car7_yellow.png")
        car = pygame.transform.scale(car, (50,75))
    elif value == 1:
        car = pygame.image.load("materials_data/car6_blue.png")
        car = pygame.transform.scale(car, (50, 75))
    elif value == 2:
        car = pygame.image.load("materials_data/car4_green.png")
        car = pygame.transform.scale(car, (50, 75))
    return [car, x, y, (x+4, y+3, 11, 10)]
carlist3.append(get_car3(445,-200))

def get_carleft(x,y):
    value=random.randint(0,2)
    if value==0:
        car = pygame.image.load("materials_data/car4_green.png")
        car = pygame.transform.scale(car, (50,75))
    elif value==1:
        car = pygame.image.load("materials_data/car1_yellow.png")
        car = pygame.transform.scale(car, (50,75))
    elif value==2:
        car = pygame.image.load("materials_data/car4_purple.png")
        car = pygame.transform.scale(car, (50,75))
    return [car, x, y, (x+4, y+3, 11, 10)]
carlistleft.append(get_carleft(190,-220))

def get_carright(x,y):
    value=random.randint(0,2)
    if value==0:
        car = pygame.image.load("materials_data/car1_blue.png")
        car = pygame.transform.scale(car, (50,75))
    elif value==1:
        car = pygame.image.load("materials_data/car5_orange.png")
        car = pygame.transform.scale(car, (50,75))
    elif value==2:
        car = pygame.image.load("materials_data/car7_yellow.png")
        car = pygame.transform.scale(car, (50,75))
    return [car, x, y, (x+4, y+3, 11, 10)]
carlistright.append(get_carright(360,-400))

def get_coin(x,y):
    coin = pygame.image.load("materials_data/coins_hud.png")
    coin = pygame.transform.scale(coin, (15,15))
    return [coin, x, y, (x+4, y+3, 11, 10)]
coin_list.append(get_coin(450,0))

def gameover(score):
    maks=max(score_list)
    window.blit(game_over, game_over_rect)
    window.blit(press_space,(90,450))
    window.blit(high_score_img, (195,270))
    text2=font2.render(f"{50*maks} m", True, (0,0,0))
    window.blit(text2, (410, 301))
    window.blit(score_img, (245,350))
    text3 = font2.render(f"{50*score} m", True, (0,0,0))
    window.blit(text3, (350,361))
    if score >= maks:
        text4=font4.render("NEW RECORD!", True, (0,0,255))
        window.blit(text4,(155,430))

def start():
    window.blit(press_space,(85,300))
    window.blit(logo,(200,100))


font=pygame.font.Font("freesansbold.ttf", 20)
font2=pygame.font.Font("freesansbold.ttf", 30)
font3=pygame.font.Font("freesansbold.ttf", 35)
font4=pygame.font.Font("freesansbold.ttf", 40)

right_regularly=True
left_regularly=True

go=False
st=True
running=True
stop=False

run = True
l=True
r=False

while True:
    window.blit(menu_bg, (0, 0))
    window.blit(bg1, (100, 300))
    window.blit(bg2, (400, 300))
    window.blit(press_space2, (135, 420))
    window.blit(logo2, (245, 580))
    while run:
        while l:
            window.blit(bg1dark, (100, 300))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        window.blit(bg1, (100, 300))
                        r = True
                        l = False
                    if event.key == pygame.K_SPACE:
                        background1 = pygame.image.load("materials_data/bg1.jpg")
                        background1 = pygame.transform.scale(background1, (600, 800))

                        background1_glow = pygame.image.load("materials_data/background1_glow.jpg")
                        background1_glow = pygame.transform.scale(background1_glow, (600, 800))

                        l=False
                        run = False
        while r:
            window.blit(bg2dark, (400, 300))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        window.blit(bg2, (400, 300))
                        l = True
                        r = False
                    if event.key == pygame.K_SPACE:
                        background1 = pygame.image.load("materials_data/background-1_0.png")
                        background1 = pygame.transform.scale(background1, (600, 800))

                        background1_glow = pygame.image.load("materials_data/background1_glow.jpg")
                        background1_glow = pygame.transform.scale(background1_glow, (600, 800))

                        r=False
                        run = False
    score_list.append(score)
    window.blit(background1_glow,(0,0))
    window.blit(pause, (540,3))
    while stop:
        maks = max(score_list)
        window.blit(pause_img, (187, 100))
        window.blit(high_score_img, (190,185))
        text2 = font3.render(f"{maks*50} m", True, (0,0,0))
        window.blit(text2, (405, 215))
        window.blit(score_img, (245, 270))
        text3 = font3.render(f"{score*50} m", True, (0, 0, 0))
        window.blit(text3, (350, 280))
        window.blit(press_space, (88, 300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stop=False


    for coin in coin_list:
        window.blit(coin[0], (coin[1], coin[2]))
        coin[2]+=coin_y_change
        if coin[2] == 648:
            coin_list.append(get_coin(450, 0))
            score+=1

    bg_y += 6
    floor_loop(bg_y)
    if bg_y >= 800:
        bg_y = 0




    while running:
        if go:
            for car1 in carlist1:
                carlist1.remove(car1)
            for car2 in carlist2:
                carlist2.remove(car2)
            for car3 in carlist3:
                carlist3.remove(car3)
            for carleft in carlistleft:
                carlistleft.remove(carleft)
            for carright in carlistright:
                carlistright.remove(carright)
            for coin in coin_list:
                coin_list.remove(coin)
            gameover(score)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        score=0
                        mycar_rect.center=(280,650)
                        running = False
                        carlist1.append(get_car1(103, 0))
                        carlist2.append(get_car2(280, -100))
                        carlist3.append(get_car3(445, -200))
                        carlistleft.append(get_carleft(190,-220))
                        carlistright.append(get_carright(360,-400))
                        coin_list.append(get_coin(450, 0))

        if st:
            start()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        score = 0
                        running = False
                        st = False






    window.blit(score_img, (-5, -5))

    window.blit(mycar, (mycar_x, mycar_y))
    #pygame.draw.rect(window,(255,0,0),(mycar_x+1,mycar_y,49,75),1)


    text2 = font.render(f"{score*50} m", True, (0, 0, 0))
    window.blit(text2, (95, 10))
    window.blit(resume, (550, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                stop=True



    key=pygame.key.get_pressed()
    if left_regularly==True and right_regularly==True:
        if key[pygame.K_a]:
            mycar_x-=mycar_x_change
        if key[pygame.K_d]:
            mycar_x += mycar_x_change

    if right_regularly == True and left_regularly == False:
        if key[pygame.K_d]:
            mycar_x += mycar_x_change
            left_regularly=True

    if left_regularly == True and right_regularly == False:
        if key[pygame.K_a]:
            mycar_x-=mycar_x_change
            right_regularly=True

    if mycar_x<=58:
        left_regularly=False
    if mycar_x>=489:
        right_regularly=False

    for car in carlist1:
        window.blit(car[0], (car[1], car[2]))
        car[2]+=car_y_change
        #pygame.draw.rect(window, (255,0,0), (car[1]+1, car[2]-1, 48,72), 1)
        if car[2] == 450:
            carlist1.append(get_car1(103,cor1[random.randint(0,3)]))

    for car in carlist1:
        if rect().colliderect(car[1]+1, car[2]-1, 48,72):
            '''coin_sound=mixer.Sound("sound_data/coin-collect-variant-sound-effect.mp3")
            coin_sound.set_volume(1)
            coin_sound.play()'''
            running=True
            go=True
            score_list.append(score)

    for car in carlist2:
        window.blit(car[0], (car[1], car[2]))
        car[2]+=car_y_change
        #pygame.draw.rect(window, (255,0,0), (car[1]+1, car[2]-1, 48,72), 1)
        if car[2] == 350:
            carlist2.append(get_car2(280,cor2[random.randint(0,3)]))

    for car in carlist2:
        if rect().colliderect(car[1]+1, car[2]-1, 48,72):
            '''coin_sound=mixer.Sound("sound_data/coin-collect-variant-sound-effect.mp3")
            coin_sound.set_volume(1)
            coin_sound.play()'''
            running = True
            go = True
            score_list.append(score)

    for car in carlist3:
        window.blit(car[0], (car[1], car[2]))
        car[2]+=car_y_change
        #pygame.draw.rect(window, (255,0,0), (car[1]+1, car[2]-1, 48,72), 1)
        if car[2] == 250:
            carlist3.append(get_car3(445,cor3[random.randint(0,1)]))

    for car in carlist3:
        if rect().colliderect(car[1]+1, car[2]-1, 48,72):
            '''coin_sound=mixer.Sound("sound_data/coin-collect-variant-sound-effect.mp3")
            coin_sound.set_volume(1)
            coin_sound.play()'''
            running = True
            go = True
            score_list.append(score)

    for car in carlistleft:
        window.blit(car[0], (car[1], car[2]))
        car[2]+=car_y_change
        #pygame.draw.rect(window, (255,0,0), (car[1]+1, car[2]-1, 48,72), 1)
        if car[2] == 800:
            carlistleft.append(get_carleft(190,corleft[random.randint(0,1)]))

    for car in carlistleft:
        if rect().colliderect(car[1]+1, car[2]-1, 48,72):
            '''coin_sound=mixer.Sound("sound_data/coin-collect-variant-sound-effect.mp3")
            coin_sound.set_volume(1)
            coin_sound.play()'''
            running=True
            go=True
            score_list.append(score)

    for car in carlistright:
        window.blit(car[0], (car[1], car[2]))
        car[2]+=car_y_change
        #pygame.draw.rect(window, (255,0,0), (car[1]+1, car[2]-1, 48,72), 1)
        if car[2] == 900:
            carlistright.append(get_carright(360,corright[random.randint(0,1)]))

    for car in carlistright:
        if rect().colliderect(car[1]+1, car[2]-1, 48,72):
            '''coin_sound=mixer.Sound("sound_data/coin-collect-variant-sound-effect.mp3")
            coin_sound.set_volume(1)
            coin_sound.play()'''
            running=True
            go=True
            score_list.append(score)





    pygame.display.update()
    clock.tick(60)