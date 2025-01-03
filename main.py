import pgzrun, os, pygame

WIDTH = 1500
HEIGHT = 800
TITLE = "PONG"

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

ball = pygame.image.load('images/ball.png')
scaled_ball = pygame.transform.scale(ball, (50, 50))
pygame.image.save(scaled_ball, 'images/ball.png')

ball = Actor("ball")
ball.pos = WIDTH // 2, HEIGHT // 2

ball_speed = [4, 4]

paddle_width = 17
paddle_height = 100
player1 = Rect((30, HEIGHT // 2 - paddle_height // 2), (paddle_width, paddle_height))
player2 = Rect((WIDTH - 50, HEIGHT // 2 - paddle_height // 2), (paddle_width, paddle_height))
paddle_speed = 6

score1 = 0
score2 = 0

def draw():
    screen.clear()
    screen.draw.filled_rect(player1, "white")
    screen.draw.filled_rect(player2, "white")
    ball.draw()
    screen.draw.text(f"{score1}", (WIDTH // 4, 30), fontsize=50, color="white")
    screen.draw.text(f"{score2}", (3 * WIDTH // 4, 30), fontsize=50, color="white")

def update():
    global score1, score2

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    if ball.left <= 0:
        score2 += 1
        reset_ball()
    if ball.right >= WIDTH:
        score1 += 1
        reset_ball()

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed[0] = -ball_speed[0]

    if keyboard.w and player1.top > 0:
        player1.y -= paddle_speed
    if keyboard.s and player1.bottom < HEIGHT:
        player1.y += paddle_speed

    if keyboard.up and player2.top > 0:
        player2.y -= paddle_speed
    if keyboard.down and player2.bottom < HEIGHT:
        player2.y += paddle_speed

def reset_ball():
    ball.pos = WIDTH // 2, HEIGHT // 2
    ball_speed[0] = -ball_speed[0]

pgzrun.go()
