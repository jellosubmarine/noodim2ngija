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
    pygame.draw.line(screen, (0,0,0),(0,250 + i*25),(800,250 + i*25))
pygame.display.flip()

def täitmine():
    kast = pygame.Surface((230,150))
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


    
