import pygame
import random


def start_game():
    global game_active
    game_active = True
    print('Start Game')
    # 必要に応じて初期化処理を追加


def draw_button(screen, text, x, y, width, height, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # ボタンの領域内にマウスがあるかどうかをチェック
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, width, height))  # ホバー時の色
        if click[0] == 1 and action != None:  # 左クリックされた場合
            action()
    else:
        pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))  # 通常時の色

    # ボタンのテキストを描画
    small_text = pygame.font.Font(None, 20)
    text_surf = small_text.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    screen.blit(text_surf, text_rect)

    return x, y, width, height   # ボタンの座標とサイズを返す


def text_objects(text, font):
    text_surface = font.render(text, True, (255, 255, 255))
    return text_surface, text_surface.get_rect()


def quit_game():
    print('Bye Bye Game!!')
    pygame.quit()
    quit()


def restart_game():
    global game_active, game_over, paddle_x, paddle_y, ball_x, ball_y, blocks, ball_x_change, ball_y_change
    game_active = True
    game_over = False

    # パドル、ボール、ブロックの位置を初期化
    paddle_x = 350
    paddle_y = 550
    ball_x = 390
    ball_y = 540
    ball_x_change = 0.15
    ball_y_change = -0.15
    blocks = [(j * 100, i * 50) for i in range(5) for j in range(8)]
    print('Restart Game')


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Block Shoot")

# ゲーム状態変数
game_active = False
game_over = False
running = True
game_clear = False

# # ゲームの初期設定
# パドルの設定
paddle_img = pygame.Surface((100, 20))
paddle_img.fill((255, 255, 255))
paddle_x = 350
paddle_y = 550
paddle_x_change = 0

# ボールの設定
ball_img = pygame.Surface((15, 15))
ball_img.fill((255, 255, 255))
ball_x = 390
ball_y = 540
ball_x_change = 0.15
ball_y_change = -0.15

# ブロックの設定
block_img = pygame.Surface((60, 30))
block_img.fill((255, 0, 0))
blocks = []
for i in range(5):  # ブロックの行
    for j in range(8):  # ブロックの列
        blocks.append((j * 100, i * 50))

# スタート画面のループ
while not game_active:
    # スタート画面の描画
    # 背景をクリア
    screen.fill((0, 0, 0))
    start_button = draw_button(screen, "Start", 350, 250, 100, 50, start_game)
    quit_button = draw_button(screen, "Quit", 350, 350, 100, 50, quit_game)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # スタートボタンのクリック判定
            if start_button[0] <= mouse_x <= start_button[0] + start_button[2] and \
                    start_button[1] <= mouse_y <= start_button[1] + start_button[3]:
                restart_game()
            # クイットボタンのクリック判定
            elif quit_button[0] <= mouse_x <= quit_button[0] + quit_button[2] and \
                    quit_button[1] <= mouse_y <= quit_button[1] + quit_button[3]:
                quit_game()

    pygame.display.update()

# # ゲームメインループ
while running:
    screen.fill((0, 0, 0))  # 画面をクリア

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                paddle_x_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                paddle_x_change = 0

    if game_over:
        screen.fill((0, 0, 0))

        # ボタンを描画し、座標とサイズを取得
        restart_button = draw_button(screen, "Restart", 350, 250, 100, 50)
        quit_button = draw_button(screen, "Quit", 350, 350, 100, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # リスタートボタンのクリック判定
                if restart_button[0] <= mouse_x <= restart_button[0] + restart_button[2] and \
                        restart_button[1] <= mouse_y <= restart_button[1] + restart_button[3]:
                    restart_game()
                # クイットボタンのクリック判定
                elif quit_button[0] <= mouse_x <= quit_button[0] + quit_button[2] and \
                        quit_button[1] <= mouse_y <= quit_button[1] + quit_button[3]:
                    quit_game()

        pygame.display.flip()

    elif game_clear:
        # ゲームクリア画面の表示と処理（XXXに相当するコード）
        screen.fill((0, 0, 0))  # 画面をクリア
        clear_button = draw_button(screen, "Back to Start", 350, 250, 200, 50)
        quit_button = draw_button(screen, "Quit", 350, 350, 100, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type is pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if clear_button[0] <= mouse_x <= clear_button[0] + clear_button[2] and \
                        clear_button[1] <= mouse_y <= clear_button[1] + clear_button[3]:
                    restart_game()
                    game_active = False
                    game_clear = False
                    game_over = False
                elif quit_button[0] <= mouse_x <= quit_button[0] + quit_button[2] and \
                        quit_button[1] <= mouse_y <= quit_button[1] + quit_button[3]:
                    quit_game()

        pygame.display.flip()

    elif game_active:
        # ここにゲームのメインロジックを追加
        # パドルの位置情報、ボールの位置更新、衝突判定など
        # ここにゲームのメインロジックを追加
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle_x_change = -0.3
                if event.key == pygame.K_RIGHT:
                    paddle_x_change = 0.3
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    paddle_x_change = 0

        # パドルの位置情報
        paddle_x += paddle_x_change
        screen.blit(paddle_img, (paddle_x, paddle_y))

        # ボールの位置更新
        ball_x += ball_x_change
        ball_y += ball_y_change
        screen.blit(ball_img, (ball_x, ball_y))

        # ボールの衝突判定
        # ここに衝突判定のコードを追加
        # ボールとパドルの衝突判定
        if ball_x > paddle_x and ball_x < paddle_x + 100 and ball_y > paddle_y and ball_y < paddle_y + 20:
            ball_y_change = -ball_y_change

        # ボールとブロックの衝突判定
        for block in blocks[:]:
            if ball_x > block[0] and ball_x < block[0] + 60 and ball_y > block[1] and ball_y < block[1] + 30:
                blocks.remove(block)
                ball_y_change = -ball_y_change

        # ボールが画面の端に衝突した場合の処理
        if ball_x <= 0 or ball_x >= 785:
            ball_x_change = -ball_x_change
        if ball_y <= 0:
            ball_y_change = -ball_y_change

        # ブロックの描画
        for block in blocks:
            screen.blit(block_img, block)

        if not blocks:
            game_active = False
            game_clear = True  # ゲームクリアフラグを追加

    pygame.display.flip()

    # ボールが画面下部に到達したかのチェック
    if ball_y > 600:
        game_over = True

    # すべてのブロックが消去されたかのチェック
    if not blocks and not game_over:
        game_clear = True
