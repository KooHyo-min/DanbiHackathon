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
menu_coord = (screen_res[0] * 3 / 5, screen_res[1] / 5)
next_tetromino_coord = (screen_res[0] / 10, (screen_res[1] / 10) * 6)


def main():
    pygame.init()
    pygame.display.set_caption("DanbiHackathon")
    screen = pygame.display.set_mode(screen_res)

    img_res_path = 'resources/images/{}'
    audio_res_path = 'resources/audio/{}'

    menu_background_path = img_res_path.format('menu_bg.png')
    game__background_path = img_res_path.format('game_bg.png')

    background = pygame.image.load(menu_background_path).convert()
    background = pygame.transform.scale(background, screen.get_size())
    menu_items = ['Play', 'Quit']

    font = pygame.font.Font(None, 24)
    main_menu = Menu('DanbiHackathon', menu_background_path, screen_res, None, menu_coord)


    while True:
        display_menu = True
        while display_menu:
            main_menu.show(screen)
            pygame.display.flip()
            event = pygame.event.wait()
            user_input = main_menu.check_input(event)

            # if user_input == menu_items[0]:
            #     display_menu = False
            # elif user_input == menu_items[1] or event.type == pygame.QUIT:  # quit
            #     exit()


if __name__ == '__main__':
    main()
