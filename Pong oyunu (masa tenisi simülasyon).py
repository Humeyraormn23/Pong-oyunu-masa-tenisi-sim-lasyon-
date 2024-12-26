import pygame
import sys

# Pygame'i başlat
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Raket ve top boyutları
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20

# Raket pozisyonları
paddle1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_speed = 5

# Top pozisyonu ve hızı
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 4, 4

# Skorlar
score1, score2 = 0, 0
font = pygame.font.Font(None, 36)

# Ana oyun döngüsü
while True:
    # Etkinlikleri kontrol et
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tuşları kontrol et
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle2_y += paddle_speed

    # Topu hareket ettir
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Top ekranın üstüne veya altına çarparsa yön değiştir
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_speed_y = -ball_speed_y

    # Top sol veya sağ duvara çarparsa skoru güncelle ve topu ortala
    if ball_x <= 0:
        score2 += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x = -ball_speed_x
    if ball_x >= WIDTH - BALL_SIZE:
        score1 += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x = -ball_speed_x

    # Top sol rakete çarparsa yön değiştir
    if (paddle1_y < ball_y < paddle1_y + PADDLE_HEIGHT and
            ball_x <= PADDLE_WIDTH):
        ball_speed_x = -ball_speed_x

    # Top sağ rakete çarparsa yön değiştir
    if (paddle2_y < ball_y < paddle2_y + PADDLE_HEIGHT and
            ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE):
        ball_speed_x = -ball_speed_x

    # Ekranı temizle
    screen.fill(BLACK)

    # Raketleri ve topu çiz
    pygame.draw.rect(screen, WHITE, (5, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH - 5, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Skorları ekrana yazdır
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    # Ekranı güncelle
    pygame.display.flip()

    # FPS ayarı
    pygame.time.Clock().tick(60)
