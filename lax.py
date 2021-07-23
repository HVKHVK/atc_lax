import vlc
import pygame
import sys
import time
import config as cfg

s1 = vlc.MediaPlayer(cfg.SOUTH_TOWER)
s2 = vlc.MediaPlayer(cfg.NORTH_TOWER)
s3 = vlc.MediaPlayer(cfg.SOUTH_GROUND)
s4 = vlc.MediaPlayer(cfg.NORTH_GROUND)
s5 = vlc.MediaPlayer(cfg.SOUTH_FINAL_APP)
s6 = vlc.MediaPlayer(cfg.NORTH_FINAL_APP)

pygame.font.init()
size = (400, 350)
screen = pygame.display.set_mode(size)

myfont = pygame.font.SysFont('Times New Romans', 30)
screen.blit(myfont.render('South Tower', False, (250, 250, 250)), (40, 40))
screen.blit(myfont.render('North Tower', False, (250, 250, 250)), (240, 40))
screen.blit(myfont.render('South Ground', False, (250, 250, 250)), (40, 140))
screen.blit(myfont.render('North Ground', False, (250, 250, 250)), (240, 140))
screen.blit(myfont.render('South App', False, (250, 250, 250)), (40, 240))
screen.blit(myfont.render('North App', False, (250, 250, 250)), (240, 240))
screen.blit(myfont.render('Off', False, (250, 250, 250)), (60, 80))
screen.blit(myfont.render('Off', False, (250, 250, 250)), (260, 80))
screen.blit(myfont.render('Off', False, (250, 250, 250)), (60, 180))
screen.blit(myfont.render('Off', False, (250, 250, 250)), (260, 180))
screen.blit(myfont.render('Off', False, (250, 250, 250)), (60, 280))
screen.blit(myfont.render('Off', False, (250, 250, 250)), (260, 280))
pygame.display.flip()

status = [False, False, False, False, False, False]

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(60, 60, 80, 80))
                if not status[0]:
                    s1.play()
                    time.sleep(1)
                    status[0] = True
                    screen.blit(myfont.render('On', False, (250, 0, 250)), (60, 80))
                else:
                    s1.stop()
                    status[0] = False
                    screen.blit(myfont.render('Off', False, (250, 250, 250)), (60, 80))
                pygame.display.flip()
            if event.key == pygame.K_y:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(260, 60, 260, 80))
                if not status[1]:
                    s2.play()
                    time.sleep(1)
                    status[1] = True
                    screen.blit(myfont.render('On', False, (250, 0, 250)), (260, 80))
                else:
                    s2.stop()
                    status[1] = False
                    screen.blit(myfont.render('Off', False, (250, 250, 250)), (260, 80))
                pygame.display.flip()
            if event.key == pygame.K_g:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(60, 170, 50, 20))
                if not status[2]:
                    s3.play()
                    time.sleep(1)
                    status[2] = True
                    screen.blit(myfont.render('On', False, (250, 0, 250)), (60, 180))
                else:
                    s3.stop()
                    status[2] = False
                    screen.blit(myfont.render('Off', False, (250, 250, 250)), (60, 180))
                pygame.display.flip()
            if event.key == pygame.K_h:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(260, 170, 50, 20))
                if not status[3]:
                    s4.play()
                    time.sleep(1)
                    status[3] = True
                    screen.blit(myfont.render('On', False, (250, 0, 250)), (260, 180))
                else:
                    s4.stop()
                    status[3] = False
                    screen.blit(myfont.render('Off', False, (250, 250, 250)), (260, 180))
                pygame.display.flip()
            if event.key == pygame.K_b:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(60, 270, 50, 20))
                if not status[4]:
                    s5.play()
                    time.sleep(1)
                    status[4] = True
                    screen.blit(myfont.render('On', False, (250, 0, 250)), (60, 280))
                else:
                    s5.stop()
                    status[4] = False
                    screen.blit(myfont.render('Off', False, (250, 250, 250)), (60, 280))
                pygame.display.flip()
            if event.key == pygame.K_n:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(260, 270, 50, 20))
                if not status[5]:
                    s6.play()
                    time.sleep(1)
                    status[5] = True
                    screen.blit(myfont.render('On', False, (250, 0, 250)), (260, 280))
                else:
                    s6.stop()
                    status[5] = False
                    screen.blit(myfont.render('Off', False, (250, 250, 250)), (260, 280))
                pygame.display.flip()
            if event.key == pygame.K_q:
                sys.exit(1)



