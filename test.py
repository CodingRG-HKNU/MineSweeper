import Board
import pygame
import time
import numpy as np

import Mine_Board

class Player_BoardCopy(Board.Board):

    def __init__(self, x, y, mine):
        # 생성자 오버로딩
        super(__class__, self).__init__(x, y)
        self.__init_Array(10)
        self.__numOpened = 0
        self.__numMines = mine
        self.gameover = False
        self.pause = False

    def __init_Array(self, k):
        for i in range(self.get_row()):
            for j in range(self.get_col()):
                self.set_cell(i, j, k)

    def open(self, x, y, b):
        #if x < 0 or y < 0 or x >= self.get_row() or y >= self.get_col():
        #    pass
        #elif not(self.__is_checked(x, y)):
        if 0 <= x < self.get_row() and 0 <= y < self.get_col() and not(self._is_checked(x, y)):
            copied = b.get_cell(x, y)
            if copied == 9:
                self.set_cell(x, y, copied)
                set_Image(img_list[copied],x*row,y*col)
                pygame.display.update()
                self.mineList = b.minePosition
                for x,y in self.mineList:
                    self.set_cell(x,y,copied)
                    set_Image(img_list[copied],x*row,y*col)
                    pygame.display.update()
                    bs.play()
                    pygame.time.wait(100)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                # for x,y in self.mineList:
                #     set_Image(ex,x*row,y*col)
                # pygame.display.update()
                # pygame.time.wait(100)

                self.GameOver()
                
            elif copied == 0:
                # for i in range(x-1, x+2):
                #     for j in range(y-1, y+2):
                #         if (i == x and j == y) or i < 0 or j < 0 or i >= self.get_row() or j >= self.get_col():
                #             continue
                #         # 재귀호출
                #         self.set_cell(x, y, copied)
                #         self.open(i, j, b)
                for i in range(max(x-1, 0), min(x+1, self.get_col()-1) + 1):
                    for j in range(max(y-1, 0), min(y+1, self.get_row()-1) + 1):
                        if (i == x and j == y):
                            continue
                        # 재귀호출
                        self.set_cell(x, y, copied)
                        self.get_cell(x,y)
                        set_Image(img_list[copied],x*row,y*col)
                        pygame.display.update()
                        if (i==x-1 or i ==x+1) and (j==y-1 or j==y+1) and b.get_cell(i,j) ==0:
                            continue
                        #bs.play()
                        self.open(i, j, b)
                        
            else:
                self.set_cell(x, y, copied)
                set_Image(img_list[copied],x*row,y*col)
                pygame.display.update()

                
            # 열은 칸 수 기록
            self.__numOpened += 1
            # 승리조건
            if (self.get_row() * self.get_col() - self.__numOpened) == self.__numMines:
                self.GameClear()

    def _is_checked(self, x, y):
        checked = False
        if self.get_cell(x, y) != 10:
            checked = True
        return checked

    def GameOver(self):
        self.gameover = True
        self.pause = True
        print("Game Over..")

    def GameClear(self):
        self.pause = True
        print("Game Clear !")
        # 승리


pygame.init()
window_width = 400
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mine Sweeper")
print(screen)
bs = pygame.mixer.Sound('shoot.wav')
clock = pygame.time.Clock()

row = 20
col = 20
mine = 50
mineB = Mine_Board.Mine_Board(row, col, mine)
playerB = Player_BoardCopy(row, col, mine)

ex = pygame.transform.scale(pygame.image.load("image/explode.jpg").convert(), (int(window_width / row), int(window_height / col)))

img_list = []
for i in range(12):
    img_list.append(pygame.transform.scale(pygame.image.load("image/"+str(i)+".jpg").convert(), (int(window_width / row), int(window_height / col))))

def set_Image(img, x, y):
    ##나중에 초기화만 따로 빼도 됨
    a = screen.blit(img, (x, y))
    return a
    # print(a)
    #pygame.draw.rect(screen,(255,0,0),a,5)

#screen.blit(rect,rect.get_rect)
    



def game_loop():
    loop = True
    i=0
    img_surface = []
    for x in range(row):
        for y in range(col):
            img_surface.append(img_list[playerB.get_cell(x,y)])
            set_Image(img_list[playerB.get_cell(x, y)], x*row, y*col)

    img_surface = np.reshape(img_surface,(row,col))
    print(img_surface)
    
    pre_rect = pygame.Rect(0,0,0,0) ##

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # elif event.type == pygame.MOUSEMOTION:
            #     mouse = event.pos
            #     x, y = int(mouse[0]//col), int((mouse[1])//row)
            #     if 0 <= x < playerB.get_row() and 0 <= y < playerB.get_col() and not(playerB._is_checked(x,y)):
            #     # print(mouse)
            #     # print(x,y)
            #         point = playerB.get_cell(x,y)
            #         #if point == 10:
            #         #img_pos : 현재 마우스가 위치한 셀의 좌표
            #         img_pos = (x * img_surface[x,y].get_rect()[2], y * img_surface[x,y].get_rect()[3])
            #         # print(img_pos)

            #         #rect = set_Image(img_list[10],img_pos[0],img_pos[1])
            #         rect = pygame.Rect(img_pos,(20,20))
                    

            #         if not(pre_rect.collidepoint(mouse[0],mouse[1])) and not(playerB._is_checked((pre_rect[0]//col),(pre_rect[1]//row))):
            #             print("Tt")
            #             set_Image(img_list[10],pre_rect[0],pre_rect[1])
            #             # pygame.draw.rect(screen,(255,255,255),pre_rect)

            #         if rect.collidepoint(mouse[0],mouse[1]):
            #             #렉트에 대한 설정을 하고 그려줘야지
            #             pygame.draw.rect(screen,(0,0,0,128),rect,1)
            #             pre_rect = rect
            #             print(pre_rect)

            elif event.type == pygame.MOUSEBUTTONUP and not(playerB.pause):
                mousex, mousey = event.pos
                x, y = int(mousex/row), int(mousey/col)
                # 좌클릭
                if event.button == 1:
                    playerB.open(x, y, mineB)

                # 우클릭
                elif event.button == 3:
                    bs.play()
                    if playerB.get_cell(x, y) == 10:
                        playerB.set_cell(x, y, 11)
                        set_Image(img_list[11],x*row,y*row)

                    elif playerB.get_cell(x, y) == 11:
                        playerB.set_cell(x, y, 10)
                        set_Image(img_list[10],x*row,y*row)

#         clock.tick(30)
#         pygame.display.update()
#         loop = not(playerB.gameover)


# print("Mine Sweeper!")
# game_loop()
# pygame.time.wait(1000)
# pygame.quit()
# quit()

        #if 0 <= x < self.get_row() and 0 <= y < self.get_col() and playerB.get_cell(x,y) == 10:

        mouse = pygame.mouse.get_pos()
        # print(mouse)
        x, y = int(mouse[0]//col), int((mouse[1])//row)
        if 0 <= x < playerB.get_row() and 0 <= y < playerB.get_col() and not(playerB._is_checked(x,y)):
            # print(mouse)
            # print(x,y)
            point = playerB.get_cell(x,y)
            #if point == 10:
            #img_pos : 현재 마우스가 위치한 셀의 좌표
            #img_pos = (x * img_surface[x,y].get_rect()[2], y * img_surface[x,y].get_rect()[3])
            img_pos = (x * 20, y * 20)
                # print(img_pos)

            #rect = set_Image(img_list[10],img_pos[0],img_pos[1])
            rect = pygame.Rect(img_pos,(20,20))
            

            if not(pre_rect.collidepoint(mouse[0],mouse[1])) and not(playerB._is_checked((pre_rect[0]//col),(pre_rect[1]//row))):
                print("Tt")
                set_Image(img_list[10],pre_rect[0],pre_rect[1])
                set_Image(img_list[10],0,380)
                # pygame.draw.rect(screen,(255,255,255),pre_rect)

            if rect.collidepoint(mouse[0],mouse[1]):
                #렉트에 대한 설정을 하고 그려줘야지
                pygame.draw.rect(screen,(0,0,0,128),rect,1)
                pre_rect = rect
                #print(pre_rect)

        clock.tick(30)
        pygame.display.update()
        loop = not(playerB.gameover)


print("Mine Sweeper!")
game_loop()
pygame.time.wait(1000)
pygame.quit()
quit()

            #마우스 좌표를 새로 얻어와야지 



'''
        mouse = pygame.mouse.get_pos()
        x, y = int(mouse[0]//col), int((mouse[1])//row)
        if 0 <= x < playerB.get_row() and 0 <= y < playerB.get_col() and not(playerB._is_checked(x,y)):
            point = playerB.get_cell(x,y)
            img_pos = (x * img_surface[x,y].get_rect()[2], y * img_surface[x,y].get_rect()[3])
            #rect = pygame.Rect(img_pos,(20,20))
            if not(pre_rect.collidepoint(mouse[0],mouse[1])):
                
                print("Tt")
                pygame.draw.rect(screen,(255,255,255),pre_rect)
'''
                

'''    

            if not(pre_pos[0]<mouse[0]<pre_pos[0]+20 and pre_pos[1]<mouse[1]<(pre_pos[1]+20)):
                # img_surface[x,y].set_alpha(0)
                set_Image(img_surface[x,y],img_pos[0],img_pos[1])
                #pygame.draw.rect(screen, (255,255,255,255), img_pos+(20,20), 1)
                #set_Image(img_list[10],pre_pos[0],pre_pos[1])

            if img_pos[0]<mouse[0]<img_pos[0]+20 and img_pos[1]<mouse[1]<(img_pos[1]+20):
                #이미지의 경우 (0,0,width,height)
                #print(img_surface[x,y].get_rect().collidepoint(pygame.mouse.get_pos()))
                rect = set_Image(img_list[10],img_pos[0],img_pos[1])
                print(rect)
                if rect.collidepoint(mouse[0],mouse[1]):
                    pygame.draw.rect(screen,(255,0,0,255),rect)
                ##자명한 사실이니까 if 없이 그냥해보자
                ##pygame.draw.rect(screen, (0,0,0), img_pos+(20,20), 1)
                #img_surface[x,y].set_alpha(128)
                #print(img_pos[0],img_pos[1])
                # set_Image(img_surface[x,y],img_pos[0],img_pos[1])
                pre_pos = img_pos

'''
'''
        
                    

        # 이미지 처리
        if playerB.gameover:
            for x,y in playerB.mineList:
                set_Image(ex,x*row,y*col)
        # else:
        #     for x in range(row):
        #         for y in range(col):
        #             set_Image(img_list[playerB.get_cell(x, y)], x*row, y*col)

        #파우즈 사용하기
'''
#         clock.tick(30)
#         pygame.display.update()
#         loop = not(playerB.gameover)


# print("Mine Sweeper!")
# game_loop()
# pygame.time.wait(1000)
# pygame.quit()
# quit()