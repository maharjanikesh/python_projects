# Tic-Tac-Toe game in Python

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the board is full (i.e., a draw)
def check_draw(board):
    return all([spot != " " for row in board for spot in row])

# Function to play Tic-Tac-Toe
def play_tic_tac_toe():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get the player's move
        try:
            row = int(input("Enter row (1, 2, 3): ")) - 1
            col = int(input("Enter column (1, 2, 3): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue
        
        # Check if the move is valid
        if row not in range(3) or col not in range(3) or board[row][col] != " ":
            print("Invalid move. Please try again.")
            continue
        
        # Place the player's move on the board
        board[row][col] = current_player
        
        # Check if the current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the game is a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_tic_tac_toe()
