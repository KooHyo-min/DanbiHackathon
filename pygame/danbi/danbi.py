from time import sleep

import pygame
import os
import speech_recognition as sr

WHITE = (255, 255, 255)
IMG_RES = 'pygame/danbi/resources/images/{}'
AUDIO_RES = 'pygame/danbi/resources/audio/{}'
RUN = True



pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Danbi")
font = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 50)
background = pygame.image.load(IMG_RES.format('background.jpg'))
background.set_alpha(124)
loud_speaker = pygame.image.load(IMG_RES.format('loud_speaker.png'))
# picture = pygame.transform.scale(background, (1920, 1080))
while RUN:
    screen.fill(WHITE)
    screen.blit(background, (0,0))
    screen.blit(loud_speaker, (0, 0))
    # 1) 사용자 입력 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if loud_speaker.get_rect().collidepoint(x, y):
                r = sr.Recognizer()
                harvard = sr.AudioFile(AUDIO_RES.format('LH_E101_Good Morning_1.wav'))
                with harvard as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.record(source, duration=6)
                left = font.render("SayHoHo!", True, (0, 0, 0))
                screen.blit(left, (100, 100))
                pygame.display.flip()
                result = r.recognize_google(audio)
                screen.fill(WHITE)
                text = font2.render(result, True, (0, 40, 0))
                textRect = text.get_rect()
                textRect.centerx = screen.get_rect().centerx
                textRect.centery = screen.get_rect().centery
                screen.blit(text, textRect)
                pygame.display.flip()
                sleep(3)

        pygame.display.flip()
"""
 for event in ev:

    # handle MOUSEBUTTONUP
    if event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()

      # get a list of all sprites that are under the mouse cursor
      clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
"""