import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        if current_player == "O":
            print("Player", current_player, "turn")
            playrow = random.randint(0,2)
            print(f"Player 'O' rowplay is: {playrow}")
            row = playrow
            playcol = random.randint(0, 2)
            print(f"Player 'O' colplay is: {playcol}")
            col = playcol
        else:
            print("Player", current_player, "turn")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                print("Player", current_player, "wins!")
                game_over = True
            elif all(board[row][col] != " " for row in range(3) for col in range(3)):
                print("It's a tie!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")


play_game()