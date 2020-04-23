import Board

class Player_Board(Board.Board):

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

        if 0 <= x < self.get_row() and 0 <= y < self.get_col() and not(self._is_checked(x, y)):
            copied = b.get_cell(x, y)
            if copied == 9:
                self.set_cell(x, y, copied)
                ## 전체 마인 표시
                mineList = b.minePosition
                for x,y in mineList:
                    self.set_cell(x,y,copied)
                    #bs.play()

                self.GameOver()
                
            elif copied == 0:

                for i in range(max(x-1, 0), min(x+1, self.get_col()-1) + 1):
                    for j in range(max(y-1, 0), min(y+1, self.get_row()-1) + 1):
                        if (i == x and j == y):
                            continue
                        # 재귀호출
                        self.set_cell(x, y, copied)
                        # bs.play()
                        ##너무 많이 까지는거 제한
                        if (i==x-1 or i ==x+1) and (j==y-1 or j==y+1) and b.get_cell(i,j) ==0:
                            continue
                        self.open(i, j, b)
                        
            else:
                self.set_cell(x, y, copied)
                
            # 열은 칸 수 기록
            self.__numOpened += 1
            ## 승리조건 not(gameover)추가
            if (self.get_row() * self.get_col() - self.__numOpened) == self.__numMines and not(self.gameover):
                self.GameClear()
            ##결국 처음 오픈한 값 리턴 -> 리턴 값에 따라 소리 재생
            return copied

    def _is_checked(self, x, y):
        checked = False
        if self.get_cell(x, y) != 10:
            checked = True
        return checked

    def GameOver(self):
        self.gameover = True
        #self.pause = True
        print("Game Over..")

    def GameClear(self):
        self.pause = True
        print("Game Clear !")
        # 승리

