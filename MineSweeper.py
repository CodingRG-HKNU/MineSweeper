import Mine_Board
import Player_Board
import pygame
import time
from random import randint as ri

pygame.init()
game_width = 500
game_height = 500

window_width = 400
window_height = 400
screen = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("Mine Sweeper")
bs = pygame.mixer.Sound('boom.wav')
bs1 = pygame.mixer.Sound('magic.wav')
bs2 = pygame.mixer.Sound('shoot.wav')

clock = pygame.time.Clock()

row = 20
col = 20
mine = 50
mineB = Mine_Board.Mine_Board(row, col, mine)
playerB = Player_Board.Player_Board(row, col, mine)


# 이미지 저장
img_list = []
img_size = (20,20)
for i in range(12):
    img_list.append(pygame.transform.scale(pygame.image.load("image/"+str(i)+".jpg").convert(), (int(window_width / row), int(window_height / col))))

# 이미지 출력 함수
def set_Image(img, x, y):
    screen.blit(img, (x, y))
    

# 효과음
def play_Sound():
    bs.play()


# start_time = time.time()
# while True:
#     ptime = time.time() - start_time
#     m,s = ptime//60, ptime%60
#     print(str(int(m))+":"+"%.0f"%s)
#     time.sleep(1)

# 메인 게임 루프
def game_loop():
    global mineB
    global playerB
    while True:
        loop = True
        #intro()
        start_time = time.time()

        mineB = Mine_Board.Mine_Board(row, col, mine)
        playerB = Player_Board.Player_Board(row, col, mine)

        #pre_rect = pygame.Rect(0,0,0,0)

        while not(playerB.gameover) and not(playerB.pause):
            ptime = time.time() - start_time
            m,s = ptime//60, ptime%60
            print(int(m),int(s))
            #print(str(int(m))+":"+"%.0f"%s)
            #print(mineB.get_numMines())
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONUP and not(playerB.pause):
                    mousex, mousey = event.pos
                    x, y = int((mousex-50)//row), int((mousey-50)//col)
                    # 좌클릭
                    if event.button == 1:
                        ## 셀 값을 받아 소리재생
                        opened = playerB.open(x, y, mineB)
                        if opened == 9:
                            play_Sound()
                        elif opened == 0:
                            bs1.play()


                    # 우클릭
                    elif event.button == 3:
                        if playerB.get_cell(x, y) == 10:
                            playerB.set_cell(x, y, 11)
                        elif playerB.get_cell(x, y) == 11:
                            playerB.set_cell(x, y, 10)
                            
            '''
                elif event.type == pygame.MOUSEMOTION:
                    mouse = event.pos
                    x, y = int(mouse[0]//col), int((mouse[1])//row)
                    if 0 <= x < playerB.get_row() and 0 <= y < playerB.get_col() and not(playerB._is_checked(x,y)):
                    # print(mouse)
                    # print(x,y)
                        point = playerB.get_cell(x,y)
                        #if point == 10:
                        #img_pos : 현재 마우스가 위치한 셀의 좌표
                        img_pos = (x * img_size[0], y * img_size[1])
                        # print(img_pos)

                        #rect = set_Image(img_list[10],img_pos[0],img_pos[1])
                        rect = pygame.Rect(img_pos,(20,20))
                        

                        if not(pre_rect.collidepoint(mouse[0],mouse[1])) and not(playerB._is_checked((pre_rect[0]//col),(pre_rect[1]//row))):
                            print("Tt")
                            set_Image(img_list[10],pre_rect[0],pre_rect[1])
                            # pygame.draw.rect(screen,(255,255,255),pre_rect)

                        if rect.collidepoint(mouse[0],mouse[1]):
                            #렉트에 대한 설정을 하고 그려줘야지
                            pygame.draw.rect(screen,(0,0,0,128),rect,1)
                            pre_rect = rect
                            print(pre_rect)
                            
            '''
            ##이미지 처리 전에 스크린 fill 해줘야 잔상 안남음
            screen.fill((255,255,255))
            # 이미지 처리
            for x in range(row):
                for y in range(col):
                    set_Image(img_list[playerB.get_cell(x, y)], 50+x*row, 50+y*col)

            display_time = pygame.Rect(350,460,100,30)
            display_mine = pygame.Rect(50,460,100,30)

            pygame.draw.rect(screen,(0,0,0),display_time)
            pygame.draw.rect(screen,(0,0,0),display_mine)
            #str(int(m))+":"+"%.0f"%s
            #str(mineB.get_numMines())

            font = pygame.font.Font(None, 30)
            text_mine_surf = font.render(str(mineB.get_numMines()),True,(255,0,0))
            text_time_surf = font.render((format(int(m),'02') + ":" +format(int(s),'02')),True,(255,0,0))
            text_mine_rect = text_mine_surf.get_rect()
            text_time_rect = text_time_surf.get_rect()
            text_mine_rect.center = display_mine.center
            text_time_rect.center = display_time.center
            ##print(text_time.get_rect())
            ##print(display_time.center)
            ##print(display_time)
            ##print(display_time)
            ##print(display_time.center)
            #str(int(m))+":"+"{%.0f}"%s, True, (255,0,0))
            ##screen.blit(text_time, (display_time.center[0]-25,display_time.center[1]-10))
            ##screen.blit(text_mine, (display_mine.center[0]-10,display_time.center[1]-10))
            screen.blit(text_time_surf,text_time_rect)
            screen.blit(text_mine_surf,text_mine_rect)
            
            mouse = pygame.mouse.get_pos()
            # print(mouse)
            x, y = int((mouse[0]-50)//col), int((mouse[1]-50)//row)
            if 0 <= x < playerB.get_row() and 0 <= y < playerB.get_col() and not(playerB._is_checked(x,y)):
                # print(mouse)
                # print(x,y)
                point = playerB.get_cell(x,y)
                #if point == 10:
                #img_pos : 현재 마우스가 위치한 셀의 좌표
                #img_pos = (x * img_surface[x,y].get_rect()[2], y * img_surface[x,y].get_rect()[3])
                img_pos = (x * 20+50, y * 20+50)
                    # print(img_pos)

                #rect = set_Image(img_list[10],img_pos[0],img_pos[1])
                rect = pygame.Rect(img_pos,(20,20))
                

                # if not(pre_rect.collidepoint(mouse[0],mouse[1])) and not(playerB._is_checked((pre_rect[0]//col),(pre_rect[1]//row))):
                #     print("Tt")
                    #set_Image(img_list[10],pre_rect[0],pre_rect[1])
                    # pygame.draw.rect(screen,(255,255,255),pre_rect)

                if rect.collidepoint(mouse[0],mouse[1]):
                    #렉트에 대한 설정을 하고 그려줘야지
                    a = pygame.draw.rect(screen,(ri(0,255),ri(0,255),ri(0,255),128),rect,2)
                    del(a)
                    #pre_rect = rect
                    #print(pre_rect)
                
            
            clock.tick(30)
            pygame.display.update()
            loop = not(playerB.gameover)

        if playerB.gameover:
            gameover()
        
        if playerB.pause:
            gameclear()
            

def intro():
    cap = pygame.transform.scale(pygame.image.load("cap.jpg").convert(), (window_width, window_height))
    lfont = pygame.font.Font(None,50)
    sfont = pygame.font.Font(None,30)

    title = lfont.render("Mine Sweeper",True,(0,0,0))
    start = sfont.render("Start",True,(0,0,0))
    option = sfont.render("option",True,(0,0,0))
    bye = sfont.render("bye",True,(0,0,0))

    print(title)
    titleRect = title.get_rect()
    startRect = start.get_rect()
    optionRect = option.get_rect()
    byeRect = bye.get_rect()
    print(titleRect)
    titleRect.center = screen.get_rect().center
    optionRect.center = (200,350)
    startRect.center = (100,350)
    byeRect.center = (300,350)

    intro = True
    while intro:
        screen.blit(cap,(0,0))
        screen.blit(title, titleRect)
        screen.blit(option, optionRect)
        screen.blit(start, startRect)
        screen.blit(bye, byeRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



def gameover():
    font = pygame.font.Font(None, 50)
    text = font.render("Game Over", True, (255,0,0))
    textRect = text.get_rect()
    textRect.center = screen.get_rect().center
    while playerB.gameover:
        screen.blit(text, textRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button ==1:
                    playerB.gameover = False

def gameclear():
    font = pygame.font.Font(None, 50)
    text = font.render("Clear", True, (0,0,255))
    textRect = text.get_rect()
    textRect.center = screen.get_rect().center
    while playerB.pause:
        screen.blit(text, textRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button ==1:
                    playerB.pause = False





print("Mine Sweeper!")
game_loop()
time.sleep(1)
pygame.quit()
quit()
