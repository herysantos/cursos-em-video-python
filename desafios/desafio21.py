import pygame

pygame.init()
pygame.mixer.music.load('/home/hery/pythonscritps/cursos_em_videos_mundo_1/media/file.mp3')
pygame.mixer.music.play(0)
pygame.event.wait()
