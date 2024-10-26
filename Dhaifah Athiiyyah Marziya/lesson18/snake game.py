# mengimpor perpustakaan
import pygame
import time
import random

snake_speed = 15

# Window size / Ukuran window
window_x = 720
window_y = 480

# Defining colors / Menentukan warna
black = pygame.Color(0, 0, 0)
chocolate = pygame.Color(210,105,30)
red = pygame.Color(255,0,0)
violet = pygame.Color(238,130,238)
chartreuse = pygame.Color(127,255,0)

# Menginisialisasi pygame
pygame.init()

# Initialize the game window / Inisialisasi jendela permainan
pygame.display.set_caption('Games Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller / Pengontrol FPS (bingkai per detik).
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 100]

# defining first 4 blocks of snake body
snake_body = [[100, 50],[90, 50],[80, 50],[70, 50]]
# fruit position
fruit_position = [random.randrange(1, (window_x // 15)) * 10,
                  random.randrange(1, (window_y // 15)) * 10]

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score / nilai score
score = 0

# displaying Score function / fungsi display score
def show_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, chartreuse)

    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()

    # sedang memutar teks
    game_window.blit(score_surface, score_rect)

# permainan di atas funcation
def game_over():
    # membuat objek font my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # membuat permukaan teks di mana teks akan ditarik
    game_over_surface = my_font.render(
        'your score is : ' + str(score), True, violet)
    game_over_surface1 = my_font.render(
        'this is the score result ' + str(name) , True, chartreuse)

    # buat objek persegi panjang untuk teks
    # objek permukaan
    game_over_rect = game_over_surface.get_rect()
    game_over_rect1 = game_over_surface1.get_rect()

    # mengatur posisi teks
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_over_rect1.midbottom = (window_x / 2, window_y / 5)

    # blit akan menggambar teks di layar
    game_window.blit(game_over_surface, game_over_rect)
    game_window.blit(game_over_surface1, game_over_rect1)
    pygame.display.flip()

    # setelah 5 detik kita akan keluar dari program
    time.sleep(8)

    # menonaktifkan perpustakaan pygame
    pygame.quit()

    # keluar dari program
    quit()

name = input(f"Silahkan Masukkan Nama Anda : ")

# Fungsi utama
while True:


    # menangani peristiwa penting
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Jika dua tombol ditekan secara bersamaan
    # kami tidak ingin ular bergerak menjadi dua arah secara bersamaan
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Memindahkan ular
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Mekanisme pertumbuhan tubuh ular
    # jika buah dan ular bertabrakan maka skor akan bertambah 20
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 20
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, violet,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, chocolate, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Kondisi Game Over
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Menyentuh tubuh ular
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # menampilkan skor terus menerus
    show_score(5, violet, 'times new roman', 30)

    # Segarkan layar permainan
    pygame.display.update()

    # Frame Per Detik / Kecepatan Penyegaran
    fps.tick(snake_speed)