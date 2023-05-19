# Project: Knight's Tour Puzzle
# Stage 3/6: Where to next?
class KnightTour:
    def __init__(self):
        self.row, self.col, self.x, self.y, self.cell_size, self.board = 0, 0, 0, 0, 0, []

    def create_board(self):
        while True:
            try:
                self.col, self.row = input("Enter your board dimensions: ").split()
                if self.row.isdigit() and self.col.isdigit() and 0 < int(self.row) and 0 < int(self.col):
                    self.row, self.col = int(self.row), int(self.col)
                    self.cell_size = len(str(self.row * self.col))
                    self.board = [["_" * self.cell_size for _ in range(self.col)] for _ in range(self.row)]
                    break
                raise ValueError
            except ValueError:
                print("Invalid dimensions!")

    def starting_position(self):
        while True:
            try:
                self.y, self.x = input("Enter the knight's starting position: ").split()
                if self.x.isdigit() and self.y.isdigit() and 1 <= int(self.x) <= self.row \
                        and 1 <= int(self.y) <= self.col:
                    self.x, self.y = int(self.x), int(self.y)
                    self.board[self.x - 1][self.y - 1] = (" " * (self.cell_size - 1)) + "X"
                    break
                raise ValueError
            except ValueError:
                print("Invalid position!")

    def display(self):
        print((" " * len(str(self.row))) + "-" * ((self.col * (self.cell_size + 1)) + 3))
        for i in range(self.row, 0, -1):
            print(" " * (len(str(self.row)) - 1) + f"{i}|", *self.board[i - 1], "|")
        print((" " * len(str(self.row))) + "-" * ((self.col * (self.cell_size + 1)) + 3))
        temp = [" " * (self.cell_size - len(str(i))) + str(i) for i in range(1, self.col + 1)]
        print(" " * (len(str(self.row)) + 2) + " ".join(temp) + "  " + "\n")

    def valid_position(self):
        val_pos = [(i, j) for i in [-2, -1, 1, 2] for j in [-2, -1, 1, 2] if abs(i) != abs(j)]
        for i in val_pos:
            if 1 <= self.x + i[0] <= self.row and 1 <= self.y + i[1] <= self.col:
                self.board[self.x + i[0] - 1][self.y + i[1] - 1] = (" " * (self.cell_size - 1)) + "O"

    def play(self):
        self.create_board()
        self.starting_position()
        self.valid_position()
        print("\nHere are the possible moves:")
        self.display()


game = KnightTour()
game.play()
