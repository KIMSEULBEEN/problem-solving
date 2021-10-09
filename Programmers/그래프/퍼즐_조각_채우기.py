class PuzzleClass:
    def __init__(self, game_board, table):
        # region -> 공통 변수 & 상수]
        self.labels = dict()
        self.label = 10  # 현재 퍼즐 조각 번호
        self.label_count = 0  # 퍼즐 조각 갯수

        self.BACKGROUND_NUM = 0  # 배경 상수
        self.LEN_MATRIX = len(game_board)
        # endregion

        # region -> game_board 관련 변수
        self.game_board = self.get_reverse_matrix(game_board)
        self.labels_gb = dict()

        self.label_gb = 10
        self.label_count_gb = 0
        # endregion

        # region -> table 관련 변수
        self.table = table

        self.label_gb = 10
        self.label_count_gb = 0
        # endregion

    def get_reverse_matrix(self, matrix):
        for row in range(self.LEN_MATRIX):
            for col in range(self.LEN_MATRIX):
                if matrix[row][col] == 1:
                    matrix[row][col] = 0
                else:
                    matrix[row][col] = 1
        return matrix

    def get_labeled_matrix(self, matrix):
        """
        전체 matrix에 대해 라벨링된 매트릭스를 리턴받음
        :param matrix:
        :return:
        """

        self.labels = dict()
        for row in range(self.LEN_MATRIX):
            for col in range(self.LEN_MATRIX):
                if matrix[row][col] == 1:
                    self.label += 1
                    self.labels[self.label] = 0
                    self.get_labeled_matrix_pixel(matrix, row, col)

        return matrix

    def get_labeled_matrix_pixel(self, matrix, row, col):
        """
        특정 row와 col 기준 라벨링된 매트릭스를 리턴받음
        :param matrix:
        :return:
        """

        if (0 <= row < self.LEN_MATRIX and
                0 <= col < self.LEN_MATRIX):

            if matrix[row][col] == 1:
                matrix[row][col] = self.label
                self.labels[self.label] += 1

                self.get_labeled_matrix_pixel(matrix, row - 1, col)
                self.get_labeled_matrix_pixel(matrix, row + 1, col)
                self.get_labeled_matrix_pixel(matrix, row, col - 1)
                self.get_labeled_matrix_pixel(matrix, row, col + 1)

        return matrix


game_board, table = [[1, 1, 0, 0, 1, 0],
                     [0, 0, 1, 0, 1, 0],
                     [0, 1, 1, 0, 0, 1],
                     [1, 1, 0, 1, 1, 1],
                     [1, 0, 0, 0, 1, 0],
                     [0, 1, 1, 1, 0, 0]], \
                    [[1, 0, 0, 1, 1, 0],
                     [1, 0, 1, 0, 1, 0],
                     [0, 1, 1, 0, 1, 1],
                     [0, 0, 1, 0, 0, 0],
                     [1, 1, 0, 1, 1, 0],
                     [0, 1, 0, 0, 0, 0]]

puzzle_class = PuzzleClass(game_board, table)
puzzle_class.game_board = puzzle_class.get_labeled_matrix(puzzle_class.game_board)

for row in puzzle_class.game_board:
    print(row)
# print(puzzle_class.table)
