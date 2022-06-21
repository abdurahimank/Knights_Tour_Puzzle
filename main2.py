class KnightsTour:
    def __init__(self):
        self.board, self.point_table, self.row, self.column, self.x, self.y = [], {}, 0, 0, 0, 0
        self.cell_length, self.count = 0, 1

    def display(self):
        len_1 = len(str(self.row * self.column))
        print(" " * len(str(self.row)), "-" * (self.column * (len_1 + 1) + 3), sep="")
        for i in range(self.row, 0, -1):
            len_2 = len(str(self.row)) - len(str(i))
            print(f"{' ' * len_2}{i}|", *self.board[i - 1], '|')
        print(" " * len(str(self.row)), "-" * (self.column * (len_1 + 1) + 3), sep="")
        print(" " * (len(str(self.row)) + 1), *[f"{' ' * (len_1 - len(str(i)))}{i}" for i in range(1, self.column + 1)],
              ' ', '\n')

    def create_board(self):
        while True:
            try:
                self.column, self.row = [int(i) for i in input("Enter your board dimensions: ").split() if i.isdigit()]
                if self.row <= 0 or self.column <= 0:
                    raise Exception
            except (ValueError, Exception):
                print("Invalid dimensions!")
            else:
                self.cell_length = len(str(self.row * self.column))
                self.board = [["_" * self.cell_length for _ in range(self.column)] for _ in range(self.row)]
                break

    def start_position(self):
        while True:
            try:
                self.y, self.x = [int(i) for i in input("Enter the knight's starting position: ").split()]
                if self.x < 1 or self.x > self.row or self.y < 1 or self.y > self.column:
                    raise Exception
            except (ValueError, Exception):
                print("Invalid dimensions!")
            else:
                self.board[self.x - 1][self.y - 1] = ' ' * (self.cell_length - 1) + 'X'
                break

    def update_board(self, valid_moves,  to_use="automatic"):
        if to_use == "automatic":
            self.board[self.x - 1][self.y - 1] = ' ' * (self.cell_length - len(str(self.count))) + str(self.count)
            self.count += 1
        else:
            self.board[self.x - 1][self.y - 1] = ' ' * (self.cell_length - 1) + '*'
        for i in valid_moves:
            self.board[i[0] - 1][i[1] - 1] = "_" * self.cell_length

    def valid_move(self, row, column, to_use="change"):
        tot_moves = [(row + i, column + j) for i in [-2, -1, 1, 2] for j in [-2, -1, 1, 2] if abs(i) != abs(j)]
        valid_moves = {i: 0 for i in tot_moves if 1 <= i[0] <= self.row and 1 <= i[1] <= self.column
                       and self.board[i[0] - 1][i[1] - 1] == "_" * self.cell_length}
        if to_use == "change":
            for i in valid_moves:
                tot_moves_2 = self.valid_move(i[0], i[1], "count")
                self.board[i[0] - 1][i[1] - 1] = ' ' * (self.cell_length - 1) + str(tot_moves_2)
                valid_moves[i] = tot_moves_2
        if to_use == "count":
            return len(valid_moves)
        return valid_moves

    def next_move(self, valid):
        self.update_board(valid, "manual")
        while True:
            try:
                self.y, self.x = [int(i) for i in input("Enter your next move: ").split()]
                if self.x < 1 or self.x > self.row or self.y < 1 or self.y > self.column:
                    raise Exception
            except (ValueError, Exception):
                print("Invalid dimensions!")
            else:
                if not self.board[self.x - 1][self.y - 1] == '_' * self.cell_length or (self.x, self.y) not in valid:
                    print("Invalid move! ", end='')
                    continue
                self.board[self.x - 1][self.y - 1] = ' ' * (self.cell_length - 1) + 'X'
                break

    def knight_tour(self, to_use="automatic"):
        if to_use == "automatic":
            while self.valid_move(self.x, self.y, "count") > 0:
                possible_moves = self.valid_move(self.x, self.y)
                self.update_board(list(possible_moves.keys()), "automatic")
                self.x, self.y = min(possible_moves, key=possible_moves.get)
        else:
            if self.row >= 5 and self.column >= 5:
                return True
            else:
                self.knight_tour()
                self.update_board([])
                if self.count > self.row * self.column:
                    return True

    def play(self):
        self.create_board()
        self.start_position()
        while True:
            mode = input("Do you want to try the puzzle? (y/n): ")
            if mode == "y":
                x, y = self.x, self.y
                if self.knight_tour("check_solution"):
                    self.x, self.y = x, y
                    self.board = [["_" * self.cell_length for _ in range(self.column)] for _ in range(self.row)]
                    self.board[x - 1][y - 1] = ' ' * (self.cell_length - 1) + 'X'
                    while self.valid_move(self.x, self.y, "count") > 0:
                        possible_moves = self.valid_move(self.x, self.y)
                        self.display()
                        self.next_move(list(possible_moves.keys()))
                    cells = [j for i in self.board for j in i]
                    self.display()
                    if "_" * self.cell_length not in cells:
                        print("What a great tour! Congratulations!")
                    else:
                        print("No more possible moves!")
                        print(f"Your knight visited {len(cells) - cells.count('_' * self.cell_length)} squares!")
                else:
                    print("No solution exists!")
            elif mode == 'n':
                self.knight_tour()
                self.update_board([])
                cells = [j for i in self.board for j in i]
                if "_" * self.cell_length not in cells:
                    print("\nHere's the solution!")
                    self.display()
                else:
                    print("No solution exists!")
            else:
                print("Invalid input!")
                continue
            break


game_1 = KnightsTour()
game_1.play()
