import os
import pygame


class Menu:
    margin_x = 35
    margin_y = 50  # space between items(y axis)
    text_color = (255, 255, 255)
    selected_color = (0, 255, 255)

    def __init__(self, title, background_path, screen_res, font, coord):
        self.title = title
        self.background = pygame.image.load(background_path).convert()
        self.background = pygame.transform.scale(self.background, screen_res)

        self.items = []
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
        for i in range(len(self.items)):
            if i == self.selected_item:
                color = self.selected_color
            else:
                color = self.text_color

            item_surface = write(self.items_font, self.items[i], color)
            screen.blit(item_surface, (self.items_coord[0],
                                         self.items_coord[1] + offset_y))
            offset_y += Menu.margin_y

    def check_input(self, event):
        """
        Check keyboard input and change selected item
        :param event: pygame.event
        :return: selected item name if an item is selected, else None
        """
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if self.selected_item == 0:
                self.selected_item = len(self.items) - 1
            else:
                self.selected_item -= 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            self.selected_item = (self.selected_item + 1) % len(self.items)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return self.items[self.selected_item]

        return None


def write(font, message, color):
    text = font.render(str(message), True, color)
    text = text.convert_alpha()
    return text

