import string


class Knight:
    def __init__(self):
        self.x = ''
        self.y = ''
        self.digits = []

    def valid(self):
        for i in string.digits:
            self.digits.append(i)
        if self.x not in self.digits or self.y not in self.digits:
            return False
        if 1 <= int(self.x) <= 8 and 1 <= int(self.y) <= 8:
            return True
        else:
            return False

    def board(self):
        pl = {(i, j): '_' for i in range(1, 9) for j in range(1, 9)}
        pl[(int(self.x), int(self.y))] = "X"
        board = f"""
 -------------------
8| {pl[(1, 8)]} {pl[(2, 8)]} {pl[(3, 8)]} {pl[(4, 8)]} {pl[(5, 8)]} {pl[(6, 8)]} {pl[(7, 8)]} {pl[(8, 8)]} |
7| {pl[(1, 7)]} {pl[(2, 7)]} {pl[(3, 7)]} {pl[(4, 7)]} {pl[(5, 7)]} {pl[(6, 7)]} {pl[(7, 7)]} {pl[(8, 7)]} |
6| {pl[(1, 6)]} {pl[(2, 6)]} {pl[(3, 6)]} {pl[(4, 6)]} {pl[(5, 6)]} {pl[(6, 6)]} {pl[(7, 6)]} {pl[(8, 6)]} |
5| {pl[(1, 5)]} {pl[(2, 5)]} {pl[(3, 5)]} {pl[(4, 5)]} {pl[(5, 5)]} {pl[(6, 5)]} {pl[(7, 5)]} {pl[(8, 5)]} |
4| {pl[(1, 4)]} {pl[(2, 4)]} {pl[(3, 4)]} {pl[(4, 4)]} {pl[(5, 4)]} {pl[(6, 4)]} {pl[(7, 4)]} {pl[(8, 4)]} |
3| {pl[(1, 3)]} {pl[(2, 3)]} {pl[(3, 3)]} {pl[(4, 3)]} {pl[(5, 3)]} {pl[(6, 3)]} {pl[(7, 3)]} {pl[(8, 3)]} |
2| {pl[(1, 2)]} {pl[(2, 2)]} {pl[(3, 2)]} {pl[(4, 2)]} {pl[(5, 2)]} {pl[(6, 2)]} {pl[(7, 2)]} {pl[(8, 2)]} |
1| {pl[(1, 1)]} {pl[(2, 1)]} {pl[(3, 1)]} {pl[(4, 1)]} {pl[(5, 1)]} {pl[(6, 1)]} {pl[(7, 1)]} {pl[(8, 1)]} |
 -------------------
   1 2 3 4 5 6 7 8 
"""
        print(board)

    def play(self):
        while True:
            try:
                self.x, self.y = input("Enter the knight's starting position: ").split()
            except ValueError:
                print("Invalid dimensions!")
                break
            if self.valid():
                self.board()
            else:
                print("Invalid dimensions!")
            break


knight = Knight()
knight.play()
