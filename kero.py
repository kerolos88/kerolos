import pygame
import random

# تهيئة مكتبة pygame
pygame.init()

# إعدادات الشاشة
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Many Bricks Breaker")

# إعدادات الألوان
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# إعدادات الكرة
ball_speed = [4, -4]
ball_radius = 10
ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50]

# إعدادات المضرب
paddle_width, paddle_height = 100, 10
paddle_speed = 8
paddle_pos = [SCREEN_WIDTH // 2 - paddle_width // 2, SCREEN_HEIGHT - 30]

# إعدادات الطوب
brick_width, brick_height = 75, 20
bricks = []
for i in range(6):
    for j in range(10):
        brick_rect = pygame.Rect(j * (brick_width + 5) + 35, i * (brick_height + 5) + 35, brick_width, brick_height)
        bricks.append(brick_rect)

# تشغيل اللعبة
running = True
while running:
    screen.fill((0, 0, 20))

    # أحداث اللعبة
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # حركة المضرب
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_pos[0] > 0:
        paddle_pos[0] -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_pos[0] < SCREEN_WIDTH - paddle_width:
        paddle_pos[0] += paddle_speed

    # حركة الكرة
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # اصطدام الكرة مع الجدران
    if ball_pos[0] <= ball_radius or ball_pos[0] >= SCREEN_WIDTH - ball_radius:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= ball_radius:
        ball_speed[1] = -ball_speed[1]

    # اصطدام الكرة مع المضرب
    paddle_rect = pygame.Rect(paddle_pos[0], paddle_pos[1], paddle_width, paddle_height)
    if paddle_rect.collidepoint(ball_pos[0], ball_pos[1] + ball_radius):
        ball_speed[1] = -ball_speed[1]

    # اصطدام الكرة مع الطوب
    for brick in bricks[:]:
        if brick.collidepoint(ball_pos[0], ball_pos[1] - ball_radius):
            ball_speed[1] = -ball_speed[1]
            bricks.remove(brick)

    # رسم الطوب
    for brick in bricks:
        pygame.draw.rect(screen, random.choice([RED, YELLOW, GREEN]), brick)

    # رسم الكرة
    pygame.draw.circle(screen, WHITE, ball_pos, ball_radius)

    # رسم المضرب
    pygame.draw.rect(screen, BLUE, paddle_rect)

    # إنهاء اللعبة إذا سقطت الكرة
    if ball_pos[1] > SCREEN_HEIGHT:
        running = False

    # تحديث الشاشة
    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
