import pygame
import random


pygame.init()


screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Ball")

#time
clock = pygame.time.Clock()

#colors
white = (0, 0, 0)
black = (255, 255, 255)

#paddle
paddle_width = 100
paddle_height = 10
paddle_x = screen_width / 2 - paddle_width / 2
paddle_y = screen_height - 50
paddle_speed = 5

#ball
ball_radius = 10
ball_speed = 3
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = 0

#score
score = 0
font = pygame.font.Font(None, 30)

#lives
lives = 3

#main
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    elif keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    # Move the ball
    ball_y += ball_speed

    # Check for collision with paddle
    if ball_y + ball_radius > paddle_y and paddle_x < ball_x < paddle_x + paddle_width:
        ball_x = random.randint(ball_radius, screen_width - ball_radius)
        ball_y = 0
        score += 1
        ball_speed += 0.2

    # Check for missed ball
    if ball_y + ball_radius > screen_height:
        ball_x = random.randint(ball_radius, screen_width - ball_radius)
        ball_y = 0
        lives -= 1
        ball_speed = 3

    # Check for game over
    if lives == 0:
        game_over = True

    # Draw the screen
    screen.fill(white)
    pygame.draw.rect(screen, black, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, black, (int(ball_x), int(ball_y)), ball_radius)
    score_text = font.render("Score: " + str(score), True, black)
    lives_text = font.render("Lives: " + str(lives), True, black)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (screen_width - 10 - lives_text.get_width(), 10))
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# End the game
pygame.quit()

