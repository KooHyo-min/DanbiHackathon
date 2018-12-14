import pygame

from menu import Menu

text_color = (255, 255, 255)

# screen variables
min_screen_coord = (0, 0)
max_screen_coord = (1280, 800)
screen_res = max_screen_coord

# game parameters
# block_width, block_height = 32, 32
# columns = 10
# rows = 20
# FPS = 60
# display_fps = False
# display_time = True

# coordinates
score_coord = (15, 50)
time_coord = (15, 100)
fps_coord = (15, 150)


def main():
    pygame.init()
    pygame.display.set_caption("DanbiHackathon")
    screen = pygame.display.set_mode(screen_res)

    img_res_path = 'resources/images/{}'
    audio_res_path = 'resources/audio/{}'

    menu_background_path = img_res_path.format('menu_bg.png')
    menu_challenge_bt_path = img_res_path.format('menu_challenge_bt.png')
    menu_practice_bt_path = img_res_path.format('menu_practice_bt.png')
    menu_exit_bt_path = img_res_path.format('menu_exit_bt.png')

    game_background_path = img_res_path.format('game_bg.png')

    game_background = pygame.image.load(game_background_path)
    game_background = pygame.transform.scale(game_background, screen.get_size())

    menu_challenge_bt = pygame.image.load(menu_challenge_bt_path)
    menu_practice_bt = pygame.image.load(menu_practice_bt_path)
    menu_exit_bt = pygame.image.load(menu_exit_bt_path)

    menu_items = {
        'challenge_bt': menu_challenge_bt,
        'practice_bt': menu_practice_bt,
        'exit_bt': menu_exit_bt
    }

    font = pygame.font.Font(None, 24)
    main_menu = Menu('DanbiHackathon V0.1', menu_background_path, screen_res, None, None)
    for item_name, item in menu_items.items():
        main_menu.add_item(item_name, item)

    while True:
        display_menu = True
        practice = False
        challenge = False
        while display_menu:
            main_menu.show(screen)
            pygame.display.flip()
            event = pygame.event.wait()
            user_input = main_menu.check_input(event)
            if user_input == 'challenge_bt':
                display_menu = False
                challenge = True
            elif user_input == 'practice_bt':
                display_menu = False
                practice = True
            elif user_input == 'exit_bt' or event.type == pygame.QUIT:  # quit
                exit()

        while practice:
            exit()
        while challenge:
            exit()


if __name__ == '__main__':
    main()
