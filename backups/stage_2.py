# Project: Knight's Tour Puzzle
# Stage 2/6: And now for something completely different!
class KnightTour:
    def __init__(self):
        self.row, self.col, self.x, self.y, self.cell_size, self.board = 0, 0, 0, 0, 0, []

    def create_board(self):
        while True:
            try:
                self.col, self.row = input("Enter your board dimensions: ").split()
                if self.row.isdigit() and self.col.isdigit() and 0 < int(self.row) and 1 < int(self.col):
                    self.row, self.col = int(self.row), int(self.col)
                    self.cell_size = len(str(self.row * self.col))
                    self.board = [["_" * self.cell_size for _ in range(self.col)] for _ in range(self.row)]
                    break
                raise ValueError
            except ValueError:
                print("Invalid dimensions!")

    def display(self):
        print((" " * len(str(self.row))) + "-" * ((self.col * (self.cell_size + 1)) + 3))
        for i in range(self.row, 0, -1):
            print(" " * (len(str(self.row)) - 1) + f"{i}|", *self.board[i - 1], "|")
        print((" " * len(str(self.row))) + "-" * ((self.col * (self.cell_size + 1)) + 3))
        temp = [" " * (self.cell_size - len(str(i))) + str(i) for i in range(1, self.col + 1)]
        print(" " * (len(str(self.row)) + 2) + " ".join(temp) + "  " + "\n")

    def starting_position(self):
        while True:
            try:
                self.y, self.x = input("Enter the knight's starting position: ").split()
                if self.x.isdigit() and self.y.isdigit() and 1 <= int(self.x) <= self.row \
                        and 1 <= int(self.y) <= self.col:
                    self.board[int(self.x) - 1][int(self.y) - 1] = (" " * (self.cell_size - 1)) + "X"
                    break
                raise ValueError
            except ValueError:
                print("Invalid position!")

    def play(self):
        self.create_board()
        self.starting_position()
        self.display()


game = KnightTour()
game.play()
