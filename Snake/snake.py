#[[ DONT FORGET TO INCLUDE eat_sound.wav and game_over_sound.wav AT YOUR DIRECTORY
import pygame
import random

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snake Game")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
score_font = pygame.font.Font(None, 24)

eat_sound = pygame.mixer.Sound('eat_sound.wav')
game_over_sound = pygame.mixer.Sound('game_over_sound.wav')

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 10
        self.dy = 0
        self.body = [(self.x, self.y)]
        self.length = 1
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.body.insert(0, (self.x, self.y))
        if len(self.body) > self.length:
            self.body.pop()
    
    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(screen, green, (x, y, 10, 10))
    
    def collide(self):
        if self.body[0][0] < 0 or self.body[0][0] >= screen_width or self.body[0][1] < 0 or self.body[0][1] >= screen_height:
            return True
        for i in range(1, len(self.body)):
            if self.body[0] == self.body[i]:
                return True
        return False

class Food:
    def __init__(self):
        self.x = random.randrange(0, screen_width - 10, 10)
        self.y = random.randrange(0, screen_height - 10, 10)
        self.color = red
    
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 10, 10))

class Powerup:
    def __init__(self):
        self.x = random.randrange(0, screen_width - 10, 10)
        self.y = random.randrange(0, screen_height - 10, 10)
        self.color = white
        self.type = random.choice(['length', 'speed'])
    
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 10, 10))
    
    def apply(self, snake):
        if self.type == 'length':
            snake.length += 1
        elif self.type == 'speed':
            snake.dx *= 2
            snake.dy *= 2

snake = Snake(screen_width//2, screen_height//2)
food = Food()
powerup = None
score = 0

game_over = False
game_over_text = font.render("Game Over", True, white)
score_text = score_font.render("Score: " + str(score), True, white)
restart_text = font.render("Press SPACE to restart", True, white)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.dy != 10:
                snake.dx = 0
                snake.dy = -10
            elif event.key == pygame.K_DOWN and snake.dy != -10:
                snake.dx = 0
                snake.dy = 10
            elif event.key == pygame.K_LEFT and snake.dx != 10:
                snake.dx = -10
                snake.dy = 0
            elif event.key == pygame.K_RIGHT and snake.dx != -10:
                snake.dx = 10
                snake.dy = 0
            elif event.key == pygame.K_SPACE and game_over:
                snake = Snake(screen_width//2, screen_height//2)
                food = Food()
                powerup = None
                score = 0
                game_over = False
                game_over_sound.stop()

    if not game_over:
        snake.move()

        if snake.body[0][0] == food.x and snake.body[0][1] == food.y:
            snake.length += 1
            score += 1
            eat_sound.play()
            food = Food()

            if random.random() < 0.3:
                powerup = Powerup()

        if powerup is not None and snake.body[0][0] == powerup.x and snake.body[0][1] == powerup.y:
            powerup.apply(snake)
            powerup = None

        if snake.collide():
            game_over = True
            game_over_sound.play()

        screen.fill(black)
        snake.draw()
        food.draw()
        if powerup is not None:
            powerup.draw()

        score_text = score_font.render("Score: " + str(score), True, white)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        clock.tick(20)
    else:
        screen.fill(black)
        screen.blit(game_over_text, (screen_width//2 - 100, screen_height//2 - 50))
        screen.blit(score_text, (screen_width//2 - 50, screen_height//2))
        screen.blit(restart_text, (screen_width//2 - 150, screen_height//2 + 50))

        pygame.display.flip()

        clock.tick(10)

pygame.quit()
