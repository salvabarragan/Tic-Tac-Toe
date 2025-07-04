from board import Board
from logic import Match
import os

game = Board()
game_over = False

while not game_over:
    while True:
        os.system('cls')
        print(game.show_board())
        if not game.player_x(input("X moves: ")):
            continue
        else:
            if game.check_result("X"):
                print(game.show_board())
                input("Player X wins!")
                game_over = True
                break
            break
    if game_over:
        break
    while True:
        print(game.show_board())
        if not game.player_o(input("O moves: ")):
            continue
        else:
            if game.check_result("O"):
                os.system('cls')
                print(game.show_board())
                input("Player O wins!")
                game_over = True
                break
            break
