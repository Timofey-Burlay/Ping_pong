import pygame


pygame.init()


width, height = 800, 600
fps = 60


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Пинг-Понг')


black = (100, 200, 100)
white = (255, 255, 255)
black_ball = (100, 45, 0)
red = (255, 0, 0)

# Координаты и размеры элементов
paddle_width, paddle_height = 20, 85
ball_size = 40

# Позиции ракеток и мяча
left_paddle = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(width - 60, height // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)


speed_x = 3
speed_y = 3


score_player1 = 0
score_player2 = 0


font = pygame.font.SysFont(None, 36)
font1 = pygame.font.SysFont(None, 50)

# Основной игровой цикл
running = True
play = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if play == True:

        # Управление первой ракеткой (левый игрок)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= 5
        elif keys[pygame.K_s] and left_paddle.bottom < height:
            left_paddle.y += 5

        # Управление второй ракеткой (правый игрок)
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= 5
        elif keys[pygame.K_DOWN] and right_paddle.bottom < height:
            right_paddle.y += 5


        ball.x += speed_x
        ball.y += speed_y

        # Столкновения с верхним и нижним краями
        if ball.top <= 0 or ball.bottom >= height:
            speed_y *= -1

        # Забивание голов и обновление счёта
        if ball.left <= 0:
            score_player2 += 1
            ball.center = (width // 2, height // 2)
        elif ball.right >= width:
            score_player1 += 1
            ball.center = (width // 2, height // 2)


        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            speed_x *= -1

    screen.fill(black)

    if score_player1 >= 5:
        lose_t = font1.render('2 игрок проиграл', True, red)
        screen.blit(lose_t, (200, 100))
        play = False

    if score_player2 >= 5:
        lose_tt = font1.render('1 игрок проиграл', True, red)
        screen.blit(lose_tt, (200, 100))
        play = False




    pygame.draw.rect(screen, white, left_paddle)
    pygame.draw.rect(screen, white, right_paddle)
    pygame.draw.ellipse(screen, black_ball, ball)


    score_text = f'{score_player1} : {score_player2}'
    score_surface = font.render(score_text, True, white)
    screen.blit(score_surface, (width // 2 - score_surface.get_width() // 2, 10))


    pygame.display.flip()


    pygame.time.Clock().tick(fps)


pygame.quit()
