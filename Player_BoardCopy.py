import Board
import pygame
import time

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
        
        if 0 <= x < self.get_row() and 0 <= y < self.get_col() and not(self.__is_checked(x, y)):
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

                self.GameOver()
                
            elif copied == 0:

                for i in range(max(x-1, 0), min(x+1, self.get_col()-1) + 1):
                    for j in range(max(y-1, 0), min(y+1, self.get_row()-1) + 1):
                        if (i == x and j == y):
                            continue
                        # 재귀호출
                        self.set_cell(x, y, copied)
                        self.get_cell(x,y)
                        set_Image(img_list[copied],x*row,y*col)
                        pygame.display.update()
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

    def __is_checked(self, x, y):
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

'''
pygame.init()
window_width = 400
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mine Sweeper")
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
    screen.blit(img, (x, y))


def game_loop():
    loop = True
    for x in range(row):
        for y in range(col):
                set_Image(img_list[playerB.get_cell(x, y)], x*row, y*col)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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

        
                    

        # 이미지 처리
        if playerB.gameover:
            for x,y in playerB.mineList:
                set_Image(ex,x*row,y*col)
        # else:
        #     for x in range(row):
        #         for y in range(col):
        #             set_Image(img_list[playerB.get_cell(x, y)], x*row, y*col)

        #파우즈 사용하기

        clock.tick(30)
        pygame.display.update()
        loop = not(playerB.gameover)


print("Mine Sweeper!")
game_loop()
pygame.time.wait(1000)
pygame.quit()
quit()
'''