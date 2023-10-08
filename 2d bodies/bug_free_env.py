import pygame
import sys
import random
import time

pygame.init()

GRID_WIDTH = 9
GRID_HEIGHT = 7
CELL_SIZE = 40
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pygame Soccer-like Game')

net_height = 3 * CELL_SIZE
net_top_position = (SCREEN_HEIGHT - net_height) // 2

ball_possession = random.choice(['A1', 'A2', 'B1', 'B2'])
scores = {'A': 0, 'B': 0}

def reset_ball():
    return GRID_WIDTH // 2 * CELL_SIZE + CELL_SIZE // 2, GRID_HEIGHT // 2 * CELL_SIZE + CELL_SIZE // 2

ball_pos_x, ball_pos_y = reset_ball()
ball_target_x = ball_pos_x
ball_target_y = ball_pos_y
ball_speed = 2.0

player_positions = {
    'A1': [GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2 - 1],
    'A2': [GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2 + 1],
    'B1': [GRID_WIDTH // 2 + 2, GRID_HEIGHT // 2 - 1],
    'B2': [GRID_WIDTH // 2 + 2, GRID_HEIGHT // 2 + 1]
}

running = True

def draw_x(pos_x, pos_y):
    offset = CELL_SIZE // 4
    pygame.draw.line(screen, (0, 0, 0), (pos_x - offset, pos_y - offset), (pos_x + offset, pos_y + offset), 3)
    pygame.draw.line(screen, (0, 0, 0), (pos_x + offset, pos_y - offset), (pos_x - offset, pos_y + offset), 3)

def check_goal():
    if net_top_position <= ball_pos_y <= net_top_position + net_height:
        if ball_pos_x <= CELL_SIZE:  # Ball enters left goal
            return 'B'
        elif ball_pos_x >= SCREEN_WIDTH - CELL_SIZE:  # Ball enters right goal
            return 'A'
    return None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for player in player_positions.keys():
        actions = ['MOVE', 'SHOOT', 'PICK']
        weights = [0.6, 0.3, 0.1]

        chosen_action = random.choices(actions, weights, k=1)[0]

        if player == ball_possession:
            # Player with ball either moves or shoots
            if chosen_action == 'MOVE':
                # Select a direction and try to move
                moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
                move = random.choice(moves)
                if move == 'LEFT' and player_positions[player][0] > 0:
                    player_positions[player][0] -= 1
                elif move == 'RIGHT' and player_positions[player][0] < GRID_WIDTH - 1:
                    player_positions[player][0] += 1
                elif move == 'UP' and player_positions[player][1] > 0:
                    player_positions[player][1] -= 1
                elif move == 'DOWN' and player_positions[player][1] < GRID_HEIGHT - 1:
                    player_positions[player][1] += 1
            elif chosen_action == 'SHOOT':
                ball_possession = None
                ball_target_x = random.randint(0, SCREEN_WIDTH)
                ball_target_y = random.randint(net_top_position, net_top_position + net_height)
        else:
            # Player without ball just moves or tries to pick up the ball if adjacent
            if chosen_action == 'MOVE':
                moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
                move = random.choice(moves)
                if move == 'LEFT' and player_positions[player][0] > 0:
                    player_positions[player][0] -= 1
                elif move == 'RIGHT' and player_positions[player][0] < GRID_WIDTH - 1:
                    player_positions[player][0] += 1
                elif move == 'UP' and player_positions[player][1] > 0:
                    player_positions[player][1] -= 1
                elif move == 'DOWN' and player_positions[player][1] < GRID_HEIGHT - 1:
                    player_positions[player][1] += 1
            elif chosen_action == 'PICK':
                if abs(player_positions[player][0]*CELL_SIZE + CELL_SIZE/2 - ball_pos_x) < CELL_SIZE and abs(player_positions[player][1]*CELL_SIZE + CELL_SIZE/2 - ball_pos_y) < CELL_SIZE:
                    ball_possession = player

    # Ball movement
    if ball_possession is None:
        dx = ball_target_x - ball_pos_x
        dy = ball_target_y - ball_pos_y
        dist = max(abs(dx), abs(dy))
        if dist > 0:
            ball_pos_x += ball_speed * dx / dist
            ball_pos_y += ball_speed * dy / dist

    scoring_team = check_goal()
    if scoring_team:
        scores[scoring_team] += 1
        print(f"Team {scoring_team} scored! Current Scores: A - {scores['A']} : B - {scores['B']}")
        ball_pos_x, ball_pos_y = reset_ball()
        ball_target_x = ball_pos_x
        ball_target_y = ball_pos_y
        ball_possession = random.choice(['A1', 'A2', 'B1', 'B2'])

    screen.fill((255, 255, 255))
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.rect(screen, (200, 200, 200), (x, y, CELL_SIZE, CELL_SIZE), 1)

    player_colors = {
        'A1': (0, 0, 255), 'A2': (135, 206, 235),
        'B1': (0, 128, 0), 'B2': (50, 205, 50)
    }

    for player, pos in player_positions.items():
        x, y = pos
        pygame.draw.circle(screen, player_colors[player], (x*CELL_SIZE + CELL_SIZE//2, y*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//3)

    if ball_possession:
        ball_x, ball_y = player_positions[ball_possession]
        pygame.draw.circle(screen, (255, 0, 0), (ball_x*CELL_SIZE + CELL_SIZE//2, ball_y*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//4)
    else:
        pygame.draw.circle(screen, (255, 0, 0), (int(ball_pos_x), int(ball_pos_y)), CELL_SIZE//4)

    pygame.draw.rect(screen, (150, 150, 150), (0, net_top_position, CELL_SIZE, net_height))
    pygame.draw.rect(screen, (150, 150, 150), (SCREEN_WIDTH - CELL_SIZE, net_top_position, CELL_SIZE, net_height))

    pygame.display.flip()
    time.sleep(0.5)

pygame.quit()
sys.exit()
