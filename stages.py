# Stage 5/6: How far will your knight go?
class KnightTourPuzzle:
    def __init__(self):
        self.board, self.valid_moves = [], []
        self.x, self.y, self.row, self.col, self.cell_size, self.visited = 0, 0, 0, 0, 0, 0

    def display(self):
        print(" " * len(str(self.row)) + "-" * (self.col * (self.cell_size + 1) + 3))
        for i in range(self.row, 0, -1):
            print((" " * (len(str(self.row)) - len(str(i)))) + str(i) + "| " + " ".join(self.board[i - 1]) + " |")
        print(" " * len(str(self.row)) + "-" * (self.col * (self.cell_size + 1) + 3))
        temp = [" " * (self.cell_size - len(str(i))) + str(i) for i in range(1, self.col + 1)]
        print(" " * (len(str(self.row)) + 2) + " ".join(temp) + "  " + "\n")

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

    def start_game(self):
        while True:
            try:
                self.y, self.x = [int(i) for i in input("Enter the knight's starting position: ").split()]
                if 1 <= self.x <= self.row and 1 <= self.y <= self.col:
                    self.board[self.x - 1][self.y - 1] = " " * (self.cell_size - 1) + "X"
                    break
                else:
                    print("Invalid position!")
            except ValueError:
                print("Invalid position!")

    def game_status(self):
        if self.visited == self.row * self.col:
            return "won"
        elif self.valid_move(self.x, self.y) == 0:
            return "lost"
        return "continue"

    def valid_move(self, x, y, option="count"):
        valid_move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, 2), (1, -2), (2, -1), (2, 1)]
        total_move = 0
        self.valid_moves = []
        for i in valid_move:
            if 1 <= x + i[0] <= self.row and 1 <= y + i[1] <= self.col \
                    and self.board[x + i[0] - 1][y + i[1] - 1] == "_" * self.cell_size:
                total_move += 1
                self.valid_moves.append((x + i[0], y + i[1]))
                if option == "replace":
                    self.board[x + i[0] - 1][y + i[1] - 1] = " " * (self.cell_size - 1) \
                                                             + str(self.valid_move(x + i[0], y + i[1]))
        return total_move

    def next_move(self):
        while True:
            try:
                self.y, self.x = [int(i) for i in input("Enter your next move: ").split()]
                if 1 <= self.x <= self.row and 1 <= self.y <= self.col and self.board[self.x - 1][self.y - 1] \
                        not in [" " * (self.cell_size - 1) + "*", " " * (self.cell_size - 1) + "X"] \
                        and (self.x, self. y) in self.valid_moves:
                    self.board[self.x - 1][self.y - 1] = " " * (self.cell_size - 1) + "X"
                    self.valid_move(self.x, self.y, "replace")
                    break
                else:
                    print("Invalid move!")
            except ValueError:
                print("Invalid move!")

    def play(self):
        self.create_board()
        self.start_game()
        while True:
            self.valid_move(self.x, self.y, "replace")
            self.display()
            self.board[self.x - 1][self.y - 1] = " " * (self.cell_size - 1) + "*"
            for i in range(self.row):
                for j in range(self.col):
                    if self.board[i][j] != " " * (self.cell_size - 1) + "*":
                        self.board[i][j] = "_" * self.cell_size

            self.visited = sum([0 if j == "_" * self.cell_size else 1 for i in self.board for j in i])
            if self.game_status() == "continue":
                self.next_move()
            elif self.game_status() == "won":
                print("What a great tour! Congratulations!")
                break
            elif self.game_status() == "lost":
                print("No more possible moves!")
                print(f"Your knight visited {self.visited} squares!")
                break


knight_tour = KnightTourPuzzle()
knight_tour.play()
