import os
import pygame


class Practice:
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
                "back_bt": (25, 20),
                "Story_PT_card_01": (60, 300),
                "Story_PT_card_02": (300, 300),
                "Story_PT_card_03": (540, 300),
                "Story_PT_card_04": (780, 300),
                "Story_PT_card_05": (1020, 300),
                "Story_PT_card_06": (60, 530),
                "Story_PT_card_07": (300, 530),
                "Story_PT_card_08": (540, 530),
                "Story_PT_card_09": (780, 530)
             }

    def add_item(self, item_name, item):
        self.items.update({item_name: item})

    def show(self, screen):
        screen.blit(self.background, (0, 0))
        title_surface = write(self.title_font, self.title, self.text_color)
        screen.blit(title_surface, self.title_coord)
        for item_name, item in self.items.items():
            center_xy = self.get_center_xy(screen, item)
            item_xy = self.items_coord[item_name]
            result_xy = (item_xy[0], item_xy[1])
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

