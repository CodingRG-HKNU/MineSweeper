import Mine_Board
import Player_Board
import pygame
import time
import numpy as np

pygame.init()

black = (0,0,0)
white = (255,255,255)

window_width = 420
window_height = 480

gamewidth = 400
gameheight = 400

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mine Sweeper")
screen.fill((220,220,220))
# print(screen)

empty_surface = pygame.Surface((gamewidth,gameheight))
#empty_surface.fill((255,0,255))
screen.blit(empty_surface,(200,0))

bs = pygame.mixer.Sound('shoot.wav')
clock = pygame.time.Clock()

row = 20
col = 20
mine = 50
mineB = Mine_Board.Mine_Board(row, col, mine)
playerB = Player_Board.Player_Board(row, col, mine)

# 이미지 저장
img_list = []
for i in range(12):
    img_list.append(pygame.transform.scale(pygame.image.load("image/"+str(i)+".jpg").convert(), (int(gamewidth / col), int(gameheight / row))))

# 이미지 출력 함수
def set_Image(img, x, y):
    screen.blit(img, (x, y))
    
    

# 효과음
def play_Sound():
    bs.play()

# 메인 게임 루프
def game_loop():
    loop = True

    # 이미지 처리
    ## 이미지 surface 배열 
    img_surface = []
    for x in range(row):
        for y in range(col):
            img_surface.append(img_list[playerB.get_cell(x,y)])
            set_Image(img_list[playerB.get_cell(x, y)], 10+x*row, 40+y*col)

    img_surface = np.reshape(img_surface,(row,col))
    print(img_surface)
    pre_pos =(-100,-100)

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # elif event.type == pygame.MOUSEMOTION:
            #     mousex, mousey = event.pos
            #     x, y = int(mousex/row), int(mousey/col)
            #     pygame.draw.rect(screen,(255,0,0),(mousex,mousey,50,50),10)
            #     pygame.display.update()
            #아마 셀을 set_cell해서 바꿧을 꺼야 전에는

            elif event.type == pygame.MOUSEBUTTONUP and not(playerB.pause):
                mousex, mousey = event.pos
                print(mousex,mousey)
                x, y = int(mousex//col), int((mousey-100)//row)
                print(x,y)
                # 좌클릭
                if event.button == 1:
                    playerB.open(x, y, mineB)

                # 우클릭
                elif event.button == 3:
                    bs.play()
                    if playerB.get_cell(x, y) == 10:
                        playerB.set_cell(x, y, 11)
                    elif playerB.get_cell(x, y) == 11:
                        playerB.set_cell(x, y, 10)

        # # 이미지 처리
        # for x in range(row):
        #     for y in range(col):
        #         set_Image(img_list[playerB.get_cell(x, y)], x*row, 100+y*col)

        mouse = pygame.mouse.get_pos()
        # print(mouse)
        x, y = int(mouse[0]//col), int((mouse[1]-100)//row)
        if 0 <= x < playerB.get_row() and 0 <= y < playerB.get_col():
            print(mouse)
            # print(x,y)
            point = playerB.get_cell(x,y)
            #img_pos : 현재 마우스가 위치한 셀의 좌표
            img_pos = (x * img_surface[x,y].get_rect()[2], y * img_surface[x,y].get_rect()[3]+100)
            # print(img_pos)

            if not(pre_pos[0]<mouse[0]<pre_pos[0]+20 and pre_pos[1]<mouse[1]<(pre_pos[1]+20)):
                set_Image(img_list[10],pre_pos[0],pre_pos[1])


            if img_pos[0]<mouse[0]<img_pos[0]+20 and img_pos[1]<mouse[1]<(img_pos[1]+20):
                set_Image(img_list[0],img_pos[0],img_pos[1])#자명한 사실이니까 if 없이 그냥해보자
                pre_pos = img_pos

            # if img_pos[0]<mouse[0]<img_pos[0]+20 and img_pos[1]<mouse[1]<(img_pos[1]+20):
            #     pre_pos = img_pos
            #     set_Image(img_list[0],img_pos[0],img_pos[1])
            
            # else:
            #     set_Image(img_list[10],img_pos[0],img_pos[1])
            
            # pre_pos = img_pos



        # if point == 10:
        #     if img_surface[x,y].get_rect[0]<x<img_surface[x,y].get_rect[0]+img_surface[x,y].get_rect[2] and img_surface[x,y].get_rect[1]<y<img_surface[x,y].get_rect[1]+img_surface[x,y].get_rect[3]:
        #         set_Image(img_list[0],img_surface.get_rect[0],img_surface.get_rect[1])
        #     else:
        #         set_Image(img_list[10],img_surface.get_rect[0],img_surface.get_rect[1])

        # for x in range(row):
        #     for y in range(col):
                
        #         set_Image(img_list[playerB.get_cell(x, y)], x*row, 100+y*col)
        

        clock.tick(30)
        pygame.display.update()
        loop = not(playerB.gameover)


print("Mine Sweeper!")
game_loop()
time.sleep(1)
pygame.quit()
quit()
