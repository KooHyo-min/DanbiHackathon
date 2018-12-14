import os
import pygame


class Popup:
    text_color = (255, 255, 255)

    def __init__(self, title, background_path, screen_res, font, coord):
        self.title = title
        self.background = pygame.image.load(background_path).convert()
        self.background = pygame.transform.scale(self.background, screen_res)

        self.items = {}
        self.items_rect = {}
        self.selected_item = 0
        if font:
            self.title_font = pygame.font.Font(os.path.join('fonts', font), 26)
            self.items_font = pygame.font.Font(os.path.join('fonts', font), 18)
        else:
            self.title_font = pygame.font.Font(None, 26)
            self.items_font = pygame.font.Font(None, 18)

        self.title_coord = (0, 0)
        if not coord:
            self.items_coord = {
                "Story_PT_card_01_image": (150, 100),
                "Story_PT_card_01_text": (150, -200),
                "practice_pu_mic_effect": (-380, 50),
                "practice_pu_mic": (-380, -120),
                'exit_bt': (-600, +350)
             }

    def add_item(self, item_name, item):
        self.items.update({item_name: item})

    def remove_item(self, item_name):
        self.items.pop(item_name)

    def show(self, screen):
        screen.blit(self.background, (0, 0))
        title_surface = write(self.title_font, self.title, self.text_color)
        screen.blit(title_surface, self.title_coord)
        for item_name, item in self.items.items():
            center_xy = self.get_center_xy(screen, item)
            item_xy = self.items_coord[item_name]
            result_xy = (center_xy[0]-item_xy[0], center_xy[1] - item_xy[1])
            item_rect = screen.blit(item, result_xy)
            self.items_rect.update({item_name: item_rect})

    def get_center_xy(self, screen, item):
        return (screen.get_rect().centerx - item.get_rect().centerx, screen.get_rect().centery - item.get_rect().centery)

    def check_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for item_name, item in self.items_rect.items():
                if item.collidepoint(x, y):
                    return item_name

        return None


def write(font, message, color):
    text = font.render(str(message), True, color)
    text = text.convert_alpha()
    return text

