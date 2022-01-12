"""
File: three_line.py.py
Author: Tyrone Garcia

Purpose: Tic-Tac-Toe game 
"""


def main():
    grid = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
    player_options = ["0","1","2","3","4","5","6","7","8","9"]
    end_game = 0
    game_position = "x"
    player_turn = "X"
    print_grid(grid)
    while game_position != "0":
        game_position = input(f" {player_turn}'s turn to choose a square (1-9): ")
        is_empty(grid, game_position, player_turn)
        if win_verify(grid) == 1:
            game_position = "0"
            print(f"Player {player_turn} win!!!!")
        print_grid(grid)
        if player_turn.upper() == "X":
            player_turn = "0"
        else:
            player_turn = "X"


    print()
    print_grid(grid)
    





def print_grid(grid_1):
    for i in range(len(grid_1)):
        print('[', end="")
        for j in range(len(grid_1[i])):
            print(f"{grid_1[i][j]:>3}", end="")
        print("]")



def win_verify(grid_1):
    win = 0
    #Row Verification
    if (grid_1[0][0] == grid_1[0][1] == grid_1[0][2]) or (grid_1[1][0] == grid_1[1][1] == grid_1[1][2]) or (grid_1[2][0] == grid_1[2][1] == grid_1[2][2]):
        win = 1
    # Col Verification
    if (grid_1[0][0] == grid_1[1][0] == grid_1[2][0]) or (grid_1[0][1] == grid_1[1][1] == grid_1[2][1]) or (grid_1[0][2] == grid_1[1][2] == grid_1[2][2]):
        win = 1

    # Diagonal verification
    if grid_1[0][0] == grid_1[1][1] == grid_1[2][2]:
        win = 1
    if grid_1[2][0] == grid_1[1][1] == grid_1[0][2]:
        win = 1
    return win


def is_empty(grid_1, value, player):
    print(f" {type(value)} {type(player)}")
    for i in range(len(grid_1)):
        for j in range(len(grid_1[i])):
            if grid_1[i][j] == value:
                grid_1[i][j] = player
                break

                #print("Replace number")
            #else:
                #print("It is full")




if __name__ == "__main__":
    main()
