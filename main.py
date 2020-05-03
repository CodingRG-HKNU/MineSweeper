import Mine_Board
import Player_Board
import pygame
import time
from random import randint as ri

pygame.init()

game_width, game_height = (800,600)
window_width, window_height = (400,400)

margin_width = (game_width - window_width)/2
margin_height = (game_height - window_height)/2

screen = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("Mine Sweeper")

inner = pygame.Surface((window_width,window_height))

clock = pygame.time.Clock()

row = 20
col = 20
mine = 50

##게임루프 안에서 중복
mineB = Mine_Board.Mine_Board(row, col, mine)
playerB = Player_Board.Player_Board(row, col, mine)

bg = pygame.transform.scale(pygame.image.load("./background/bg.jpg").convert(),(game_width,game_height))

# 이미지 저장
img_list = []
img_size = (20,20)
for i in range(12):
    img_list.append(pygame.transform.scale(pygame.image.load("image/"+str(i)+".jpg").convert(), (int(window_width / row), int(window_height / col))))

# 이미지 출력 함수
def set_Image(img, x, y):
    inner.blit(img, (x, y))
    

# 메인 게임 루프
def game_loop():
    global mineB
    global playerB

    while True:
        start_time = time.time()

        mineB = Mine_Board.Mine_Board(row, col, mine)
        playerB = Player_Board.Player_Board(row, col, mine)

        while not(playerB.gameover) and not(playerB.pause):
            ptime = time.time() - start_time
            m,s = ptime//60, ptime%60
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONUP and not(playerB.pause):
                    mousex, mousey = event.pos
                    x, y = int((mousex-margin_width)//row), int((mousey-margin_height)//col)
                    # 좌클릭
                    if event.button == 1:
                        opened = playerB.open(x, y, mineB)
                    # 우클릭
                    elif event.button == 3:
                        if playerB.get_cell(x, y) == 10:
                            playerB.set_cell(x, y, 11)
                        elif playerB.get_cell(x, y) == 11:
                            playerB.set_cell(x, y, 10)
                            
            # 이미지 처리 전에 스크린 fill 해줘야 잔상 안남음
            screen.blit(bg,(0,0))

            # 이미지 처리
            for x in range(row):
                for y in range(col):
                    set_Image(img_list[playerB.get_cell(x, y)], x*row, y*col)

            screen.blit(inner,(margin_width,margin_height))

            display_time = pygame.Rect(margin_width + window_width - 100,margin_height+window_height+10,100,30)
            display_mine = pygame.Rect(margin_width,margin_height+window_height+10,100,30)

            pygame.draw.rect(screen,(0,0,0),display_time)
            pygame.draw.rect(screen,(0,0,0),display_mine)

            font = pygame.font.Font(None, 30)
            text_mine_surf = font.render(str(mineB.get_numMines()),True,(255,0,0))
            text_time_surf = font.render((format(int(m),'02') + ":" +format(int(s),'02')),True,(255,0,0))
            text_mine_rect = text_mine_surf.get_rect()
            text_time_rect = text_time_surf.get_rect()
            text_mine_rect.center = display_mine.center
            text_time_rect.center = display_time.center

            screen.blit(text_time_surf,text_time_rect)
            screen.blit(text_mine_surf,text_mine_rect)
            
            mouse = pygame.mouse.get_pos()

            x, y = int((mouse[0]-margin_width)//col), int((mouse[1]-margin_height)//row)
            if 0 <= x < playerB.get_row() and 0 <= y < playerB.get_col() and not(playerB._is_checked(x,y)):
                point = playerB.get_cell(x,y)
                img_pos = (x * 20+margin_width, y * 20+margin_height)
                rect = pygame.Rect(img_pos,(20,20))
                
                if rect.collidepoint(mouse[0],mouse[1]):
                    a = pygame.draw.rect(screen,(ri(0,255),ri(0,255),ri(0,255),128),rect,2)
                    del(a)
   
            clock.tick(30)
            pygame.display.update()

        if playerB.gameover:
            gameover()
        
        if playerB.pause:
            gameclear()
            

def gameover():
    font = pygame.font.Font(None, 50)
    text = font.render("Game Over", True, (255,0,0))
    textRect = text.get_rect()
    textRect.center = inner.get_rect().center
    while playerB.gameover:
        inner.blit(text, textRect)
        screen.blit(inner,(margin_width,margin_height))
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
    textRect.center = inner.get_rect().center
    while playerB.pause:
        inner.blit(text, textRect)
        screen.blit(inner,(margin_width,margin_height))
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
pygame.quit()
quit()
