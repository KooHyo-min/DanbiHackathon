import os
import pygame


text_color = (255, 255, 255)

# screen variables
min_screen_coord = (0, 0)
max_screen_coord = (960, 720)
screen_res = max_screen_coord

# game parameters
block_width, block_height = 32, 32
columns = 10
rows = 20
FPS = 60
display_fps = False
display_time = True

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

if __name__ == '__main__':
    main()
