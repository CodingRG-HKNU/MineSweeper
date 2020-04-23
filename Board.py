class Board:
    # python 은 기본적으로 모두 public 으로 접근제어를 제공하지 않는다.
    # 접근제어자는 naming 으로만. private : __name , protected : _name
    def __init__(self, x, y):
        self.__rows = x
        self.__cols = y
        self.__make_array(self.__rows, self.__cols)

    def get_cell(self, x, y):
        return self.__mine_Array[x][y]

    def get_row(self):
        return self.__rows

    def get_col(self):
        return self.__cols

    def set_cell(self, x, y, s):
        self.__mine_Array[x][y] = s

    def __make_array(self, x, y):
        # 2차원 동적 배열 생성 , 값을 0으로 초기화
        self.__mine_Array = [[0 for col in range(y)] for row in range(x)]

