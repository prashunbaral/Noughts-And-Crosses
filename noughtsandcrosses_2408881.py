
#Prashun Baral
#2408881

""" 
noughtsandcrosses.py: A simple implementation of Noughts and Crosses (Tic-Tac-Toe) game.
"""

import random
import os.path
import json

random.seed()

def draw_board(board):
    """
    Draw the current state of the game board.
    
    Args:
        board (list): The 3x3 game board represented as a list of lists.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 13)

def welcome(board):
    """
    Display a welcome message and draw the initial game board.
    
    Args:
        board (list): The 3x3 game board represented as a list of lists.
    """
    print("Welcome to Unbeatable Noughts and Crosses!")
    draw_board(board)

def initialise_board(board):
    """
    Initialise the game board with empty spaces.
    
    Args:
        board (list): The 3x3 game board represented as a list of lists.
        
    Returns:
        list: The initialised game board.
    """
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

def get_player_move(board):
    """
    Get the player's move.
    
    Args:
        board (list): The 3x3 game board represented as a list of lists.
        
    Returns:
        tuple: The row and column indices of the player's move.
    """
    while True:
        move = input("Enter the number of the cell to put 'X' in (1-9): ")
        if move.isdigit():
            move = int(move)
            if 1 <= move <= 9:
                row, col = divmod(move - 1, 3)
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("Cell already occupied. Please choose another one.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        else:
            print("Invalid input. Please enter a number.")

def choose_computer_move(board):
    """
    Choose the computer's move.
    
    Args:
        board (list): The 3x3 game board represented as a list of lists.
        
    Returns:
        tuple: The row and column indices of the computer's move.
    """
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None

def check_for_win(board, mark):
    """
    Check if a player has won the game.
    
    Args:
        board (list): The 3x3 game board represented as a list of lists.
        mark (str): The mark ('X' or 'O') to check for a win.
        
    Returns:
        bool: True if the player with the given mark has won, False otherwise.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
        if board[0][0] == board[1][1] == board[2][2] == mark:
            return True
        if board[0][2] == board[1][1] == board[2][0] == mark:
            return True
    return False

def check_for_draw(board):
    """
    Check if the game is a draw.
    
    Args:
        board (list): The 3x3 game board represented as a list of lists.
        
    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def play_game(board):
    """
    Play the Noughts and Crosses game.
    
    Args:
        board (list): The 3x3 game board represented as a list of lists.
        
    Returns:
        int: The result of the game (-1 for computer win, 0 for draw, 1 for player win).
    """
    initialise_board(board)
    draw_board(board)
    player_mark = 'X'
    computer_mark = 'O'
    
    while True:
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = player_mark

        if check_for_win(board, player_mark):
            print("Congratulations! You win!")
            draw_board(board)
            return 1

        if check_for_draw(board):
            print("It's a draw!")
            return 0

        computer_row, computer_col = choose_computer_move(board)
        board[computer_row][computer_col] = computer_mark
        draw_board(board)

        if check_for_win(board, computer_mark):
            print("Computer wins! Better luck next time.")
            return -1

        if check_for_draw(board):
            print("It's a draw!")
            return 0

def menu():
    """
    Display the menu and get user's choice.
    
    Returns:
        str: The user's choice.
    """
    while True:
        print("Menu:")
        print("1 - Play the game")
        print("2 - Save score in file 'leaderboard.txt'")
        print("3 - Load and display the scores from 'leaderboard.txt'")
        print("q - End the program")
        choice = input("Enter your choice: ")
        if choice in ['1', '2', '3', 'q']:
            return choice
        else:
            print("Invalid choice. Please choose again.")

def load_scores():
    """
    Load scores from the 'leaderboard.txt' file.
    
    Returns:
        dict: A dictionary containing player names as keys and their scores as values.
    """
    file_path = 'leaderboard.txt'

    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                leaders = json.load(file)
        except json.JSONDecodeError:
            leaders = {}
    else:
        leaders = {}

    return leaders

def save_score(score):
    """
    Save the player's score in the 'leaderboard.txt' file.
    
    Args:
        score (int): The player's score.
    """
    player_name = input("Enter your name: ")
    leaders = load_scores()
    leaders[player_name] = score
    with open('leaderboard.txt', 'w') as file:
        json.dump(leaders, file)

def display_leaderboard(leaders):
    """
    Display the leaderboard.
    
    Args:
        leaders (dict): A dictionary containing player names as keys and their scores as values.
    """
    if not leaders:
        print("Leaderboard is empty.")
    else:
        print("Leaderboard:")
        for player, score in leaders.items():
            print(f"{player}: {score}")
