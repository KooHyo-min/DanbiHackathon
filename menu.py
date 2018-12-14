import os
import pygame


class Menu:
    margin_x = 35
    margin_y = 100  # space between items(y axis)
    text_color = (255, 255, 255)
    selected_color = (0, 255, 255)

    def __init__(self, title, background_path, screen_res, font, coord):
        self.title = title
        self.background = pygame.image.load(background_path).convert()
        self.background = pygame.transform.scale(self.background, screen_res)

        self.items = []
        self.items_rect = []
        self.selected_item = 0
        if font:
            self.title_font = pygame.font.Font(os.path.join('fonts', font), 26)
            self.items_font = pygame.font.Font(os.path.join('fonts', font), 18)
        else:
            self.title_font = pygame.font.Font(None, 26)
            self.items_font = pygame.font.Font(None, 18)

        self.title_coord = tuple(coord)
        self.items_coord = (coord[0] + Menu.margin_x, coord[1] + Menu.margin_y)

    def add_item(self, item):
        self.items.append(item)

    def show(self, screen):
        """
        Blit all menu items.
        :param screen: screen surface
        """
        screen.blit(self.background, (0, 0))
        title_surface = write(self.title_font, self.title, self.text_color)
        screen.blit(title_surface, self.title_coord)

        # blit menu items
        offset_y = Menu.margin_y
        print(self.items[0])
        for i in range(len(self.items)):
            item_rect = screen.blit(self.items[i], (self.items_coord[0], self.items_coord[1] + offset_y))
            self.items_rect.append(item_rect)
            offset_y += Menu.margin_y

    def check_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i in range(len(self.items_rect)):
                if self.items_rect[i].collidepoint(x, y):
                    return self.items[i]

        return None


def write(font, message, color):
    text = font.render(str(message), True, color)
    text = text.convert_alpha()
    return text

