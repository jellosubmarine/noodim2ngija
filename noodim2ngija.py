import pygame
#HELI
pygame.mixer.init()
pygame.init()
pygame.mixer.music.set_volume(1.0)
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption('Noodimängija')
#taust
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))
screen.blit(background, (0, 0))
pygame.display.flip()

#pygame.mixer.music.load(noot + '.wav')
#pygame.mixer.music.play()
noodid = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']

#noodijoonestik
for i in range(5):
    pygame.draw.line(screen, (0,0,0),(0,250 + i*24),(800,250 + i*24))
pygame.display.flip()

def täitmine():
    kast = pygame.Surface((150,230))
    kast = kast.convert()
    kast.fill((255,255,255))
    screen.blit(kast, (0,0))
    pygame.display.flip()
def bassivõti():
    täitmine()
    bass = pygame.image.load('bass.jpg')
    screen.blit(bass, (50,20))
    pygame.display.flip()

def viiulivõti():
    täitmine()
    viiul = pygame.image.load('viiul.gif')
    screen.blit(viiul, (50,20))
    pygame.display.flip()

    
def noodid():
    for i in range(13):
        pygame.draw.circle(screen, (0,0,0), (100 + i*40,370 - i*12), 12,2)
    pygame.draw.line(screen, (0,0,0), (85, 370), (115,370), 1)
    pygame.draw.line(screen, (0,0,0), (85 + 12*40, 370-6*24), (115 + 12*40,370-6*24), 1)
    pygame.display.flip()
noodid()
pygame.mixer.music.load('F4.wav')
pygame.mixer.music.play()
viiulivõti()

pygame.time.wait(5000)
pygame.mixer.music.load('F2.wav')
pygame.mixer.music.play()
bassivõti()



"""def hiireklikk(xalg,yalg,x,y):
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            koht = pygame.mouse.get_pos()
            if koht"""

    
