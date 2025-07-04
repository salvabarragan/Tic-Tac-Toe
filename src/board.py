from logic import Match
import os


class Board(Match):
    def __init__(self):
        super().__init__()
        
    def show_board(self):
        os.system('cls')
        return f""" {self.moves[0]} | {self.moves[1]} | {self.moves[2]} 
-----------
 {self.moves[3]} | {self.moves[4]} | {self.moves[5]} 
-----------
 {self.moves[6]} | {self.moves[7]} | {self.moves[8]} """
            