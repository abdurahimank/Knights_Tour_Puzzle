class KnightsTour:
    def __init__(self):
        self.col = ''
        self.row = ''
        self.x = ''
        self.y = ''
        self.digits = []
        self.board = ''  # board including side numbers and cells
        self.pl = {}  # dictionary of cells
        self.cell_len = 0  # length of each cell

    def pos_move(self, x, y, space_len, value):
        tot_pos = [(x + i, y + j) for i in [-2, -1, 1, 2] for j in [-2, -1, 1, 2] if abs(i) != abs(j)]
        pos = [i for i in tot_pos if 1 <= i[0] <= int(self.col) and 1 <= i[1] <= int(self.row)]
        pos = [i for i in pos if self.pl[i] == "_" * space_len]
        if value:  # used to return number of possible moves
            # pos = [i for i in pos if self.pl[i] == "_" * space_len]
            return pos
        else:  # used to show number of possible moves in board
            for item in pos:
                self.pl[item] = " " * (space_len - 1) + f"{len(self.pos_move(item[0], item[1], space_len, True))}"

    def valid(self, cat):
        if cat == 'dimension':
            return False if not self.col.isdigit() or not self.row.isdigit() or \
                            int(self.col) == 0 or int(self.row) == 0 else True
        else:
            if not self.x.isdigit() or not self.y.isdigit():
                return False
            if cat == "move":
                if self.pl[(int(self.x), int(self.y))] != '_' * self.cell_len:
                    return False
                for item in self.pl:
                    if self.pl[item] == " " * (self.cell_len - 1) + "X":
                        if (int(self.x), int(self.y)) not in self.pos_move(item[0], item[1], self.cell_len, True):
                            # print((int(self.x), int(self.y)))  # for testing
                            # print(self.pos_move(item[0], item[1], self.cell_len, True))  # for testing
                            return False
            return True if 1 <= int(self.x) <= int(self.col) and 1 <= int(self.y) <= int(self.row) else False

    def update_board(self, up_type):
        if up_type == "with_all_moves":
            for item in self.pl:
                if self.pl[item] == " " * (self.cell_len - 1) + "X":
                    self.pl[item] = " " * (self.cell_len - 1) + "*"
            self.pl[(int(self.x), int(self.y))] = " " * (self.cell_len - 1) + "X"
            self.pos_move(int(self.x), int(self.y), self.cell_len, False)
        else:
            for item in self.pl:
                if self.pl[item] != " " * (self.cell_len - 1) + "*" \
                        and self.pl[item] != " " * (self.cell_len - 1) + "X":
                    self.pl[item] = '_' * self.cell_len

    def show_board(self):
        self.update_board("with_all_moves")
        self.board = ''
        for i in range(int(self.row) + 3):
            if i == 0 or i == int(self.row) + 1:
                self.board += ' ' * len(self.row) + '-' * (int(self.col) * (self.cell_len + 1) + 3) + '\n'
            elif i == int(self.row) + 2:
                centre = ''.join(f'{" " * (self.cell_len - len(str(k)) + 1)}{str(k)}'
                                 for k in range(1, int(self.col) + 1))
                self.board += ' ' * (len(self.row) + 1) + centre + '  \n'
            else:
                centre = ''.join(f' {self.pl[(m, int(self.row) + 1 - i)]}' for m in range(1, int(self.col) + 1))
                first = ' ' * (len(self.row) - len(str(int(self.row) + 1 - i)))
                self.board += first + f'{int(self.row) + 1 - i}|' + centre + ' |' + '\n'
        print(self.board)
        self.update_board("clearing")

    def knight_move(self):
        while True:
            try:
                self.x, self.y = input("Enter the knight's starting position: ").split()
            except ValueError:
                print("Invalid position!")
                continue
            if self.valid("start_position"):
                self.show_board()
                break
            else:
                print("Invalid position!")
                continue
        while True:
            try:
                self.x, self.y = input("Enter your next move: ").split()
            except ValueError:
                print("Invalid move!")
                continue
            if self.valid("move"):
                if len(self.pos_move(int(self.x), int(self.y), self.cell_len, True)) > 0:
                    self.show_board()
                    continue
                else:
                    self.show_board()
                    if len([i for i in self.pl if self.pl[i] == '_' * self.cell_len]) == 0:
                        print("What a great tour! Congratulations!")
                        break
                    print("No more possible moves!")
                    tot_move = len(self.pl) - len([i for i in self.pl if self.pl[i] == '_' * self.cell_len])
                    print(f"Your knight visited {tot_move} squares!")
                    break
            else:
                print("Invalid move!")
                continue

    def play(self):
        while True:
            try:
                self.col, self.row = input("Enter your board dimensions: ").split()
            except ValueError:
                print("Invalid dimensions!")
                continue
            if self.valid("dimension"):
                self.cell_len = len(str(int(self.col) * int(self.row)))
                # Initially all cells have "_" value in length of variable self.cell_len.
                self.pl = {(i, j): '_' * self.cell_len for i in range(1, int(self.col) + 1)
                           for j in range(1, int(self.row) + 1)}
                self.knight_move()
                break
            else:
                print("Invalid dimensions!")
                continue


knight = KnightsTour()
knight.play()
