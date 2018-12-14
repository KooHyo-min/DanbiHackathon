from copy import deepcopy

import pygame

from menu import Menu
from practice import Practice
from popup import Popup
import speech_recognition as sr

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

    practice_01_path = img_res_path.format('practice_01.png')
    back_bt_path = img_res_path.format('back_bt.png')
    Story_PT_card_01_path = img_res_path.format('Story_PT_card_01.png')
    Story_PT_card_02_path = img_res_path.format('Story_PT_card_02.png')
    Story_PT_card_03_path = img_res_path.format('Story_PT_card_03.png')
    Story_PT_card_04_path = img_res_path.format('Story_PT_card_04.png')
    Story_PT_card_05_path = img_res_path.format('Story_PT_card_05.png')
    Story_PT_card_06_path = img_res_path.format('Story_PT_card_06.png')
    Story_PT_card_07_path = img_res_path.format('Story_PT_card_07.png')
    Story_PT_card_08_path = img_res_path.format('Story_PT_card_08.png')
    Story_PT_card_09_path = img_res_path.format('Story_PT_card_09.png')

    popup_bg_path = img_res_path.format('popup_bg.png')

    practice_pu_mic_path = img_res_path.format('practice_pu_mic.png')
    practice_pu_mic_effect_path = img_res_path.format('practice_pu_mic_effect.png')


    practice_pu_mic = pygame.image.load(practice_pu_mic_path)
    practice_pu_mic_effect = pygame.image.load(practice_pu_mic_effect_path)

    back_bt = pygame.image.load(back_bt_path)
    Story_PT_card_01 = pygame.image.load(Story_PT_card_01_path)
    Story_PT_card_02 = pygame.image.load(Story_PT_card_02_path)
    Story_PT_card_03 = pygame.image.load(Story_PT_card_03_path)
    Story_PT_card_04 = pygame.image.load(Story_PT_card_04_path)
    Story_PT_card_05 = pygame.image.load(Story_PT_card_05_path)
    Story_PT_card_06 = pygame.image.load(Story_PT_card_06_path)
    Story_PT_card_07 = pygame.image.load(Story_PT_card_07_path)
    Story_PT_card_08 = pygame.image.load(Story_PT_card_08_path)
    Story_PT_card_09 = pygame.image.load(Story_PT_card_09_path)

    menu_challenge_bt = pygame.image.load(menu_challenge_bt_path)
    menu_practice_bt = pygame.image.load(menu_practice_bt_path)
    menu_exit_bt = pygame.image.load(menu_exit_bt_path)

    menu_items = {
        'challenge_bt': menu_challenge_bt,
        'practice_bt': menu_practice_bt,
        'exit_bt': menu_exit_bt
    }

    font = pygame.font.Font(None, 50)
    main_menu = Menu('DanbiHackathon V0.1', menu_background_path, screen_res, None, None)
    for item_name, item in menu_items.items():
        main_menu.add_item(item_name, item)

    practice_items = {
        "back_bt": back_bt,
        "Story_PT_card_01": Story_PT_card_01,
        "Story_PT_card_02": Story_PT_card_02,
        "Story_PT_card_03": Story_PT_card_03,
        "Story_PT_card_04": Story_PT_card_04,
        "Story_PT_card_05": Story_PT_card_05,
        "Story_PT_card_06": Story_PT_card_06,
        "Story_PT_card_07": Story_PT_card_07,
        "Story_PT_card_08": Story_PT_card_08,
        "Story_PT_card_09": Story_PT_card_09
    }

    practice_game = Practice('DanbiHackathon V0.1', practice_01_path, screen_res, None, None)
    for item_name, item in practice_items.items():
        practice_game.add_item(item_name, item)

    popup_items = {
        "practice_pu_mic": practice_pu_mic,
        "exit_bt": menu_exit_bt
    }

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
                practice_game.show(screen)
                pygame.display.flip()
            elif user_input == 'exit_bt' or event.type == pygame.QUIT:  # quit
                exit()

        while practice:
            event = pygame.event.wait()
            user_input = practice_game.check_input(event)
            if user_input == 'back_bt':
                display_menu = True
                practice = False
            elif event.type == pygame.QUIT:
                exit()
            elif user_input and user_input.startswith('Story'):
                popup = True
                # practice = False
                # display_menu = False
                game_popup = Popup('DanbiHackathon V0.1', popup_bg_path, screen_res, None, None)
                text_name = '{}_text'.format(user_input)
                image_name = '{}_image'.format(user_input)
                text_path = img_res_path.format('{}.png'.format(text_name))
                image_path = img_res_path.format('{}.png'.format(image_name))
                text = pygame.image.load(text_path)
                image = pygame.image.load(image_path)
                in_pop_up_items = popup_items
                in_pop_up_items.update({text_name: text, image_name: image})
                for item_name, item in in_pop_up_items.items():
                    game_popup.add_item(item_name, item)
                game_popup.show(screen)
                pygame.display.flip()
                while popup:
                    event = pygame.event.wait()
                    popup_user_input = game_popup.check_input(event)
                    if popup_user_input == 'exit_bt':
                        popup = False
                        practice_game.show(screen)
                        pygame.display.flip()
                    elif event.type == pygame.QUIT:
                        exit()
                    elif popup_user_input == 'Story_PT_card_01_text':
                        pygame.mixer.music.load('resources/audio/Story_PT_card_01_audio.wav')
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play()
                    elif popup_user_input == 'practice_pu_mic':
                        game_popup.add_item("practice_pu_mic_effect", practice_pu_mic_effect)
                        game_popup.show(screen)
                        pygame.display.flip()
                        r = sr.Recognizer()
                        mic = sr.Microphone(device_index=sr.Microphone.list_microphone_names().index('default'))
                        with mic as source:
                            audio = r.record(source, duration=3)
                        try:
                            result = r.recognize_google(audio)
                        except:
                            result = None

                        game_popup.remove_item("practice_pu_mic_effect")
                        game_popup.show(screen)
                        pygame.display.flip()
                        if result:
                            full = "alligator"
                            part_sc = 100 / len(full)
                            result_sc = 0
                            for i in range(len(full)):
                                try:
                                    if result[i] == full[i]:
                                         result_sc += part_sc
                                except:
                                    pass
                            if result_sc > 0:
                                text = "Your Score : {}".format(str(int(result_sc)))
                                text_0 = result
                                text_result_0 = font.render(text_0, True, (0, 40, 0))
                                textRect = text_result_0.get_rect()
                                textRect.centerx = 1020
                                textRect.centery = 250
                                screen.blit(text_result_0, textRect)
                            else:
                                text = "RETRY!!!"
                        else:
                            text = "RETRY!!!"
                        text_result = font.render(text, True, (0, 40, 0))
                        textRect = text_result.get_rect()
                        textRect.centerx = 1020
                        textRect.centery = 300
                        screen.blit(text_result, textRect)
                        pygame.display.flip()
        while challenge:
            exit()


if __name__ == '__main__':
    main()
