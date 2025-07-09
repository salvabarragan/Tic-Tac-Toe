class Match:
    winning_patterns = [[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8],
                    [0, 3, 6],
                    [1, 4, 7],
                    [2, 5, 8],
                    [0, 4, 8],
                    [2, 4, 6]]
    
    def __init__(self):
       self.moves = [" ", " ", " ",
                     " ", " ", " ",
                     " ", " ", " "]
    
    def player_x(self, move):
        try:
            if self.moves[int(move) - 1] == " " and int(move) < 10:
                self.moves[int(move) - 1] = "X"
                return True
            else:
                return False
        except IndexError:
            return False
    
    def player_o(self, move):
        try:
            if self.moves[int(move) - 1] == " " and int(move) < 10:
                self.moves[int(move) - 1] = "O"
                return True
            else:
                return False
        except IndexError:
            return False
    
    def check_result(self, player):
        if self.moves.count(" ") <= 4:
            for i in self.winning_patterns:
                if self.moves[i[0]] == player and self.moves[i[1]] == player and self.moves[i[2]] == player:
                    return 1
            if self.moves.count(" ") == 0:
                return 2
            