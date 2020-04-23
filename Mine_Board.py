import Board
import random
#random.seed(777)


class Mine_Board(Board.Board):

    def __init__(self, x, y, mine):
        # 생성자 오버로딩
        super().__init__(x, y)
        #Board.Board.__init__(x, y)
        self.__numMines = mine
        self.__set_Mine()
        self.__set_Num()

    def __set_Mine(self):
        ##마인 위치 기록
        self.minePosition = set()
        ##for문 안에 있던 제네레이터 밖으로 빼고
        g = self.gencoordinates(0, self.get_row()-1, 0, self.get_col()-1)
        for i in range(self.get_numMines()):
            # x = self.__get_RandNum(0, self.get_row()-1)
            # y = self.__get_RandNum(0, self.get_col()-1)
            x, y = next(g)
            self.minePosition.add((x,y))

            if self.get_cell(x, y) == 0:
                self.set_cell(x, y, 9)
            else:
                i -= 1  # i--
        print(len(self.minePosition),sorted(self.minePosition))

    def gencoordinates(self, r0, r1, c0, c1):
        seen = set()

        x, y = random.randint(r0, r1), random.randint(c0, c1)

        while True:
            seen.add((x, y))
            yield (x, y)
            x, y = random.randint(r0, r1), random.randint(c0, c1)
            
            while (x, y) in seen:
                x, y = random.randint(r0, r1), random.randint(c0, c1)

    # def __set_Num(self):
    #     for i in range(self.get_row()):
    #         for j in range(self.get_col()):
    #             if self.get_cell(i, j) != 9:
    #                 n = 0
    #                 for i2 in range(i-1, i+2):
    #                     for j2 in range(j-1, j+2):
    #                         if (i2 == i and j2 == j) or i2 < 0 or j2 < 0 or i2 >= self.get_row() or j2 >= self.get_col():
    #                             continue
    #                         elif self.get_cell(i2, j2) == 9:
    #                             n += 1
    #                 self.set_cell(i, j, n)
    # ㅁ ㅁ ㅁ
    # ㅁ ㅁ ㅁ
    # ㅁ ㅁ ㅁ  순회, 전체 보드를 벗어나는 경우 처리 : 최소 0 최대 row, col 

    def __set_Num(self):
        for i in range(self.get_row()):
            for j in range(self.get_col()):
                if self.get_cell(i, j) != 9:
                    n = 0
                    for i2 in range(max(i-1, 0),  min(i+1, self.get_row() - 1) + 1):
                        for j2 in range(max(j-1, 0),  min(j+1, self.get_col() - 1) + 1):
                            if (i2 == i and j2 == j):
                                continue
                            elif self.get_cell(i2, j2) == 9:
                                n += 1
                    self.set_cell(i, j, n)

    def __get_RandNum(self, r_min, r_max):
        return random.randint(r_min, r_max)

    def get_numMines(self):
        return self.__numMines



