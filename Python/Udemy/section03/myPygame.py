import pygame
import sys

# python環境
print(sys.executable)

# pygame初期化
pygame.init()

# ウィンドウ作成
screen = pygame.display.set_mode((1600, 1200))

# playerの設定
player_img = pygame.image.load('player.png')
player_x = 370
player_y = 480
player_x_change = 0
player_y_change = 0

# playerを画面に表示する関数
def player(x, y):
    screen.blit(player_img, (x, y))


# ゲームループ
running = True
while running:
    # ウィンドウの背景色
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # キーボードが押されたときのイベント
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3  # 左に移動
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3  # 右に移動
            if event.key == pygame.K_UP:
                player_y_change = -0.3
            if event.key == pygame.K_DOWN:
                player_y_change = 0.3
        # キーボードから手が離れたときのイベント
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                player_y_change = 0

    # プレイヤーの位置を更新
    player_x += player_x_change
    player_y += player_y_change

    # プレイヤーの表示
    player(player_x, player_y)

    # 画面を更新
    pygame.display.flip()

# pygame終了
pygame.quit()
