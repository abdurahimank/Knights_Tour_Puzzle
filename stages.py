# Stage 6/6: Give me an answer
class KnightTourPuzzle:
    def __init__(self):
        self.board, self.solution = [], []
        self.x, self.y, self.row, self.col, self.cell, self.count = 0, 0, 0, 0, 0, 1

    def create_board(self):
        while True:
            try:
                self.col, self.row = [int(i) for i in input("Enter your board dimensions: ").split()]
                if self.row <= 0 or self.col <= 0:
                    raise ValueError
                else:
                    self.cell = len(str(self.col * self.row))
                    self.board = [["_" * self.cell for _ in range(self.col)] for _ in range(self.row)]
                    break
            except ValueError:
                print("Invalid dimensions!")

    def starting_position(self):
        while True:
            try:
                self.y, self.x = [int(i) for i in input("Enter the knight's starting position: ").split()]
                if 1 <= self.x <= self.row and 1 <= self.y <= self.col:
                    self.board[self.x - 1][self.y - 1] = " " * (self.cell - 1) + "X"
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid position!")

    def display(self):
        print(" " * len(str(self.row)) + "-" * (self.col * (self.cell + 1) + 3))
        for i in range(self.row, 0, -1):
            print((" " * (len(str(self.row)) - len(str(i)))) + str(i) + "| " + " ".join(self.board[i - 1]) + " |")
        print(" " * len(str(self.row)) + "-" * (self.col * (self.cell + 1) + 3))
        temp = [" " * (self.cell - len(str(i))) + str(i) for i in range(1, self.col + 1)]
        print(" " * (len(str(self.row)) + 2) + " ".join(temp) + "  " + "\n")

    def game_status(self, x, y, board):
        if not any([1 if j == "_" * self.cell else 0 for i in board for j in i]):
            return "won"
        elif self.valid_move(x, y) == 0:
            return "lost"
        return "continue"

    def valid_move(self, x, y, option="count"):
        valid_move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, 2), (1, -2), (2, -1), (2, 1)]
        total_move, valid_moves = 0, {}
        for i in valid_move:
            if 1 <= x + i[0] <= self.row and 1 <= y + i[1] <= self.col \
                    and self.board[x + i[0] - 1][y + i[1] - 1] == "_" * self.cell:
                total_move += 1
                if option == "replace":
                    self.board[x + i[0] - 1][y + i[1] - 1] = " " * (self.cell - 1) \
                                                             + str(self.valid_move(x + i[0], y + i[1]))
                elif option == "rank":
                    valid_moves[(x + i[0], y + i[1])] = self.valid_move(x + i[0], y + i[1])
        return total_move if option == "count" else valid_moves

    def check_solution(self):
        self.solution, p, q = self.board, self.x, self.y  # Made aliases inorder to preserve initial values for manual.
        while True:
            if self.game_status(p, q, self.solution) == "continue":
                self.solution[p - 1][q - 1] = " " * (self.cell - len(str(self.count))) + str(self.count)
                rank_dic = sorted(self.valid_move(p, q, "rank").items(), key=lambda x: x[1])
                if len(rank_dic) > 1:
                    rank_dic = [i for i in rank_dic if i[1] > 0 and any([i[1] for i in rank_dic])]
                if self.count < self.row * self.col:
                    # print(p, q, self.count, rank_dic)
                    p, q = rank_dic[0][0]
                self.count += 1
            else:
                self.solution[p - 1][q - 1] = " " * (self.cell - len(str(self.count))) + str(self.count)
                return p, q

    def next_move(self):
        pos_moves = list(self.valid_move(self.x, self.y, "rank").keys())
        while True:
            try:
                self.y, self.x = [int(i) for i in input("Enter your next move: ").split()]
                if (self.x, self.y) in pos_moves:
                    self.board[self.x - 1][self.y - 1] = " " * (self.cell - 1) + "X"
                    self.valid_move(self.x, self.y, "replace")
                    break
                else:
                    raise Exception
            except (ValueError, Exception):
                print("Invalid move!", end=" ")

    def user(self):
        while True:
            self.valid_move(self.x, self.y, "replace")
            self.display()
            self.board[self.x - 1][self.y - 1] = " " * (self.cell - 1) + "*"
            for i in range(self.row):
                for j in range(self.col):
                    if self.board[i][j] != " " * (self.cell - 1) + "*":
                        self.board[i][j] = "_" * self.cell
            if self.game_status(self.x, self.y, self.board) == "continue":
                self.next_move()
            elif self.game_status(self.x, self.y, self.board) == "won":
                print("What a great tour! Congratulations!")
                break
            elif self.game_status(self.x, self.y, self.board) == "lost":
                print("No more possible moves!")
                print(f"Your knight visited {sum([1 for i in self.board for j in i if j != '_' * self.cell])} squares!")
                break

    def play(self):
        self.create_board()
        self.starting_position()
        p, q = self.check_solution()
        while True:
            mode = input("Do you want to try the puzzle? (y/n): ")
            if mode not in ["y", "n"]:
                print("Invalid input!")
                continue
            elif self.game_status(p, q, self.solution) == "lost":
                print("No solution exists!")
            elif mode == "y":
                self.board = [["_" * self.cell for _ in range(self.col)] for _ in range(self.row)]
                self.board[self.x - 1][self.y - 1] = " " * (self.cell - 1) + "X"
                self.user()
            else:
                self.board = self.solution
                print("\nHere's the solution!")
                self.display()
            break


knight_tour = KnightTourPuzzle()
knight_tour.play()
