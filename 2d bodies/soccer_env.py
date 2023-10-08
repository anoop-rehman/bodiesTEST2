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

        self.reset_game()

    def reset_game(self):
        self.ball_pos_x = self.GRID_WIDTH // 2 * self.CELL_SIZE + self.CELL_SIZE // 2
        self.ball_pos_y = self.GRID_HEIGHT // 2 * self.CELL_SIZE + self.CELL_SIZE // 2
        self.ball_speed = 2.0

        self.player_positions = {
            'A1': [self.GRID_WIDTH // 2 - 2, self.GRID_HEIGHT // 2 - 1],
            'A2': [self.GRID_WIDTH // 2 - 2, self.GRID_HEIGHT // 2 + 1],
            'B1': [self.GRID_WIDTH // 2 + 2, self.GRID_HEIGHT // 2 - 1],
            'B2': [self.GRID_WIDTH // 2 + 2, self.GRID_HEIGHT // 2 + 1]
        }

        self.ball_possession = random.choice(['A1', 'A2', 'B1', 'B2'])
        self.scores = {'A': 0, 'B': 0}

    def check_goal(self):
        if self.net_top_position <= self.ball_pos_y <= self.net_top_position + self.net_height:
            if self.ball_pos_x <= self.CELL_SIZE:
                self.scores['B'] += 1
                return 'B'
            elif self.ball_pos_x >= self.SCREEN_WIDTH - self.CELL_SIZE:
                self.scores['A'] += 1
                return 'A'
        return None

    def step(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for player, pos in self.player_positions.items():
            actions = ['MOVE', 'SHOOT', 'PICK']
            weights = [0.6, 0.2, 0.2] if player == self.ball_possession else [0.8, 0.1, 0.1]

            chosen_action = random.choices(actions, weights, k=1)[0]

            if chosen_action == "MOVE":
                moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
                move = random.choice(moves)
                if move == 'LEFT' and pos[0] > 0:
                    pos[0] -= 1
                elif move == 'RIGHT' and pos[0] < self.GRID_WIDTH - 1:
                    pos[0] += 1
                elif move == 'UP' and pos[1] > 0:
                    pos[1] -= 1
                elif move == 'DOWN' and pos[1] < self.GRID_HEIGHT - 1:
                    pos[1] += 1

            elif chosen_action == "SHOOT" and player == self.ball_possession:
                self.ball_possession = None
                target_x = random.choice([0, self.SCREEN_WIDTH])
                target_y = random.randint(self.net_top_position, self.net_top_position + self.net_height)
                dx = target_x - self.ball_pos_x
                dy = target_y - self.ball_pos_y
                dist = max(abs(dx), abs(dy))
                self.ball_pos_x += self.ball_speed * dx / dist
                self.ball_pos_y += self.ball_speed * dy / dist

            elif chosen_action == "PICK" and self.ball_possession is None:
                if abs(self.ball_pos_x - pos[0]*self.CELL_SIZE) <= self.CELL_SIZE and abs(self.ball_pos_y - pos[1]*self.CELL_SIZE) <= self.CELL_SIZE:
                    self.ball_possession = player

        scoring_team = self.check_goal()
        if scoring_team:
            self.reset_game()

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
            pygame.draw.circle(self.screen, player_colors[player], (pos[0]*self.CELL_SIZE + self.CELL_SIZE//2, pos[1]*self.CELL_SIZE + self.CELL_SIZE//2), self.CELL_SIZE//3)

        if self.ball_possession:
            pos = self.player_positions[self.ball_possession]
            pygame.draw.circle(self.screen, (255, 0, 0), (pos[0]*self.CELL_SIZE + self.CELL_SIZE//2, pos[1]*self.CELL_SIZE + self.CELL_SIZE//2), self.CELL_SIZE//4)
        else:
            pygame.draw.circle(self.screen, (255, 0, 0), (int(self.ball_pos_x), int(self.ball_pos_y)), self.CELL_SIZE//4)

        pygame.draw.rect(self.screen, (150, 150, 150), (0, self.net_top_position, self.CELL_SIZE, self.net_height))
        pygame.draw.rect(self.screen, (150, 150, 150), (self.SCREEN_WIDTH - self.CELL_SIZE, self.net_top_position, self.CELL_SIZE, self.net_height))

        pygame.display.flip()

    def run(self):
        while True:
            self.step()
            self.render()
            time.sleep(0.5)

if __name__ == "__main__":
    env = SoccerEnv()
    env.run()
