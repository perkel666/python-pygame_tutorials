__author__ = 'Perkel'

import pygame
import os

def find_file(name):
    for root, dirs, files in os.walk(os.curdir):
        if name in files:
            print os.path.join(root, name)
            return os.path.join(root, name)


def load_image(name, rect=None):
    file_path = find_file(name)

    if rect is not None:
        try:
            image = pygame.image.load(file_path)
        except pygame.error, message:
            print 'Cannot load image:', name
            raise SystemExit, message
        image = image.convert_alpha()
        return image, image.get_rect()

    else:
        try:
            image = pygame.image.load(file_path)
        except pygame.error, message:
            print 'Cannot load image:', name
            raise SystemExit, message
        image = image.convert_alpha()
        return image


class CreateSprite(pygame.sprite.Sprite):
    def __init__(self, name, hover=None, pressed=None):
        pygame.sprite.Sprite.__init__(self)
        # DATA
        self.image, self.rect = load_image(name, True)
        self.visible = True
        self.image_no_hover = self.image
        self.image_hover = None
        self.image_pressed = None
        # State in response to input
        self.last_pressed = False
        # State of buttons

        if hover is True:
            name_path = find_file(name)
            file_path, file_fullname = os.path.split(name_path)
            file_name, file_ending = os.path.splitext(file_fullname)
            self.image_hover = load_image(file_name+"_hover"+file_ending)
        if pressed is True:
            name_path = find_file(name)
            file_path, file_fullname = os.path.split(name_path)
            file_name, file_ending = os.path.splitext(file_fullname)
            self.image_pressed = load_image(file_name+"_pressed"+file_ending)

    def get_state(self, game):

        mouse_hover = False
        mouse_button_down = False
        mouse_button_up = False



        #    is mouse over sprite ?
        if self.rect.collidepoint(game.mouse_position):
            mouse_hover = True
        else:
            mouse_hover = False
        #    is mouse button is down ?
        for event in game.events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_button_down = True
            else:
                mouse_button_down = False
        #    is mouse button is up ?
        for event in game.events:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_button_up = True
            else:
                mouse_button_up = False

        #    If mouse is on sprite and button is pressed up
        if mouse_button_up is True and mouse_hover is True:
            self.last_pressed = True
        else:
            self.last_pressed = False

        # CHANGE IMAGE GRAPHIC BASED ON INPUT
        # sprite has flags : hover, pressed
        if self.image_pressed is not None and self.image_hover is not None:
            if mouse_button_down is True and mouse_hover is True:
                self.image = self.image_pressed
            else:
                if mouse_hover is True:
                    self.image = self.image_hover
                else:
                    self.image = self.image_no_hover
        # sprite has flags: pressed
        elif self.image_pressed is not None and self.image_hover is None:
            if mouse_button_down is True and mouse_hover is True:
                self.image = self.image_pressed
            else:
                self.image = self.image_no_hover
        # sprite has flags: pressed
        elif self.image_pressed is None and self.image_hover is not None:
            if mouse_hover is True:
                self.image = self.image_hover
            else:
                self.image = self.image_no_hover

