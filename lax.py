import vlc
import pygame
import sys
import time
import config as cfg


def writings():
    height = screen.get_height()
    screen.blit(myfont.render('S-Tow', False, (0, 0, 250)), (10, height/2 - 100))
    screen.blit(myfont.render('N-Tow', False, (0, 0, 250)), (10, height/2 - 60))
    screen.blit(myfont.render('S-Gnd', False, (0, 0, 250)), (10, height/2 - 20))
    screen.blit(myfont.render('N-Gnd', False, (0, 0, 250)), (10, height/2 + 20))
    screen.blit(myfont.render('S-App', False, (0, 0, 250)), (10, height/2 + 60))
    screen.blit(myfont.render('N-App', False, (0, 0, 250)), (10, height/2 + 100))

instance = vlc.Instance("-q")
s1 = vlc.MediaPlayer(instance, cfg.SOUTH_TOWER)
s2 = vlc.MediaPlayer(instance, cfg.NORTH_TOWER)
s3 = vlc.MediaPlayer(instance, cfg.SOUTH_GROUND)
s4 = vlc.MediaPlayer(instance, cfg.NORTH_GROUND)
s5 = vlc.MediaPlayer(instance, cfg.SOUTH_FINAL_APP)
s6 = vlc.MediaPlayer(instance, cfg.NORTH_FINAL_APP)

bg = pygame.image.load("LAX.png")
size = (500, 300)

pygame.font.init()
screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
screen.blit(bg, (0, 0))

myfont = pygame.font.SysFont('Times New Romans', 30)
writings()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(
            event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
            screen.blit(pygame.transform.scale(bg, event.dict['size']), (0, 0))
            writings()
            pygame.display.flip()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                height = screen.get_height()
                if not s1.is_playing():
                    s1.play()
                    time.sleep(1)
                    screen.blit(myfont.render('S-Tow', False, (250, 0, 0)), (10, height/2 - 100))
                else:
                    s1.stop()
                    screen.blit(myfont.render('S-Tow', False, (0, 0, 250)), (10, height/2 - 100))
                pygame.display.flip()
            if event.key == pygame.K_y:
                height = screen.get_height()
                if not s2.is_playing():
                    s2.play()
                    time.sleep(1)
                    screen.blit(myfont.render('N-Tow', False, (250, 0, 0)), (10, height/2 - 60))
                else:
                    s2.stop()
                    screen.blit(myfont.render('N-Tow', False, (0, 0, 250)), (10, height/2 - 60))
                pygame.display.flip()
            if event.key == pygame.K_g:
                height = screen.get_height()
                if not s3.is_playing():
                    s3.play()
                    time.sleep(1)
                    screen.blit(myfont.render('S-Gnd', False, (250, 0, 0)), (10, height/2 - 20))
                else:
                    s3.stop()
                    screen.blit(myfont.render('S-Gnd', False, (0, 0, 250)), (10, height/2 - 20))
                pygame.display.flip()
            if event.key == pygame.K_h:
                height = screen.get_height()
                if not s4.is_playing():
                    s4.play()
                    time.sleep(1)
                    screen.blit(myfont.render('N-Gnd', False, (250, 0, 0)), (10, height/2 + 20))
                else:
                    s4.stop()
                    screen.blit(myfont.render('N-Gnd', False, (0, 0, 250)), (10, height/2 + 20))
                pygame.display.flip()
            if event.key == pygame.K_b:
                height = screen.get_height()
                if not s5.is_playing():
                    s5.play()
                    time.sleep(1)
                    screen.blit(myfont.render('S-App', False, (250, 0, 0)), (10, height/2 + 60))
                else:
                    s5.stop()
                    screen.blit(myfont.render('S-App', False, (0, 0, 250)), (10, height/2 + 60))
                pygame.display.flip()
            if event.key == pygame.K_n:
                height = screen.get_height()
                if not s6.is_playing():
                    s6.play()
                    time.sleep(1)
                    screen.blit(myfont.render('N-App', False, (250, 0, 0)), (10, height/2 + 100))
                else:
                    s6.stop()
                    screen.blit(myfont.render('N-App', False, (0, 0, 250)), (10, height/2 + 100))
                pygame.display.flip()
            if event.key == pygame.K_m:
                height = screen.get_height()
                s1.stop()
                s2.stop()
                s3.stop()
                s4.stop()
                s5.stop()
                s6.stop()
                screen.blit(myfont.render('S-Tow', False, (0, 0, 250)), (10, height / 2 - 100))
                screen.blit(myfont.render('N-Tow', False, (0, 0, 250)), (10, height / 2 - 60))
                screen.blit(myfont.render('S-Gnd', False, (0, 0, 250)), (10, height / 2 - 20))
                screen.blit(myfont.render('N-Gnd', False, (0, 0, 250)), (10, height / 2 + 20))
                screen.blit(myfont.render('S-App', False, (0, 0, 250)), (10, height / 2 + 60))
                screen.blit(myfont.render('N-App', False, (0, 0, 250)), (10, height/2 + 100))
                pygame.display.flip()
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                sys.exit(1)
