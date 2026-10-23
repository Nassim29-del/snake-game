import pygame
import random

pygame.init()

width = 600
height = 400
cell_size = 20

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

Black = (0, 0, 0)
Green = (0, 255, 0)
Red = (255, 0, 0)
White = (255, 255, 255)

clock = pygame.time.Clock()

snake = [(100, 100)]

food = (
    random.randrange(0, width, cell_size),
    random.randrange(0, height, cell_size)
)

direction = (cell_size, 0)
new_direction = direction
score = 0
font = pygame.font.SysFont(None, 30)
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if not game_over:
                if event.key == pygame.K_UP and direction != (0, cell_size):
                    new_direction = (0, -cell_size)
                elif event.key == pygame.K_DOWN and direction != (0, -cell_size):
                    new_direction = (0, cell_size)
                elif event.key == pygame.K_LEFT and direction != (cell_size, 0):
                    new_direction = (-cell_size, 0)
                elif event.key == pygame.K_RIGHT and direction != (-cell_size, 0):
                    new_direction = (cell_size, 0)

    if not game_over:
        direction = new_direction
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])

        if (
            new_head[0] < 0 or new_head[0] >= width
            or new_head[1] < 0 or new_head[1] >= height
            or new_head in snake
        ):
            game_over = True
        else:
            snake.insert(0, new_head)

            if new_head == food:
                score += 1
                food = (
                    random.randrange(0, width, cell_size),
                    random.randrange(0, height, cell_size)
                )
            else:
                snake.pop()

    screen.fill(Black)

    pygame.draw.rect(
        screen, Red,
        (food[0], food[1], cell_size, cell_size)
    )

    for segment in snake:
        pygame.draw.rect(
            screen, Green,
            (segment[0], segment[1], cell_size, cell_size)
        )

    score_text = font.render(f"Score: {score}", True, White)
    screen.blit(score_text, (10, 10))

    if game_over:
        message = font.render("Game Over! Press ESC to quit", True, White)
        screen.blit(message, (100, height // 2))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()