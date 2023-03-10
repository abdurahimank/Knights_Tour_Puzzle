# Stage 3/6: Where to next?
class KnightTourPuzzle:
    def __init__(self):
        self.board = []
        self.row, self.col, self.cell_size = 0, 0, 0

    def display(self):
        print(" " * len(str(self.row)) + "-" * (self.col * (self.cell_size + 1) + 3))
        for i in range(self.row, 0, -1):
            print((" " * (len(str(self.row)) - len(str(i)))) + str(i) + "| " + " ".join(self.board[i - 1]) + " |")
        print(" " * len(str(self.row)) + "-" * (self.col * (self.cell_size + 1) + 3))
        temp = [" " * (self.cell_size - len(str(i))) + str(i) for i in range(1, self.col + 1)]
        print(" " * (len(str(self.row)) + 2) + " ".join(temp) + "  ")

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

    def valid_move(self, x, y):
        valid_move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, 2), (1, -2), (2, -1), (2, 1)]
        for i in valid_move:
            if 1 <= x + i[0] <= self.row and 1 <= y + i[1] <= self.col:
                self.board[x + i[0] - 1][y + i[1] - 1] = " " * (self.cell_size - 1) + "O"

    def start(self):
        self.create_board()
        while True:
            try:
                y, x = [int(i) for i in input("Enter the knight's starting position: ").split()]
                if 1 <= x <= self.row and 1 <= y <= self.col:
                    self.board[x - 1][y - 1] = " " * (self.cell_size - 1) + "X"
                    self.valid_move(x, y)
                    self.display()
                    break
                else:
                    print("Invalid position!")
            except ValueError:
                print("Invalid position!")


knight_tour = KnightTourPuzzle()
knight_tour.start()
