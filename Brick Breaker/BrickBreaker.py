import random
import os
import time
import keyboard
from colorama import Fore, Style, init

# Initialize colorama
init()

# Constants
PADDLE_CHAR = Fore.GREEN + "=" + Style.RESET_ALL
BALL_CHAR = Fore.YELLOW + "O" + Style.RESET_ALL
BRICK_CHAR = Fore.RED + "#" + Style.RESET_ALL
EMPTY_CHAR = " "

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board(width, height, paddle_width):
    """Creates the initial board with bricks at the top."""
    board = [[EMPTY_CHAR for _ in range(width)] for _ in range(height)]

    # Add bricks (the top 3 rows)
    for i in range(3):
        for j in range(width):
            board[i][j] = BRICK_CHAR
    
    # Add paddle at the bottom
    paddle_start = (width - paddle_width) // 2
    for i in range(paddle_start, paddle_start + paddle_width):
        board[height - 1][i] = PADDLE_CHAR

    return board

def print_board(board, ball_pos, score):
    """Prints the game board with the current score."""
    clear_screen()
    print(f"Score: {score}")
    for row in range(len(board)):
        for col in range(len(board[row])):
            # Check if we're at the ball position
            if [row, col] == ball_pos:
                print(BALL_CHAR, end=' ')
            else:
                print(board[row][col], end=' ')
        print()
    print()

def move_paddle(board, direction, paddle_width, width):
    """Moves the paddle left or right."""
    bottom_row = len(board) - 1
    current_paddle_pos = [i for i, x in enumerate(board[bottom_row]) if x == PADDLE_CHAR]
    
    if direction == "left" and current_paddle_pos[0] > 0:
        new_paddle_pos = [pos - 1 for pos in current_paddle_pos]
    elif direction == "right" and current_paddle_pos[-1] < width - 1:
        new_paddle_pos = [pos + 1 for pos in current_paddle_pos]
    else:
        return  # Paddle is at the edge, no movement
    
    # Clear old paddle position entirely
    for pos in range(width):
        board[bottom_row][pos] = EMPTY_CHAR
    
    # Set new paddle position
    for pos in new_paddle_pos:
        board[bottom_row][pos] = PADDLE_CHAR

def move_ball(board, ball_pos, ball_dir, width, height):
    """Moves the ball according to its direction, handles collisions."""
    next_pos = [ball_pos[0] + ball_dir[0], ball_pos[1] + ball_dir[1]]

    # Check for collision with walls
    if next_pos[1] <= 0 or next_pos[1] >= width - 1:
        ball_dir[1] = -ball_dir[1]  # Bounce horizontally
    if next_pos[0] <= 0:
        ball_dir[0] = -ball_dir[0]  # Bounce vertically

    # Check for collision with the paddle
    if next_pos[0] == height - 1:
        paddle_pos = [i for i, x in enumerate(board[height - 1]) if x == PADDLE_CHAR]
        if next_pos[1] in paddle_pos:
            ball_dir[0] = -ball_dir[0]  # Bounce the ball upwards
        else:
            return "game_over"

    # Check for collision with bricks
    if board[next_pos[0]][next_pos[1]] == BRICK_CHAR:
        ball_dir[0] = -ball_dir[0]  # Bounce vertically
        board[next_pos[0]][next_pos[1]] = EMPTY_CHAR  # Remove the brick
        return "brick_hit"

    return next_pos

def game_over_screen():
    clear_screen()
    game_over_ascii = """
  _____                         ____                 
 / ____|                       / __ \                
| |  __  __ _ _ __ ___   ___   | |  | |_   _____ _ __ 
| | |_ |/ _` | '_ ` _ \ / _ \  | |  | \ \ / / _ \ '__|
| |__| | (_| | | | | | |  __/  | |__| |\ V /  __/ |   
 \_____|\__,_|_| |_| |_|\___|   \____/  \_/ \___|_|   
                                                     
    """
    print(Fore.RED + game_over_ascii + Style.RESET_ALL)
    time.sleep(3)

def game_loop(width, height, paddle_width):
    board = create_board(width, height, paddle_width)
    ball_pos = [height - 2, width // 2]  # Ball starts right above the paddle
    ball_dir = [-1, random.choice([-1, 1])]  # Ball starts moving diagonally
    score = 0
    running = True

    while running:
        # Handle paddle movement
        if keyboard.is_pressed('a'):
            move_paddle(board, "left", paddle_width, width)
        if keyboard.is_pressed('d'):
            move_paddle(board, "right", paddle_width, width)

        # Move the ball
        result = move_ball(board, ball_pos, ball_dir, width, height)
        
        if result == "game_over":
            game_over_screen()
            break
        elif result == "brick_hit":
            score += 1
        else:
            ball_pos = result

        # Print the updated board, keeping the ball visible without overwriting the paddle
        print_board(board, ball_pos, score)

        # Delay to control speed
        time.sleep(0.1)

# Game setup
width = 20  # Width of the board
height = 15  # Height of the board
paddle_width = 5  # Paddle size
game_loop(width, height, paddle_width)
