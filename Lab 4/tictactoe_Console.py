def print_board(board):
    print("\n")
    for i in range(3):
        row = " | ".join(board[i*3:(i+1)*3])
        print(row)
        if i < 2:
            print("--+---+--")
    print("\n")

def check_winner(board, player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False

def main():
    board = [" "]*9
    current_player = "X"
    moves = 0

    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue

        board[move] = current_player
        moves += 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif moves == 9:
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()