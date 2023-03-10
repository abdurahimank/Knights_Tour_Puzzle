# Stage 1/6: Setting up the board
class KnightTourPuzzle:
    def __init__(self):
        self.x = [["_" for _ in range(8)] for _ in range(8)]

    def display(self):
        print(f""" -------------------
8| {self.x[7][0]} {self.x[7][1]} {self.x[7][2]} {self.x[7][3]} {self.x[7][4]} {self.x[7][5]} {self.x[7][6]} {self.x[7][7]} |
7| {self.x[6][0]} {self.x[6][1]} {self.x[6][2]} {self.x[6][3]} {self.x[6][4]} {self.x[6][5]} {self.x[6][6]} {self.x[6][7]} |
6| {self.x[5][0]} {self.x[5][1]} {self.x[5][2]} {self.x[5][3]} {self.x[5][4]} {self.x[5][5]} {self.x[5][6]} {self.x[5][7]} |
5| {self.x[4][0]} {self.x[4][1]} {self.x[4][2]} {self.x[4][3]} {self.x[4][4]} {self.x[4][5]} {self.x[4][6]} {self.x[4][7]} |
4| {self.x[3][0]} {self.x[3][1]} {self.x[3][2]} {self.x[3][3]} {self.x[3][4]} {self.x[3][5]} {self.x[3][6]} {self.x[3][7]} |
3| {self.x[2][0]} {self.x[2][1]} {self.x[2][2]} {self.x[2][3]} {self.x[2][4]} {self.x[2][5]} {self.x[2][6]} {self.x[2][7]} |
2| {self.x[1][0]} {self.x[1][1]} {self.x[1][2]} {self.x[1][3]} {self.x[1][4]} {self.x[1][5]} {self.x[1][6]} {self.x[1][7]} |
1| {self.x[0][0]} {self.x[0][1]} {self.x[0][2]} {self.x[0][3]} {self.x[0][4]} {self.x[0][5]} {self.x[0][6]} {self.x[0][7]} |
 -------------------
   1 2 3 4 5 6 7 8 """)

    def start(self):
        try:
            y, x = [int(i) for i in input("Enter the knight's starting position: ").split()]
            if 1 <= x <= 8 and 1 <= y <= 8:
                self.x[x - 1][y - 1] = "X"
                self.display()
            else:
                print("Invalid dimensions!")
        except ValueError:
            print("Invalid dimensions!")


knight_tour = KnightTourPuzzle()
knight_tour.start()
