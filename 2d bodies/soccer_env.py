import pygame
import random
import time

class SoccerEnv:

    def __init__(self):
        pygame.init()

        self.GRID_WIDTH = 9
        self.GRID_HEIGHT = 7
        self.CELL_SIZE = 40
        self.SCREEN_WIDTH = self.GRID_WIDTH * self.CELL_SIZE
        self.SCREEN_HEIGHT = self.GRID_HEIGHT * self.CELL_SIZE

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption('Pygame Soccer-like Game')

        self.net_height = 3 * self.CELL_SIZE
        self.net_top_position = (self.SCREEN_HEIGHT - self.net_height) // 2

        self.initialize_game()

    def initialize_game(self):
        self.ball_pos_x, self.ball_pos_y = self.reset_ball()
        self.ball_target_x = self.ball_pos_x
        self.ball_target_y = self.ball_pos_y
        self.ball_speed = 2.0
        self.ball_possession = random.choice(['A1', 'A2', 'B1', 'B2'])
        self.scores = {'A': 0, 'B': 0}

        self.player_positions = {
            'A1': [self.GRID_WIDTH // 2 - 2, self.GRID_HEIGHT // 2 - 1],
            'A2': [self.GRID_WIDTH // 2 - 2, self.GRID_HEIGHT // 2 + 1],
            'B1': [self.GRID_WIDTH // 2 + 2, self.GRID_HEIGHT // 2 - 1],
            'B2': [self.GRID_WIDTH // 2 + 2, self.GRID_HEIGHT // 2 + 1]
        }

    def reset_ball(self):
        return self.GRID_WIDTH // 2 * self.CELL_SIZE + self.CELL_SIZE // 2, self.GRID_HEIGHT // 2 * self.CELL_SIZE + self.CELL_SIZE // 2

    def check_goal(self):
        if self.net_top_position <= self.ball_pos_y <= self.net_top_position + self.net_height:
            if self.ball_pos_x <= self.CELL_SIZE:  # Ball enters left goal
                return 'B'
            elif self.ball_pos_x >= self.SCREEN_WIDTH - self.CELL_SIZE:  # Ball enters right goal
                return 'A'
        return None

    def step(self):
        for player in self.player_positions.keys():
            actions = ['MOVE', 'SHOOT', 'PICK']
            weights = [0.6, 0.3, 0.1]

            chosen_action = random.choices(actions, weights, k=1)[0]

            if player == self.ball_possession:
                if chosen_action == 'MOVE':
                    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
                    move = random.choice(moves)
                    if move == 'LEFT' and self.player_positions[player][0] > 0:
                        self.player_positions[player][0] -= 1
                    elif move == 'RIGHT' and self.player_positions[player][0] < self.GRID_WIDTH - 1:
                        self.player_positions[player][0] += 1
                    elif move == 'UP' and self.player_positions[player][1] > 0:
                        self.player_positions[player][1] -= 1
                    elif move == 'DOWN' and self.player_positions[player][1] < self.GRID_HEIGHT - 1:
                        self.player_positions[player][1] += 1

                elif chosen_action == 'SHOOT':
                    self.ball_possession = None
                    self.ball_target_x = random.randint(0, self.SCREEN_WIDTH)
                    self.ball_target_y = random.randint(self.net_top_position, self.net_top_position + self.net_height)
            else:
                if chosen_action == 'MOVE':
                    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
                    move = random.choice(moves)
                    if move == 'LEFT' and self.player_positions[player][0] > 0:
                        self.player_positions[player][0] -= 1
                    elif move == 'RIGHT' and self.player_positions[player][0] < self.GRID_WIDTH - 1:
                        self.player_positions[player][0] += 1
                    elif move == 'UP' and self.player_positions[player][1] > 0:
                        self.player_positions[player][1] -= 1
                    elif move == 'DOWN' and self.player_positions[player][1] < self.GRID_HEIGHT - 1:
                        self.player_positions[player][1] += 1

                elif chosen_action == 'PICK':
                    if abs(self.player_positions[player][0]*self.CELL_SIZE + self.CELL_SIZE/2 - self.ball_pos_x) < self.CELL_SIZE and abs(self.player_positions[player][1]*self.CELL_SIZE + self.CELL_SIZE/2 - self.ball_pos_y) < self.CELL_SIZE:
                        self.ball_possession = player

        if self.ball_possession is None:
            dx = self.ball_target_x - self.ball_pos_x
            dy = self.ball_target_y - self.ball_pos_y
            dist = max(abs(dx), abs(dy))
            if dist > 0:
                self.ball_pos_x += self.ball_speed * dx / dist
                self.ball_pos_y += self.ball_speed * dy / dist

        scoring_team = self.check_goal()
        if scoring_team:
            self.scores[scoring_team] += 1
            print(f"Team {scoring_team} scored! Current Scores: A - {self.scores['A']} : B - {self.scores['B']}")
            self.ball_pos_x, self.ball_pos_y = self.reset_ball()
            self.ball_target_x = self.ball_pos_x
            self.ball_target_y = self.ball_pos_y
            self.ball_possession = random.choice(['A1', 'A2', 'B1', 'B2'])

    def render(self):
        self.screen.fill((255, 255, 255))
        for x in range(0, self.SCREEN_WIDTH, self.CELL_SIZE):
            for y in range(0, self.SCREEN_HEIGHT, self.CELL_SIZE):
                pygame.draw.rect(self.screen, (200, 200, 200), (x, y, self.CELL_SIZE, self.CELL_SIZE), 1)

        player_colors = {
            'A1': (0, 0, 255), 'A2': (135, 206, 235),
            'B1': (0, 128, 0), 'B2': (50, 205, 50)
        }

        for player, pos in self.player_positions.items():
            x, y = pos
            pygame.draw.circle(self.screen, player_colors[player], (x*self.CELL_SIZE + self.CELL_SIZE//2, y*self.CELL_SIZE + self.CELL_SIZE//2), self.CELL_SIZE//3)

        if self.ball_possession:
            ball_x, ball_y = self.player_positions[self.ball_possession]
            pygame.draw.circle(self.screen, (255, 0, 0), (ball_x*self.CELL_SIZE + self.CELL_SIZE//2, ball_y*self.CELL_SIZE + self.CELL_SIZE//2), self.CELL_SIZE//4)
        else:
            pygame.draw.circle(self.screen, (255, 0, 0), (int(self.ball_pos_x), int(self.ball_pos_y)), self.CELL_SIZE//4)

        pygame.draw.rect(self.screen, (150, 150, 150), (0, self.net_top_position, self.CELL_SIZE, self.net_height))
        pygame.draw.rect(self.screen, (150, 150, 150), (self.SCREEN_WIDTH - self.CELL_SIZE, self.net_top_position, self.CELL_SIZE, self.net_height))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.step()
            self.render()
            # time.sleep(0.5)

        pygame.quit()

if __name__ == "__main__":
    env = SoccerEnv()
    env.run()
