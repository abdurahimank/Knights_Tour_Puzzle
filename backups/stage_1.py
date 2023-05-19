# Project: Knight's Tour Puzzle
# Stage 1/6: Setting up the board
class KnightTour:
    def __init__(self):
        self.row, self.col, self.x, self.y = 8, 8, 0, 0
        self.board = [["_" for _ in range(self.col)] for _ in range(self.row)]

    def display(self):
        print(" " + "-" * (self.row * 2 + 3))
        for i in range(8, 0, -1):
            print(f"{i}|", *self.board[i - 1], "|")
        print(" " + "-" * (self.row * 2 + 3))
        print("   1 2 3 4 5 6 7 8")

    def play(self):
        while True:
            try:
                self.y, self.x = input("Enter the knight's starting position: ").split()
                if self.x.isdigit() and self.y.isdigit() and 1 <= int(self.x) <= 8 and 1 <= int(self.y) <= 8:
                    self.board[int(self.x) - 1][int(self.y) - 1] = "X"
                    self.display()
                    break
                raise ValueError
            except ValueError:
                print("Invalid dimensions!")


game = KnightTour()
game.play()
