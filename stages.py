# Stage 5.5/6: Automatic answer
class KnightTourPuzzle:
    def __init__(self):
        self.board, self.solution = [], []
        self.x, self.y, self.row, self.col, self.cell_size, self.count = 0, 0, 0, 0, 0, 1

    def create_board(self):
        while True:
            try:
                self.col, self.row = [int(i) for i in input("Enter your board dimensions: ").split()]
                if self.row <= 0 or self.col <= 0:
                    raise ValueError
                else:
                    self.cell_size = len(str(self.col * self.row))
                    self.board = [["_" * self.cell_size for _ in range(self.col)] for _ in range(self.row)]
                    break
            except ValueError:
                print("Invalid dimensions!")

    def starting_position(self):
        while True:
            try:
                self.y, self.x = [int(i) for i in input("Enter the knight's starting position: ").split()]
                if 1 <= self.x <= self.row and 1 <= self.y <= self.col:
                    self.board[self.x - 1][self.y - 1] = " " * (self.cell_size - 1) + "X"
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid position!")

    def display(self):
        print(" " * len(str(self.row)) + "-" * (self.col * (self.cell_size + 1) + 3))
        for i in range(self.row, 0, -1):
            print((" " * (len(str(self.row)) - len(str(i)))) + str(i) + "| " + " ".join(self.board[i - 1]) + " |")
        print(" " * len(str(self.row)) + "-" * (self.col * (self.cell_size + 1) + 3))
        temp = [" " * (self.cell_size - len(str(i))) + str(i) for i in range(1, self.col + 1)]
        print(" " * (len(str(self.row)) + 2) + " ".join(temp) + "  " + "\n")

    def game_status(self, board):
        if not any([1 if j == "_" * self.cell_size else 0 for i in board for j in i]):
            return "won"
        elif self.valid_move(self.x, self.y) == 0:
            return "lost"
        return "continue"

    def valid_move(self, x, y, option="count"):
        valid_move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, 2), (1, -2), (2, -1), (2, 1)]
        total_move, valid_moves = 0, {}
        for i in valid_move:
            if 1 <= x + i[0] <= self.row and 1 <= y + i[1] <= self.col \
                    and self.board[x + i[0] - 1][y + i[1] - 1] == "_" * self.cell_size:
                total_move += 1
                if option == "replace":
                    self.board[x + i[0] - 1][y + i[1] - 1] = " " * (self.cell_size - 1) \
                                                             + str(self.valid_move(x + i[0], y + i[1]))
                elif option == "rank":
                    valid_moves[(x + i[0], y + i[1])] = self.valid_move(x + i[0], y + i[1])
        return total_move if option == "count" else valid_moves

    def check_solution(self):
        self.solution = self.board
        while True:
            if self.game_status(self.solution) == "continue":
                self.solution[self.x - 1][self.y - 1] = " " * (self.cell_size - len(str(self.count))) + str(self.count)
                rank_dic = sorted(self.valid_move(self.x, self.y, "rank").items(), key=lambda x: x[1])
                if len(rank_dic) > 1:
                    rank_dic = [i for i in rank_dic if i[1] > 0 and any([i[1] for i in rank_dic])]
                if self.count < self.row * self.col:
                    self.x, self.y = rank_dic[0][0]
                self.count += 1
            elif self.game_status(self.solution) == "won":
                return True
            else:
                self.solution[self.x - 1][self.y - 1] = " " * (self.cell_size - len(str(self.count))) + str(self.count)
                return False

    def play(self):
        self.create_board()
        self.starting_position()
        self.check_solution()
        self.board = self.solution
        self.display()


knight_tour = KnightTourPuzzle()
knight_tour.play()

