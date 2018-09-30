#coding:utf-8
import pygame,sys
from pygame.locals import *

tetx,tety=1200,1000

fichier = sys.argv[1]

dcx,dcy=0,0

#################################################

def rem(f):
    mapeop,prs=[],[]
    l1=f.split("!")
    lmapeop =l1[0].split("{")
    lprs    =l1[1].split("{")
    for o in lmapeop:
        oo=o.split("|")
        fenetre.blit( pygame.image.load("images/"+oo[5]) ,[int(oo[3])+dcx,int(oo[4])+dcy] )
    for o in lprs:
        oo=o.split("|")
        if   oo[7] == "Up"   : angl = 0
        elif oo[7] == "Down" : angl = 180
        elif oo[7] == "Left" : angl = 90
        elif oo[7] == "Right": angl = -90
        fenetre.blit( pygame.image.transform( pygame.image.load("images/"+oo[6]) ,angl)    , [int(oo[3])+dcx,int(oo[4])+dcy] )
        fenetre.blit( pygame.image.transform( pygame.image.load("images/"+oo[5]) ,angl)    , [int(oo[3])+dcx,int(oo[4])+dcy] )
    oo=l1[2].split("|")
    if   oo[7] == "Up"   : angl = 0
    elif oo[7] == "Down" : angl = 180
    elif oo[7] == "Left" : angl = 90
    elif oo[7] == "Right": angl = -90
    fenetre.blit( pygame.image.transform( pygame.image.load("images/"+oo[6]) ,angl)    , [int(oo[3])+dcx,int(oo[4])+dcy] )
    fenetre.blit( pygame.image.transform( pygame.image.load("images/"+oo[5]) ,angl)    , [int(oo[3])+dcx,int(oo[4])+dcy] )
    pygame.display.update()

#################################################

pygame.init()
fenetre=pygame.display.set_mode([tetx,tety])
pygame.display.set_caption("replay TLBR")

frames=open("records/"+fichier,"r").readlines()

print len(frames)

for f in frames:
    rem( f[:-1] )
    for event in pygame.event.get():
        if event.type == QUIT   : exit()
        if event.type == KEYDOWN:
            if event.key == K_q : exit()
    time.sleep(0.5)





