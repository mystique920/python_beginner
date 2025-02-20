import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game settings
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Auto-Controlled Snake")

clock = pygame.time.Clock()

# Initialize snake and food
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

def draw_rect(color, pos):
    rect = pygame.Rect(pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

def spawn_food():
    # Ensure that food does not appear on the snake
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake:
            return pos

def get_possible_moves(head):
    # Define moves with their (x, y) deltas
    moves = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0)
    }
    possible = {}
    for move, delta in moves.items():
        new_head = (head[0] + delta[0], head[1] + delta[1])
        # Check boundaries (walls)
        if new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
            continue
        # Check collision with itself
        if new_head in snake:
            continue
        possible[move] = delta
    return possible

def choose_direction(snake, food):
    head = snake[0]
    possible = get_possible_moves(head)
    if not possible:
        return None  # No safe moves; game over.
    
    # Use Manhattan distance heuristic to choose the move that brings the snake closer to the food.
    best_move = None
    best_distance = float('inf')
    for move, delta in possible.items():
        new_head = (head[0] + delta[0], head[1] + delta[1])
        distance = abs(new_head[0] - food[0]) + abs(new_head[1] - food[1])
        if distance < best_distance:
            best_distance = distance
            best_move = delta
    return best_move

# Main game loop
running = True
while running:
    clock.tick(FPS)
    
    # Handle quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Determine the next move using the AI
    new_direction = choose_direction(snake, food)
    if new_direction is None:
        print("Game Over! Final length:", len(snake))
        running = False
        continue

    # Calculate new head position
    new_head = (snake[0][0] + new_direction[0], snake[0][1] + new_direction[1])
    snake.insert(0, new_head)

    # Check if food is eaten
    if new_head == food:
        food = spawn_food()  # Generate new food
    else:
        snake.pop()  # Remove tail segment if not eating

    # Drawing
    screen.fill(BLACK)
    draw_rect(RED, food)
    for segment in snake:
        draw_rect(GREEN, segment)
    pygame.display.update()

pygame.quit()
sys.exit()
