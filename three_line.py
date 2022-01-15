"""
File: three_line.py.py
Author: Tyrone Garcia

Purpose: Tic-Tac-Toe game 
"""


def main():
    # Text color definition
    win_color = '\033[32;22m'
    dead_heat_color = '\033[1;33m'
    normal_color = '\u001b[39;22m'
    # Variable definition
    grid = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
    game_position = ""
    player_turn = "X"
    
    # Repeat it until user write 0, one gamer win or nobody win the game
    while game_position != "0":
        print("\nWelcome to Three in Line Game \n")
        print_grid(grid)
        print("\nInput 0 to Exit or 1-9 to play...")
        game_position = input(f" {player_turn}'s turn to choose a square (1-9): ")
        # Validate if the block is empty and later check if are the a winner
        validate_move(grid, game_position, player_turn)
        if win_verify(grid) == 1:
            game_position = "0"
            print(f"{win_color} Player {player_turn} win!!!! {normal_color} ")
        else:
            print_grid(grid)
            if is_empty(grid) == 0:
                game_position = "0"
                print(f"{dead_heat_color} It is a Dead Heat!!! {normal_color} ")
            else:
                if player_turn.upper() == "X":
                    player_turn = "0"
                else:
                    player_turn = "X"


    print()
    print_grid(grid)
    print("End of game!!!")
    
# Print the grid or game workspace
def print_grid(grid_1):
    normal_color = '\u001b[39;22m'
    cell_color = ""
    for i in range(len(grid_1)):
        print('[', end="")
        for j in range(len(grid_1[i])):
            if grid_1[i][j] == "X":
                cell_color = '\033[1;32m' 
            elif grid_1[i][j] == "0":
                cell_color = '\033[1;33m' 
            else:
                cell_color = '\u001b[39;22m' 
            print(f"{cell_color} {grid_1[i][j]:>3} {normal_color} ", end="")
        print("]")


# Check if a gamer won the game
def win_verify(grid_1):
    win = 0
    #Row Verification
    #It could be done with for loops
    if (grid_1[0][0] == grid_1[0][1] == grid_1[0][2]) or (grid_1[1][0] == grid_1[1][1] == grid_1[1][2]) or (grid_1[2][0] == grid_1[2][1] == grid_1[2][2]):
        win = 1
    # Col Verification
    if (grid_1[0][0] == grid_1[1][0] == grid_1[2][0]) or (grid_1[0][1] == grid_1[1][1] == grid_1[2][1]) or (grid_1[0][2] == grid_1[1][2] == grid_1[2][2]):
        win = 1

    # Diagonal verification
    # First diagonal
    if grid_1[0][0] == grid_1[1][1] == grid_1[2][2]:
        win = 1
    # Second diagonal    
    if grid_1[2][0] == grid_1[1][1] == grid_1[0][2]:
        win = 1
    return win

# Check if the block or space is empty or not used by the other gamer
# and put the gamer value in it
def validate_move(grid_1, value, player):
    #print(f" {type(value)} {type(player)}")
    for i in range(len(grid_1)):
        for j in range(len(grid_1[i])):
            if grid_1[i][j] == value:
                grid_1[i][j] = player
                break
                #print("Replace number")
            #else:
                #print("It is full")

# Check if are there another empty block or cell to 
# play
def is_empty(grid_1):
    empty_cell = 0
    cell_value = ""
    for i in range(len(grid_1)):
        for j in range(len(grid_1[i])):
            cell_value = grid_1[i][j]
            if cell_value.isnumeric():
                if int(cell_value) > 0:
                    empty_cell = 1
    return  empty_cell



if __name__ == "__main__":
    main()
