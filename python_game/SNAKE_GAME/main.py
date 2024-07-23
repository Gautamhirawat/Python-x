import pygame
import time
import random
import json

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
OBSTACLE_COUNT = 10
POWERUP_DURATION = 200  # frames

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Advanced Snake Game')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

clock = pygame.time.Clock()
FPS = 15

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])  # Up, Down, Left, Right
        self.color = GREEN
        self.score = 0
        self.powered_up = False
        self.powerup_timer = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * CELL_SIZE)) % WIDTH), (cur[1] + (y * CELL_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])  # Up, Down, Left, Right
        self.score = 0
        self.powered_up = False
        self.powerup_timer = 0

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], CELL_SIZE, CELL_SIZE))
        if self.powered_up:
            pygame.draw.rect(surface, YELLOW, (self.positions[0][0], self.positions[0][1], CELL_SIZE, CELL_SIZE))

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.turn((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.turn((1, 0))

    def update_powerup(self):
        if self.powered_up:
            self.powerup_timer -= 1
            if self.powerup_timer <= 0:
                self.powered_up = False

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                         random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

class Obstacle:
    def __init__(self):
        self.positions = []
        self.color = BLUE
        self.randomize_positions()

    def randomize_positions(self):
        for _ in range(OBSTACLE_COUNT):
            position = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                        random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
            self.positions.append(position)

    def draw(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, self.color, (pos[0], pos[1], CELL_SIZE, CELL_SIZE))

class PowerUp:
    def __init__(self, color):
        self.position = (0, 0)
        self.color = color
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                         random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

def draw_text(surface, text, size, color, position):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = position
    surface.blit(text_surface, text_rect)

def save_high_score(score):
    try:
        with open('high_scores.json', 'r') as file:
            high_scores = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        high_scores = []

    high_scores.append(score)
    high_scores = sorted(high_scores, reverse=True)[:5]

    with open('high_scores.json', 'w') as file:
        json.dump(high_scores, file)

def display_high_scores():
    window.fill(BLACK)
    draw_text(window, 'High Scores', 48, RED, (WIDTH // 2 - 100, HEIGHT // 2 - 150))
    try:
        with open('high_scores.json', 'r') as file:
            high_scores = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        high_scores = []

    for i, score in enumerate(high_scores):
        draw_text(window, f'{i + 1}. {score}', 36, WHITE, (WIDTH // 2 - 50, HEIGHT // 2 - 100 + i * 40))

    draw_text(window, 'Press any key to continue', 24, WHITE, (WIDTH // 2 - 150, HEIGHT // 2 + 100))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                return

def pause():
    draw_text(window, 'Paused', 48, RED, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    draw_text(window, 'Press P to resume', 36, WHITE, (WIDTH // 2 - 180, HEIGHT // 2 + 10))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return

def game_over(score):
    save_high_score(score)
    window.fill(BLACK)
    draw_text(window, 'Game Over', 48, RED, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    draw_text(window, 'Press any key to restart', 36, WHITE, (WIDTH // 2 - 180, HEIGHT // 2 + 10))
    pygame.display.update()
    time.sleep(2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                return

def main():
    snake = Snake()
    food = Food()
    obstacles = Obstacle()
    powerups = [PowerUp(ORANGE)]
    powerup_spawned = False

    while True:
        snake.handle_keys()
        snake.move()
        snake.update_powerup()

        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
            if not powerup_spawned:
                for powerup in powerups:
                    powerup.randomize_position()
                powerup_spawned = True

        for powerup in powerups:
            if powerup_spawned and snake.get_head_position() == powerup.position:
                snake.powered_up = True
                snake.powerup_timer = POWERUP_DURATION
                powerup_spawned = False

        for pos in obstacles.positions:
            if snake.get_head_position() == pos and not snake.powered_up:
                game_over(snake.score)
                return

        window.fill(BLACK)
        snake.draw(window)
        food.draw(window)
        obstacles.draw(window)
        if powerup_spawned:
            for powerup in powerups:
                powerup.draw(window)
        draw_text(window, f'Score: {snake.score}', 18, WHITE, (10, 10))

        pygame.display.update()
        clock.tick(FPS + snake.score // 5)

while True:
    main()
    display_high_scores()
