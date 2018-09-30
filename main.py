#coding:utf-8
import pygame,os
from pygame.locals import *

encour=True
tetx,tety=1200,900


sts=open("profil.nath","r").readlines()
pseudo          =sts[0][:-1]
argent          =int(sts[1][:-1])
totpartiesjoues =int(sts[2][:-1])
tottop1         =int(sts[3][:-1])
pselec          =int(sts[4][:-1])
aselec          =int(sts[5][:-1])
mselec          =int(sts[6][:-1])
record          =int(sts[7])
pmenu=1


ptpp=[0             ,1                  ,2                  ,3                  ,4                  ,5          ,6          ,7          ,8              ,9              ]
pnom=["Clyde"       ,"Linconu"          ,"Lesprideglace"    ,"Fantom"           ,"Le montagnard"    ,"Legro"    ,"Elector"  ,"Einstein" ,"La voyante"   ,"Le gangster"  ]
pvie=[1000          ,900                ,1500               ,600                ,1000               ,5000       ,1700       ,980        ,1500           ,1450           ]
pres=[10            ,35                 ,15                 ,0                  ,40                 ,150        ,40         ,20         ,5              ,10             ]
pvit=[15            ,25                 ,20                 ,20                 ,18                 ,5          ,19         ,15         ,23             ,24             ]
pimp=["p_1.png"     ,"p_2.png"          ,"p_3.png"          ,"p_4.png"          ,"p_5.png"          ,"p_6.png"  ,"p_7.png"  ,"p_8.png"  ,"p_9.png"      ,"p_10.png"     ]
pimm=["p_1.png"     ,"p_2.png"          ,"p_3.png"          ,"p_4.png"          ,"p_5.png"          ,"p_6.png"  ,"p_7.png"  ,"p_8.png"  ,"p_9.png"      ,"p_10.png"     ]
pcou=[0             ,1500               ,4000               ,6000               ,4500               ,8000       ,4999       ,1905       ,3000           ,4563           ]

atpp=[0             ,1           ,2             ,3              ,4              ,5          ,6                      ,7          ,8              ,9          ,10                 ,11         ]
anom=["pistolet"    ,"biochoc45" ,"arbalette"   ,"sniper"       ,"lanscoeur"    ,"bazooka"  ,"super-mitrailleuse"   ,"Tronelec" ,"lancepatate"  ,"l'arc"    ,"Le double bazooka","Trazor"   ]
attr=[0.4           ,1.3         ,2             ,4              ,2              ,3          ,0.09                   ,1          ,1.7            ,1.2        ,2.5                ,0.5        ]
abdg=[100           ,2000        ,1000          ,1010           ,500            ,1500       ,10                     ,999        ,3000           ,1111       ,1650               ,555        ]
aimp=["a_1.png"     ,"a_2.png"   ,"a_3.png"     ,"a_4.png"      ,"a_5.png"      ,"a_6.png"  ,"a_7.png"              ,"a_8.png"  ,"a_9.png"      ,"a_10.png" ,"a_11.png"         ,"a_12.png" ]
aimm=["a_1.png"     ,"a_2.png"   ,"a_3.png"     ,"a_4.png"      ,"a_5.png"      ,"a_6.png"  ,"a_7.png"              ,"a_8.png"  ,"a_9.png"      ,"a_10.png" ,"a_11.png"         ,"a_12.png" ]
acou=[0             ,10000       ,5000          ,3500           ,7000           ,9000       ,6500                   ,4001       ,7500           ,2560       ,45600              ,5654       ]

mtpp=[0             ,1              ,2                          ,3          ,4              ]
mnom=["poignard"    ,"sabre-laser"  ,"Le baton de Montagnard"   ,"Spelectr" ,"Tronconneuse" ]
mtat=[1             ,1              ,1.5                        ,1          ,1.2            ]
mdgg=[50            ,800            ,100                        ,999        ,800            ]
mprt=[30            ,60             ,45                         ,70         ,50             ]
mcou=[0             ,1000           ,6000                       ,4000       ,2500           ]
mimp=["m_1.png"     ,"m_2.png"      ,"m_3.png"                  ,"m_4.png"  ,"m_5.png"      ]
mimm=["m_1.png"     ,"m_2.png"      ,"m_3.png"                  ,"m_4.png"  ,"m_5.png"      ]

###################################""
pygame.init()
fenetre=pygame.display.set_mode((tetx,tety))



def save_profil():
    txt=str(pseudo)+"\n"+str(argent)+"\n"+str(totpartiesjoues)+"\n"+str(tottop1)+"\n"+str(pselec)+"\n"+str(aselec)+"\n"+str(mselec)+"\n"+str(record)
    f=open("profil.nath","w")
    f.write(txt)
    f.close()


def aff():
    button_menu1,button_menu2,button_menu3,button_play,b_record=pygame.Rect(1,1,1,1),pygame.Rect(1,1,1,1),pygame.Rect(1,1,1,1),pygame.Rect(1,1,1,1),pygame.Rect(1,1,1,1)
    fenetre.fill((0,0,100))
    font=pygame.font.SysFont("Sherif",20)
    fon2=pygame.font.SysFont("Sherif",30)
    pygame.draw.rect(fenetre,(0,0,0),(0,0,200,50)   ,1)
    pygame.draw.rect(fenetre,(0,0,0),(200,0,200,50) ,1)
    pygame.draw.rect(fenetre,(0,0,0),(400,0,200,50) ,1)
    pygame.draw.rect(fenetre,(0,0,0),(600,0,200,50) ,1)
    pygame.draw.rect(fenetre,(0,0,0),(800,0,200,50) ,1)
    pygame.draw.rect(fenetre,(0,0,0),(1000,0,200,50),1)
    fenetre.blit( font.render(pseudo               ,20 ,(250,250,250) ) , [50  ,10] )
    fenetre.blit( font.render(str(argent)          ,20 ,(250,250,250) ) , [250 ,10] )
    fenetre.blit( font.render(str(totpartiesjoues) ,20 ,(250,250,250) ) , [450 ,10] )
    fenetre.blit( font.render(str(tottop1)         ,20 ,(250,250,250) ) , [650 ,10] )
    fenetre.blit( font.render(pnom[pselec]         ,20 ,(250,250,250) ) , [850 ,10] )
    fenetre.blit( font.render(anom[aselec]         ,20 ,(250,250,250) ) , [1050,10] )
    
    button_menu3=pygame.draw.rect(fenetre,(0,0,0),(0   ,50,400,70),1)
    button_menu1=pygame.draw.rect(fenetre,(0,0,0),(400 ,50,400,70),1)
    button_menu2=pygame.draw.rect(fenetre,(0,0,0),(800 ,50,400,70),1)
    fenetre.blit( font.render("magasin"    ,20 ,(250,250,150) ) , [150 ,70] )
    fenetre.blit( font.render("home"       ,20 ,(250,250,150) ) , [550 ,70] )
    fenetre.blit( font.render("historique" ,20 ,(250,250,150) ) , [950,70] )
    
    lprs,lam1,lam2=[],[],[]
        
    if pmenu == 1: #menu principal
        pygame.draw.rect(fenetre,(100,0  ,0 ),(400     ,50      ,400,70 ),5)
        
        button_play=pygame.draw.rect(fenetre,(150,150,20),(tetx-500,tety-150,400,100),0)
        fenetre.blit( font.render( "PLAY" , 20 , (0,0,0) ) , [ tetx-450 , tety - 120 ] )
    
        fenetre.blit( pygame.transform.scale( pygame.image.load("images/"+pimp[pselec]) , [300,400]) , [50,150] )
        fenetre.blit( pygame.transform.scale(pygame.image.load("images/"+aimp[aselec]),[300,200]) , [50,600] )
        fenetre.blit( pygame.transform.scale(pygame.image.load("images/"+mimp[mselec]),[100,75]) , [450,800] )
        
        button_play=pygame.draw.rect(fenetre,(150,150,20),(tetx-500,tety-150,400,100),0)
        fenetre.blit( font.render( "PLAY" , 20 , (0,0,0) ) , [ tetx-450 , tety - 120 ] )
        
        fenetre.blit( fon2.render( "PERSONNAGE = "+pnom[pselec] , 20 , (250,250,250) ) , [ tetx-700 , tety - 520 ] )
        fenetre.blit( fon2.render( "ARME 1 = "+anom[aselec]     , 20 , (250,250,250) ) , [ tetx-700 , tety - 420 ] )
        fenetre.blit( fon2.render( "ARME 2 = "+mnom[mselec]     , 20 , (250,250,250) ) , [ tetx-700 , tety - 320 ] )
        
        
        if record: crc=(20,100,20)
        else     : crc=(100,20,20)
        b_record=pygame.draw.rect(fenetre,crc,(tetx-500,150,400,100),0)
        fenetre.blit( font.render( "RECORD" , 20 , (0,0,0) ) , [ tetx-450 , 170 ] )
    
    if pmenu == 2: #historique parties
        pygame.draw.rect(fenetre,(100,0  ,0 ),(800     ,50      ,400,70 ),5)
        try:
            hist=open("hist.nath","r").readlines()
            hist=hist[::-1]
            for h in hist:
                if len(h) < 5: del(hist[hist.index(h)])
            if len(hist) < 5 and len(hist) > 0: jkl=len(hist)
            else                              : jkl=5
            xx=50
            yy=200
            fenetre.blit( font.render("VOICI LES 5 DERNIERES PARTIES JOUEES :",20,(0,150,0)) , [450,150] )
            for x in range(jkl):
                rr=hist[x].split("|")
                pygame.draw.rect(fenetre,(200,200,200),(xx,yy,1000,100)   ,0)
                pygame.draw.rect(fenetre,(0,0,0)      ,(xx,yy,200,100)    ,3)
                pygame.draw.rect(fenetre,(0,0,0)      ,(xx+200,yy,200,100),3)
                pygame.draw.rect(fenetre,(0,0,0)      ,(xx+400,yy,200,100),3)
                pygame.draw.rect(fenetre,(0,0,0)      ,(xx+600,yy,200,100),3)
                pygame.draw.rect(fenetre,(0,0,0)      ,(xx+800,yy,200,100),3)
                fenetre.blit( font.render("TOP : "  +rr[0]                 ,20,(50,50,0)) , [xx+10 ,yy+40] )
                fenetre.blit( font.render("TUES : " +rr[1]                 ,20,(50,50,0)) , [xx+210,yy+40] )
                fenetre.blit( font.render("PERSO : "+pnom[int(rr[2]     )] ,20,(50,50,0)) , [xx+410,yy+40] )
                fenetre.blit( font.render("ARME1 : "+anom[int(rr[3]     )] ,20,(50,50,0)) , [xx+610,yy+40] )
                fenetre.blit( font.render("ARME2 : "+mnom[int(rr[4]     )] ,20,(50,50,0)) , [xx+810,yy+40] )
                yy+=120
        except:
            fenetre.blit( font.render("VOUS N'AVEZ PAS ENCOURE FAIT DE PARTIES",20,(50,0,0)) , [500,400] )
    if pmenu == 3:
        pygame.draw.rect(fenetre,(100,0  ,0 ),(0     ,50      ,400,70 ),5)        
        xx,yy=20,200
        cx,cy=70,70
        for x in ptpp:
            fenetre.blit( pygame.image.load("images/"+pimm[x]) , [xx,yy] )
            lprs.append( pygame.Rect(xx,yy,cx,cy))
            if x == pselec: pygame.draw.rect(fenetre,(200,0,100),(xx,yy,cx,cy),4)
            xx+=80
            if xx >= 260: xx,yy=20,yy+80
       
        xx,yy=520,200
        cx,cy=70,70
        for x in atpp:
            fenetre.blit( pygame.image.load("images/"+aimm[x]) , [xx,yy] )
            lam1.append( pygame.Rect(xx,yy,cx,cy) )
            if x == aselec: pygame.draw.rect(fenetre,(200,0,100),(xx,yy,cx,cy),4)
            xx+=80
            if xx >= 760: xx,yy=520,yy+80
    
        xx,yy=820,200
        cx,cy=70,70
        for x in mtpp:
            fenetre.blit( pygame.image.load("images/"+mimm[x]) , [xx,yy] )
            lam2.append( pygame.Rect(xx,yy,cx,cy) )
            if x == mselec: pygame.draw.rect(fenetre,(200,0,100),(xx,yy,cx,cy),4)
            xx+=80
            if xx >= 1060: xx,yy=820,yy+80

    pygame.display.update()
    return button_menu1,button_menu2,button_menu3,button_play,lprs,lam1,lam2,b_record

#button_play =pygame.Rect( tetx-500,tety-150,400,100 )
#button_menu1=pygame.Rect( 400     ,70      ,400,70  )
#button_menu2=pygame.Rect( 800     ,70      ,400,70  )

while encour:
    button_menu1,button_menu2,button_menu3,button_play,lprs,lam1,lam2,b_record=aff()
    for event in pygame.event.get():
        if   event.type == QUIT:
            exit()
        elif event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            rectpose=pygame.Rect(pos[0],pos[1],1,1)
            if   rectpose.colliderect(button_menu1): pmenu=1
            elif rectpose.colliderect(button_menu2): pmenu=2
            elif rectpose.colliderect(button_menu3): pmenu=3
            if pmenu == 1:
                if rectpose.colliderect(button_play) :
                    import subprocess
                    subprocess.Popen(["python","a.py"])
                    exit()
                elif rectpose.colliderect(b_record) :
                    if record: record=0
                    else     : record=1
            elif pmenu == 3:
                pp,aa,mm=0,0,0
                for p in lprs:
                    if rectpose.colliderect(p): pselec=lprs.index(p)
                for a in lam1:
                    if rectpose.colliderect(a): aselec=lam1.index(a)
                for m in lam2:
                    if rectpose.colliderect(m): mselec=lam2.index(m)
             
            save_profil()
        elif event.type == KEYDOWN:
            if event.key == K_q: exit()











