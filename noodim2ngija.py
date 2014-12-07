import pygame
#Madis Kaspar Nigol
#HELI
pygame.mixer.init()
pygame.init()
pygame.mixer.music.set_volume(1.0)
screen = pygame.display.set_mode([1200,800])
pygame.display.set_caption('Noodimängija')
#taust
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))
screen.blit(background, (0, 0))
pygame.display.flip()

#pygame.mixer.music.load(noot + '.wav')
#pygame.mixer.music.play()
kõik_noodid = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
viiulinoodid = ['D3', 'Eb3', 'E3', 'F3', 'Gb3', 'G3', 'Ab3', 'A3', 'Bb3', 'B3', 'C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4', 'C5', 'Db5', 'D5', 'Eb5', 'E5', 'F5', 'Gb5', 'G5', 'Ab5', 'A5', 'Bb5', 'B5', 'C6', 'Db6', 'D6', 'Eb6', 'E6', 'F6', 'Gb6', 'G6']
bassinoodid = ['F1', 'Gb1', 'G1', 'Ab1', 'A1', 'Bb1', 'B1', 'C2', 'Db2', 'D2', 'Eb2', 'E2', 'F2', 'Gb2', 'G2', 'Ab2', 'A2', 'Bb2', 'B2', 'C3', 'Db3', 'D3', 'Eb3', 'E3', 'F3', 'Gb3', 'G3', 'Ab3', 'A3', 'Bb3', 'B3', 'C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4']
#noodijoonestik
for i in range(5):
    pygame.draw.line(screen, (0,0,0),(0,250 + i*24),(1200,250 + i*24))
pygame.display.flip()

koordinaadid = []
for i in range(25):
    koordinaadid.append([100 + i*40,442 - i*12])


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
    for i in range(25):
        pygame.draw.circle(screen, (0,0,0), (koordinaadid[i]), 12,2)
        if i % 2 == 0:
            pygame.draw.line(screen, (0,0,0), (60 + i*40, 442-i/2*24), (140 + i*40,442-i/2*24), 1)
    pygame.display.flip()

def täida():
    x=pygame.mouse.get_pos()[0]
    y=pygame.mouse.get_pos()[1]
    
noodid()
"""pygame.mixer.music.load('F4.wav')
pygame.mixer.music.play()
viiulivõti()

pygame.time.wait(5000)
pygame.mixer.music.load('F2.wav')
pygame.mixer.music.play()
bassivõti()"""



"""def hiireklikk(xalg,yalg,x,y):
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            koht = pygame.mouse.get_pos()
            if koht"""

    
