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

koordinaadid = []
for i in range(25):
    koordinaadid.append([100 + i*40,442 - i*12])


def täitmine():
    kast = pygame.Surface((150,230))
    kast = kast.convert()
    kast.fill((255,255,255))
    screen.blit(kast, (0,0))
    
def diees():
    diees = pygame.image.load('diees.png')
    screen.blit(diees, (250,20))

def bemoll():
    bemoll = pygame.image.load('bemoll.png')
    screen.blit(bemoll, (250,20))

def pole():
    pole = pygame.image.load('pole.png')
    screen.blit(pole, (250,20))

def bassivõti():
    bass = pygame.image.load('bass.jpg')
    screen.blit(bass, (50,20))

def viiulivõti():
    viiul = pygame.image.load('viiul.gif')
    screen.blit(viiul, (50,20))
    
def noodid(): #ja noodijoonestik
    for i in range(5):
        pygame.draw.line(screen, (0,0,0),(0,250 + i*24),(1200,250 + i*24))
    for i in range(25):
        pygame.draw.circle(screen, (0,0,0), (koordinaadid[i]), 12,2)
        if i % 2 == 0:
            pygame.draw.line(screen, (0,0,0), (60 + i*40, 442-i/2*24), (140 + i*40,442-i/2*24), 1)

def hiir():
    global võti, märk
    x=pygame.mouse.get_pos()[0]
    y=pygame.mouse.get_pos()[1]
    if x<=150 and y <=230:
        if võti == 1: #viiul
            täitmine()
            võti = 0
        else: #bass
            täitmine()
            võti = 1
    if x >= 250 and x <= 293 and y >= 20 and y <= 102:
        if märk == 0:
            märk = 1
        elif märk == 1:
            märk = 2
        else:
            märk = 0
    for i in range(25):
        if abs(x - (100+i*40))<=12:
            if abs(y - (442 - i*12))<=12:
                pygame.draw.circle(screen, (0,0,0), (koordinaadid[i]), 12,0)
                print(i)
                break
    return i

võti = 0
märk = 0
pole()
bassivõti()
noodid()
pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill([255,255,255])
            noodid()
            x = hiir() #kasuta et noot märgistada
    if võti == 1:
        viiulivõti()
    else:
        bassivõti()
    if märk == 0:
        pole()
    elif märk == 1:
        diees()
    else:
        bemoll()
    pygame.display.flip()
            
pygame.quit()           
