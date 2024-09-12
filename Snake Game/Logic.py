import random
import os
import time
import keyboard
from colorama import Fore, Style, init

# Initialize colorama
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board(size):
    return [[0 for _ in range(size[1])] for _ in range(size[0])]

def print_board(board, score):
    clear_screen()
    print(Fore.YELLOW + f"Score: {score}" + Style.RESET_ALL)  # Display score in yellow
    for row in board:
        for cell in row:
            if cell == 1:  # Apple
                print(Fore.RED + 'A', end=' ')
            elif cell == '*':  # Snake
                print(Fore.GREEN + '*', end=' ')
            else:
                print(Style.RESET_ALL + str(cell), end=' ')
        print(Style.RESET_ALL)
    print()

def place_apple(board, size):
    random_x = random.randint(0, size[1] - 1)
    random_y = random.randint(0, size[0] - 1)
    board[random_y][random_x] = 1
    return [random_y, random_x]

def move_snake(snake, direction, size):
    head = snake[0].copy()
    
    if direction == 'd':  # right
        head[1] += 1
    elif direction == 'a':  # left
        head[1] -= 1
    elif direction == 'w':  # up
        head[0] -= 1
    elif direction == 's':  # down
        head[0] += 1

    # Check for collision with the edges
    if head[0] < 0 or head[0] >= size[0] or head[1] < 0 or head[1] >= size[1]:
        return None  # Snake hit the edge, return None to indicate game over
    
    return head

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

def game_loop(size):
    snake = [[0, 0]]  # Snake starts at top-left corner
    board = create_board(size)
    apple_pos = place_apple(board, size)
    direction = 'd'
    running = True
    score = 0  # Initialize the score

    while running:
        # Handle keyboard input
        if keyboard.is_pressed('d'): direction = 'd'
        if keyboard.is_pressed('a'): direction = 'a'
        if keyboard.is_pressed('w'): direction = 'w'
        if keyboard.is_pressed('s'): direction = 's'

        # Move snake
        new_head = move_snake(snake, direction, size)
        
        if new_head is None:  # Snake hit the edge, game over
            game_over_screen()
            break
        
        # Check if snake ate the apple
        if new_head == apple_pos:
            snake.insert(0, new_head)  # Grow the snake
            apple_pos = place_apple(board, size)  # New apple
            score += 1  # Increment the score
        else:
            snake.insert(0, new_head)  # Move snake forward
            snake.pop()  # Remove the tail

        # Update board
        board = create_board(size)
        board[apple_pos[0]][apple_pos[1]] = 1  # Place apple
        for part in snake:
            board[part[0]][part[1]] = '*'  # Place snake

        # Print the board with the updated score
        print_board(board, score)

        # Delay to control speed
        time.sleep(0.1)

# Game setup
size = [int(x) for x in input("Choose a size for nxm matrix: ").split()]
game_loop(size)
