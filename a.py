#coding:utf-8
import pygame,random,time,math,os
from pygame.locals import *

#####################################################################################################################################

fps=40

tetx,tety=1300,1000

nbprs=50
tmx,tmy=40*100,40*100

affcarte=True
affstats=True

encour=True

mape=[]
mapeop=[]
prs=[]
blts=[]

imgsp1=["p_1_up1.png","p_1_up2.png","p_1_up3.png"]
imgsp2=["p_2_up1.png","p_2_up2.png","p_2_up3.png"]
imgsp3=["p_3_up1.png","p_3_up2.png","p_3_up3.png"]
imgsp4=["p_4_up1.png","p_4_up2.png","p_4_up3.png"]
imgsp5=["p_5_up1.png","p_5_up2.png","p_5_up3.png"]
imgsp6=["p_6_up1.png","p_6_up2.png","p_6_up3.png"]
imgsp7=["p_7_up1.png","p_7_up2.png","p_7_up3.png"]
imgsp8=["p_8_up1.png","p_8_up2.png","p_8_up3.png"]
imgsp9=["p_9_up1.png","p_9_up2.png","p_9_up3.png"]
imgsp10=["p_10_up1.png","p_10_up2.png","p_10_up3.png"]
imgsa1=["a_1_up1.png","a_1_up2.png"]
imgsa2=["a_2_up1.png","a_2_up2.png"]
imgsa3=["a_3_up1.png","a_3_up2.png"]
imgsa4=["a_4_up1.png","a_4_up2.png"]
imgsa5=["a_5_up1.png","a_5_up2.png"]
imgsa6=["a_6_up1.png","a_6_up2.png"]
imgsa7=["a_7_up1.png","a_7_up2.png"]
imgsa8=["a_8_up1.png","a_8_up2.png"]
imgsa9=["a_9_up1.png","a_9_up2.png"]
imgsa10=["a_10_up1.png","a_10_up2.png"]
imgsa11=["a_11_up1.png","a_11_up2.png"]
imgsa12=["a_12_up1.png","a_12_up2.png"]
imgss1=["m_1_up1.png","m_1_up2.png"]
imgss2=["m_2_up1.png","m_2_up2.png"]
imgss3=["m_3_up1.png","m_3_up2.png"]
imgss4=["m_4_up4.png","m_4_up4.png"]
imgss5=["m_5_up4.png","m_5_up4.png"]

anbal1=["bal1.png","bal2.png","bal3.png","bal4.png"]
animband=["anim_b1.png","anim_b2.png","anim_b1.png","anim_b3.png" ]
animtron=["m_5_up1.png","m_5_up2.png","m_5_up3.png"               ]
animepee=["m_4_up1.png","m_4_up2.png","m_4_up3.png"               ]
anicap  =["cape_1.png" ,"cape_2.png" ,"cape_3.png","cape_2.png"   ]
animbio =["nucl_1.png" ,"nucl_2.png" ,"nucl_3.png","nucl_2.png"   ]
animelct=["elct_1.png" ,"elct_2.png" ,"elct_3.png","elct_4.png"   ]
animcpel=["cpel_1.png" ,"cpel_2.png" ,"cpel_3.png"                ]
animce  =["ce1.png"    ,"ce2.png"    ,"ce3.png"   ,"ce2.png"      ]
animvche=["vche1.png"  ,"vche2.png"  ,"vche3.png" ,"vche2.png"    ]

ptpp=[0         ,1          ,2              ,3          ,4              ,5      ,6          ,7          ,8              ,9              ]
pnom=["Clyde"   ,"Linconu"  ,"Lesprideglace","Fantom"   ,"Le montagnard","Legro","Elector"  ,"Einstein" ,"La Voyante"   ,"Le gangster"  ]
pvie=[1000      ,900        ,1500           ,600        ,1000           ,5000   ,1700       ,980        ,1500           ,1450           ]
pres=[10        ,35         ,15             ,0          ,40             ,150    ,40         ,21         ,5              ,10             ]
pvit=[15        ,25         ,20             ,20         ,18             ,6      ,19         ,15         ,23             ,24             ]
pimg=[imgsp1    ,imgsp2     ,imgsp3         ,imgsp4     ,imgsp5         ,imgsp6 ,imgsp7     ,imgsp8     ,imgsp9         ,imgsp10        ]
ptxx=[50        ,50         ,50             ,50         ,50             ,50     ,50         ,50         ,50             ,50             ]
ptyy=[50        ,50         ,50             ,50         ,50             ,50     ,50         ,50         ,50             ,50             ]
pnim=[[]        ,[]         ,[]             ,[]         ,anicap         ,[]     ,animcpel   ,animce     ,animvche       ,animband       ]

atpp=[0             ,1          ,2              ,3              ,4              ,5              ,6                      ,7          ,8              ,9              ,10                 ,11         ]
anom=["pistolet"    ,"biochoc45","arbalette"    ,"sniper"       ,"lanscoeur"    ,"bazooka"      ,"super mitrailleuse"   ,"tronelec" ,"lancepatate"  ,"l'arc"        ,"Le double bazooka","Trazor"   ]
attr=[0.4           ,1.7        ,2              ,4              ,2              ,3              ,0                      ,1          ,1.7            ,1.2            ,2.5                ,0.5        ]
abcl=[(20,20,20)    ,(10,250,10),(0,0,0)        ,(10,10,110)    ,(0,0,0)        ,(0,0,0)        ,(40,40,40)             ,(0,0,0)    ,(0,0,0)        ,(0,0,0)        ,(121,154,21)       ,(210,15,15)]
abce=[(200,250,50)  ,(50,90,140),(250,0,0)      ,(200,250,50)   ,(250,20,60)    ,(200,250,50)   ,(200,250,50)           ,(0,50,250) ,(150,160,20)   ,(150,0,0)      ,(121,154,21)       ,(210,15,15)]
abte=[6             ,150        ,4              ,4              ,30             ,120            ,5                      ,75         ,99             ,4              ,150                ,55         ]
abvt=[15            ,30         ,45             ,40             ,30             ,30             ,40                     ,20         ,20             ,50             ,30                 ,55         ]
abfr=[2             ,1          ,1              ,2              ,2              ,2              ,2                      ,1          ,1              ,1              ,1                  ,1          ]
abdg=[100           ,2000       ,1000           ,2200           ,500            ,1600           ,50                     ,999        ,3000           ,1111           ,1650               ,555        ]
abtx=[6             ,30         ,10             ,4              ,11             ,30             ,3                      ,20         ,25             ,10             ,30                 ,15         ]
abty=[5             ,50         ,5              ,3              ,9              ,20             ,3                      ,20         ,25             ,5              ,20                 ,15         ]
abds=[500           ,800        ,1500           ,2000           ,650            ,400            ,1400                   ,2000       ,150            ,3000           ,400                ,555        ]
abtp=[1             ,3          ,2              ,1              ,2              ,2              ,1                      ,3          ,2              ,2              ,2                  ,3          ]
abim=["rien.png"    ,"rien.png" ,"fleche.png"   ,"rien.png"     ,"coeur.png"    ,"roquette.png" ,"rien.png"             ,"rien.png" ,"patate.png"   ,"fleche.png"   ,"roquette.png"     ,"rien.png" ]
anim=[[]            ,animbio    ,[]             ,[]             ,[]             ,[]             ,[]                     ,animelct   ,[]             ,[]             ,[]                 ,anbal1     ]
aimg=[imgsa1        ,imgsa2     ,imgsa3         ,imgsa4         ,imgsa5         ,imgsa6         ,imgsa7                 ,imgsa8     ,imgsa9         ,imgsa10        ,imgsa11            ,imgsa12    ]
atxx=[50            ,50         ,50             ,50             ,50             ,50             ,50                     ,50         ,50             ,50             ,50                 ,50         ]
atyy=[50            ,50         ,50             ,50             ,50             ,50             ,50                     ,50         ,50             ,50             ,50                 ,50         ]
#forme 1 = rectangulaire , forme 2 = rond

stpp=[0         ,1              ,2                      ,3          ,4              ]
snom=["poignard","sabre laser"  ,"baton de montagnard"  ,"Spelectr" ,"Tronsonneuse" ]
sttr=[0.5       ,0.5            ,0.7                    ,0.8        ,1.2            ]
simg=[imgss1    ,imgss2         ,imgss3                 ,imgss4     ,imgss5         ]
snim=[[]        ,[]             ,[]                     ,animepee   ,animtron       ]
sdeg=[400       ,800            ,100                    ,999        ,800            ]
sprt=[30        ,55             ,45                     ,70         ,50             ]
stxx=[50        ,50             ,50                     ,50         ,50             ]
styy=[50        ,50             ,50                     ,50         ,50             ]
stpt=[1         ,1              ,1                      ,2          ,2              ]


mtpp=[0            ,1                                   ]
mnom=["herbe"      ,"arbre"                             ]
mtxx=[100          ,50                                  ]
mtyy=[100          ,50                                  ]
mpmd=[True         ,False                               ]
mimg=[["herbe.png"],["arbre_1_1.png","arbre_1_2.png"]   ]

#####################################################################################################################################

def cabre(ss):
    global mape
    ata=True
    if ss.pos.tp == 7 and ss.px > -tmx and ss.px < tmx and ss.py > -tmy and ss.py < tmy:
      for m in mapeop:
        if pygame.Rect(ss.px,ss.py,mtxx[1],mtyy[1]).colliderect( pygame.Rect(m.px,m.py,m.tx,m.ty) ): ata = False
      if  ata : mapeop.append( Om(ss.px,ss.py,1) )


def vt(p):
    if p.px < 0-tmx/2: return True
    if p.px > tmx/2  : return True
    if p.py < 0-tmy/2: return True
    if p.py > tmy/2  : return True
    for m in mapeop:
        if pygame.Rect(m.fx,m.fy,m.tx,m.ty).colliderect( pygame.Rect(p.fx,p.fy,p.tx,p.ty) ) and p.tp != 3: return True
    return False

def bm(dd):
    for o in mape:
        o.fx+=dd[0]
        o.fy+=dd[1]
    for o in mapeop:
        o.fx+=dd[0]
        o.fy+=dd[1]
    for o in prs:
        o.fx+=dd[0]
        o.fy+=dd[1]
    for o in blts:
        o.fx+=dd[0]
        o.fy+=dd[1]

class Om():
    def __init__(self,x,y,tp):
        self.nom     = mnom[tp]
        self.tp      = tp
        self.px      = x
        self.py      = y
        self.fx      = x
        self.fy      = y
        self.tx      = mtxx[tp]
        self.ty      = mtyy[tp]
        self.imgs    = mimg[tp]
        self.i       = 0
        self.imgactu = self.imgs[self.i]
        self.img     = pygame.image.load("images/"+self.imgactu)
        self.pmd     = mpmd[tp]
    def anim(self):
        if self.i >= len(self.imgs)-1:
            self.i=0
        else: self.i+=1
        if self.imgs.index( self.imgactu ) != self.i:
            self.imgactu=self.imgs[self.i]
            self.img    =pygame.image.load("images/"+self.imgactu)

def explose(bb,prs,mapeop):
    cabre(bb)
    if bb.fx+bb.te >= 0 and bb.fx - bb.te <= tetx and bb.fy + bb.ty >= 0 and bb.fy - bb.ty <= tety:
        pygame.draw.circle(fenetre,bb.ce,(bb.fx,bb.fy),bb.te,0)
    re=pygame.Rect(bb.fx-bb.te,bb.fy-bb.te,bb.te*2,bb.te*2)
    for p in prs:
        if re.colliderect( pygame.Rect(p.fx,p.fy,p.tx,p.ty) ):
          if p.tp != 3:
            #a1=abs(bb.fy-p.fy)
            #a2=abs(bb.fx-p.fx)
            #a3=math.sqrt(a1*a1+a2*a2)
            #p.vie-=int(float(a3)/float(bb.te)*float(bb.dg))
            if bb.dg-p.resist > 0 : p.vie -= bb.dg-p.resist
            if bb.fx+bb.te >= 0 and bb.fx - bb.te <= tetx and bb.fy + bb.ty >= 0 and bb.fy - bb.ty <= tety: pygame.draw.rect(fenetre,(100,0,10),(p.fx,p.fy,5,5),0)
            if p.vie <= 0:
                del(prs[prs.index(p)])
                bb.pos.tues+=1
          else:
            a=random.randint(0,100)
            if a <= 30:
                if bb.dg-p.resist > 0 : p.vie -= bb.dg-p.resist
                if bb.fx+bb.te >= 0 and bb.fx - bb.te <= tetx and bb.fy + bb.ty >= 0 and bb.fy - bb.ty <= tety: pygame.draw.rect(fenetre,(100,0,10),(p.fx,p.fy,5,5),0)
                if p.vie <= 0:
                    del(prs[prs.index(p)])
                    bb.pos.tues+=1
    if re.colliderect( pygame.Rect(perso.fx,perso.fy,perso.tx,perso.ty) ):
        if perso.tp != 3:
            #a1=abs(bb.fy-perso.fy)
            #a2=abs(bb.fx-perso.fx)
            #a3=math.sqrt(a1*a1+a2*a2)
            #p.vie-=int(float(a3)/float(bb.te)*float(bb.dg))
            if bb.dg-perso.resist > 0 : perso.vie -= bb.dg-perso.resist
            if bb.fx+bb.te >= 0 and bb.fx - bb.te <= tetx and bb.fy + bb.ty >= 0 and bb.fy - bb.ty <= tety: pygame.draw.rect(fenetre,(100,0,10),(perso.fx,perso.fy,5,5),0)
            if perso.vie <= 0:
                encour=False
                bb.pos.tues+=1
        else:
          try:
            random.randint(0,100)
            if a <= 30:
                if bb.dg-perso.resist > 0 : perso.vie -= bb.dg-perso.resist
                if bb.fx+bb.te >= 0 and bb.fx - bb.te <= tetx and bb.fy + bb.ty >= 0 and bb.fy - bb.ty <= tety: pygame.draw.rect(fenetre,(100,0,10),(perso.fx,perso.fy,5,5),0)
                if perso.vie <= 0:
                    encour=False
                    bb.pos.tues+=1
          except: pass
    pygame.display.update()            


class Bullet:
    def __init__(self,x,y,tx,ty,cl,vit,dg,frm,dist,ce,te,pos,tpp,im,anim,i):
        self.px     = x
        self.py     = y
        self.fx     = x
        self.fy     = y
        self.tx     = tx
        self.ty     = ty
        self.cl     = cl
        self.vit    = vit
        self.dg     = dg
        self.forme  = frm
        self.dist   = dist
        self.ce     = ce
        self.te     = te
        self.pos    = pos
        self.tpp    = tpp
        self.img    = im
        self.ianim  = 0
        self.imganim= anim
        self.i      = i

    def bouger(self):
      try:
        self.px+=self.vit[0]
        self.py+=self.vit[1]
        self.fx+=self.vit[0]
        self.fy+=self.vit[1]
        self.dist-=abs(self.vit[0])+abs(self.vit[1])
        if self.dist <= 0:
            explose(self,prs,mapeop)
            #try   :
            del(blts[blts.index(self)])
            #except: error=True
      except: pass

    def detect(self):
        lprs=[]
        for p in prs:
          try:
            pp=10
            if pygame.Rect(self.fx,self.fy,self.tx,self.ty).colliderect( pygame.Rect(p.fx-pp,p.fy-pp,p.tx+pp,p.ty+pp) ):
              cabre(self)
              if p.resist > 0:  p.resist-=3
              if p.tp != 3:
                if self.pos.tp == 2:
                    p.vit-=2
                    p.arme.ttirer+=0.2
                if self.dg-p.resist > 0 : p.vie-=self.dg-p.resist
                if p.vie <= 0:
                    del(prs[prs.index(p)])
                    self.pos.tues+=1
                pygame.draw.circle(fenetre,self.ce,(self.fx,self.fy), self.te ,0)
                pygame.display.update()
                try   : del(blts[blts.index(self)])
                except: errorblts=True
              else:
                a=random.randint(0,100)
                p.vie-=self.dg
                if p.vie <= 0:
                    del(prs[prs.index(p)])
                    self.pos.tues+=1
                pygame.draw.circle(fenetre,self.ce,(self.fx,self.fy), self.te ,0)
                pygame.display.update()
                try   : del(blts[blts.index(self)])
                except: errorblts=True
                
          except: error=True
        try:
          if pygame.Rect(self.fx,self.fy,self.tx,self.ty).colliderect( pygame.Rect(perso.fx-pp,perso.fy-pp,perso.tx+pp,perso.ty+pp) ):
            cabre(self)
            if perso.resist > 0:  perso.resist-=3
            if perso.tp != 3:
                if self.dg-perso.resist > 0 :
                    perso.vie-=self.dg-perso.resist
                if perso.vie <= 0:
                    encour=False
                    self.pos.tues+=1
                pygame.draw.circle(fenetre,self.ce,(self.fx,self.fy), self.te ,0)
                pygame.display.update()
                try   : del(blts[blts.index(self)])
                except: error=True
            else:
                a=random.randint(0,200)
                print(a,)
                if a <= 30:
                    print(a)
                    perso.vie -= self.dg
                    if perso.vie <= 0:
                        encour=False
                        self.pos.tues+=1
                    pygame.draw.circle(fenetre,self.ce,(self.fx,self.fy), self.te ,0)
                    pygame.display.update()
                    try   : del(blts[blts.index(self)])
                    except: error=True
                print()
        except: error = True

class Arme:
    def __init__(self,x,y,tp,pos):
        self.tp         =tp
        self.nom        =anom[tp]
        self.blargeur   =abtx[tp]
        self.blongueur  =abty[tp]
        self.abtx       =abtx[tp]
        self.abty       =abty[tp]
        self.bcl        =abcl[tp]
        self.bvit       =abvt[tp]
        self.bdg        =abdg[tp]
        if pos == 6 and self.tp == 7: self.bdg += 100
        if pos == 9 and self.tp == 0: self.bdg=int(self.bdg*2.5)
        self.bfrm       =abfr[tp]
        self.bdist      =abds[tp]
        self.bclecl     =abce[tp]
        self.bte        =abte[tp]
        self.abtp       =abtp[tp]
        self.bim        =abim[tp]
        self.imgs       =aimg[tp]
        self.banim      =anim[tp]
        self.ttirer     =attr[tp]
        self.dtirer     =time.time()
        self.px,self.py =x,y
        self.i          =0
        self.img        =pygame.image.load("images/"+self.imgs[0])
        self.sens       ="Up"
        self.pos        =pos
        self.tx,self.ty =atxx[tp],atyy[tp]

    def tirer(self):
      if time.time() - self.dtirer >= self.ttirer and self.dtirer >= 0.1:
        self.dtirer=time.time()
        if self.tp != 4 and self.tp != 10 and self.tp != 11:
            if   self.sens == "Up"   :
                blts.append( Bullet( self.pos.fx+self.pos.tx/2-5          , self.pos.fy-self.abty-5                 , self.blargeur  , self.blongueur , self.bcl , [0,-self.bvit] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),0)    , self.banim , 0   ))
                xyz=0
            elif self.sens == "Down" :
                blts.append( Bullet( self.pos.fx+self.pos.tx/2+5          , self.pos.fy+self.pos.ty+self.abty+5     , self.blargeur  , self.blongueur , self.bcl , [0,self.bvit ] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),180)  , self.banim , 180 ))
                xyz=180
            elif self.sens == "Left" :
                blts.append( Bullet( self.pos.fx-self.abtx-25             , self.pos.fy+self.pos.ty/2-5             , self.blongueur , self.blargeur  , self.bcl , [-self.bvit,0] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),90)   , self.banim , 90  ))
                xyz=90
            elif self.sens == "Right":
                blts.append( Bullet( self.pos.fx+self.pos.tx+self.abtx+5  , self.pos.fy+self.pos.ty/2+5             , self.blongueur , self.blargeur  , self.bcl , [self.bvit,0 ] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),-90)  , self.banim ,- 90 ))
                xyz=-90
        elif self.tp == 4:
            blts.append( Bullet( self.pos.fx+self.pos.tx/2-5          , self.pos.fy-self.abty-5                 , self.blargeur  , self.blongueur , self.bcl , [0,-self.bvit] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate( pygame.image.load("images/"+self.bim) , 0  ) , self.banim ,0   ))
            blts.append( Bullet( self.pos.fx+self.pos.tx/2+5          , self.pos.fy+self.pos.ty+self.abty+5     , self.blargeur  , self.blongueur , self.bcl , [0,self.bvit ] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate( pygame.image.load("images/"+self.bim) , 180) , self.banim ,180 ))
            blts.append( Bullet( self.pos.fx-self.abtx-25             , self.pos.fy+self.pos.ty/2-5             , self.blongueur , self.blargeur  , self.bcl , [-self.bvit,0] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate( pygame.image.load("images/"+self.bim) , 90 ) , self.banim ,90  ))
            blts.append( Bullet( self.pos.fx+self.pos.tx+self.abtx+5  , self.pos.fy+self.pos.ty/2+5             , self.blongueur , self.blargeur  , self.bcl , [self.bvit,0 ] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate( pygame.image.load("images/"+self.bim) , -90) , self.banim ,-90 ))
            if   self.sens=="Up"   : xyz=0
            elif self.sens=="Down" : xyz=180
            elif self.sens=="Left" : xyz=90
            elif self.sens=="Right": xyz=-90
        elif self.tp == 10:
            if self.sens == "Up"   :
                blts.append( Bullet( self.pos.fx+self.pos.tx/2-10          , self.pos.fy-self.abty-5                 , self.blargeur  , self.blongueur , self.bcl , [0,-self.bvit] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),0)    , self.banim , 0   ))
                blts.append( Bullet( self.pos.fx+self.pos.tx/2+10          , self.pos.fy-self.abty-5                 , self.blargeur  , self.blongueur , self.bcl , [0,-self.bvit] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),0)    , self.banim , 0   ))
                xyz=0
            elif self.sens == "Down" :
                blts.append( Bullet( self.pos.fx+self.pos.tx/2+10          , self.pos.fy+self.pos.ty+self.abty+5     , self.blargeur  , self.blongueur , self.bcl , [0,self.bvit ] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),180)  , self.banim , 180 ))
                blts.append( Bullet( self.pos.fx+self.pos.tx/2-10          , self.pos.fy+self.pos.ty+self.abty+5     , self.blargeur  , self.blongueur , self.bcl , [0,self.bvit ] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),180)  , self.banim , 180 ))
                xyz=180
            elif self.sens == "Left" :
                blts.append( Bullet( self.pos.fx-self.abtx-25             , self.pos.fy+self.pos.ty/2-10             , self.blongueur , self.blargeur  , self.bcl , [-self.bvit,0] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),90)   , self.banim , 90  ))
                blts.append( Bullet( self.pos.fx-self.abtx-25             , self.pos.fy+self.pos.ty/2+10             , self.blongueur , self.blargeur  , self.bcl , [-self.bvit,0] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),90)   , self.banim , 90  ))
                xyz=90
            elif self.sens == "Right":
                blts.append( Bullet( self.pos.fx+self.pos.tx+self.abtx+5  , self.pos.fy+self.pos.ty/2+10             , self.blongueur , self.blargeur  , self.bcl , [self.bvit,0 ] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),-90)  , self.banim ,- 90 ))
                blts.append( Bullet( self.pos.fx+self.pos.tx+self.abtx+5  , self.pos.fy+self.pos.ty/2-10             , self.blongueur , self.blargeur  , self.bcl , [self.bvit,0 ] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),-90)  , self.banim ,- 90 ))
                xyz=-90
        elif self.tp == 11:
            if   self.sens == "Up"   :
                blts.append( Bullet( self.pos.fx+self.pos.tx/2-5          , self.pos.fy-self.abty-5                 , self.blargeur  , self.blongueur , self.bcl , [-15,-self.bvit-15] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),-15)  , self.banim , -15 ))
                blts.append( Bullet( self.pos.fx+self.pos.tx/2            , self.pos.fy-self.abty-5                 , self.blargeur  , self.blongueur , self.bcl , [0,-self.bvit] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),0)    , self.banim , 0   ))
                blts.append( Bullet( self.pos.fx+self.pos.tx/2-5          , self.pos.fy-self.abty-5                 , self.blargeur  , self.blongueur , self.bcl , [15,-self.bvit+15] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),+15)  , self.banim , +15 ))
                xyz=0
            elif self.sens == "Down" :
                blts.append( Bullet( self.pos.fx+self.pos.tx/2-5          , self.pos.fy+self.pos.ty+self.abty+5     , self.blargeur  , self.blongueur , self.bcl , [-15,self.bvit-15 ] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),180-15)  , self.banim , 180-15 ))
                blts.append( Bullet( self.pos.fx+self.pos.tx/2          , self.pos.fy+self.pos.ty+self.abty+5     , self.blargeur  , self.blongueur , self.bcl   , [0,self.bvit ] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),180)  , self.banim , 180 ))
                blts.append( Bullet( self.pos.fx+self.pos.tx/2+5          , self.pos.fy+self.pos.ty+self.abty+5     , self.blargeur  , self.blongueur , self.bcl , [15,self.bvit+15 ] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),180+15)  , self.banim , 180+15 ))
                xyz=180
            elif self.sens == "Left" :
                blts.append( Bullet( self.pos.fx-self.abtx-25             , self.pos.fy+self.pos.ty/2-5             , self.blongueur , self.blargeur  , self.bcl , [-self.bvit-15,-15] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),90)   , self.banim , 90  ))
                blts.append( Bullet( self.pos.fx-self.abtx-25             , self.pos.fy+self.pos.ty/2             , self.blongueur , self.blargeur  , self.bcl , [-self.bvit,0] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),90)   , self.banim , 90  ))
                blts.append( Bullet( self.pos.fx-self.abtx-25             , self.pos.fy+self.pos.ty/2+5             , self.blongueur , self.blargeur  , self.bcl , [-self.bvit+15,15] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),90)   , self.banim , 90  ))
                xyz=90
            elif self.sens == "Right":
                blts.append( Bullet( self.pos.fx+self.pos.tx+self.abtx+5  , self.pos.fy+self.pos.ty/2-5             , self.blongueur , self.blargeur  , self.bcl , [self.bvit-15,-15 ] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),-90)  , self.banim ,- 90 ))
                blts.append( Bullet( self.pos.fx+self.pos.tx+self.abtx+5  , self.pos.fy+self.pos.ty/2             , self.blongueur , self.blargeur  , self.bcl , [self.bvit,0 ] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),-90)  , self.banim ,- 90 ))
                blts.append( Bullet( self.pos.fx+self.pos.tx+self.abtx+5  , self.pos.fy+self.pos.ty/2+5             , self.blongueur , self.blargeur  , self.bcl , [self.bvit+15,15 ] , self.bdg ,self.bfrm , self.bdist , self.bclecl , self.bte , self.pos , self.abtp , pygame.transform.rotate(pygame.image.load("images/"+self.bim),-90)  , self.banim ,- 90 ))
                xyz=-90
        fenetre.blit( pygame.transform.rotate( pygame.image.load("images/"+self.imgs[1]),xyz),[self.pos.fx,self.pos.fy] )
        pygame.display.update()

class Melee:
    def __init__(self,pos,tp):
        self.tp     =tp
        self.nom    = snom[tp]
        self.dg     = sdeg[tp]
        if pos == 6 and self.tp == 3: self.dg += 100
        self.ttr    = sttr[tp]
        self.imgs   = simg[tp]
        self.prt    = sprt[tp]
        self.imganim= snim[tp]
        self.ianim  = 0        
        self.img    = pygame.image.load("images/"+self.imgs[0])
        self.pos    = pos
        self.da     = time.time()
        self.tpt    = stpt[tp]
    
    def att(self):
      if time.time()-self.da >= self.ttr:
        self.da=time.time()
        for p in prs:
            if p != self.pos:
                if pygame.Rect(self.pos.px-self.prt,self.pos.py-self.prt,self.pos.tx+self.prt,self.pos.ty+self.prt).colliderect( pygame.Rect(p.px,p.py,p.tx,p.ty) ) and self.pos != p:
                  if p.tp != 5 and 3:
                    if self.tp == 2 and self.pos.tp == 4:
                        p.vit = int(float(p.vit)/1.4)
                    p.vie-=self.dg
                    if p.vie <= 0:
                        self.pos.tues+=1
                        del( prs[prs.index(p)] )
                  elif p.tp == 5:
                    if self.dg-p.resist > 0: p.vie-=self.dg-p.resist
                    if p.vie <= 0:
                        self.pos.tues+=1
                        del( prs[prs.index(p)] )
                  elif p.tp == 3:
                    a=random.randint(0,100)
                    if a <= 30:
                        p.vie-=self.dg
                        if p.vie <= 0:
                            self.pos.tues+=1
                            del( prs[prs.index(p)] )
        if pygame.Rect(self.pos.px-self.prt,self.pos.py-self.prt,self.pos.tx+self.prt,self.pos.ty+self.prt).colliderect( pygame.Rect(perso.px,perso.py,perso.tx,perso.ty) ) and self.pos != perso:
          try:
            if perso.tp != 5 and 3:
                    perso.vie-=self.dg
                    if perso.vie <= 0:
                        self.pos.tues+=1
                        del( prs[prs.index(perso)] )
            elif perso.tp == 5:
                    if self.dg-perso.resist > 0: perso.vie-=self.dg-perso.resist
                    if perso.vie <= 0:
                        self.pos.tues+=1
                        del( prs[prs.index(perso)] )
            elif perso.tp == 3:
                    a=random.randint(0,100)
                    if a <= 30:
                        perso.vie-=self.dg
                        if perso.vie <= 0:
                            self.pos.tues+=1
                            del( prs[prs.index(perso)] )
          except: print("error 1")
        if   self.pos.sens == "Up"   : angl=0
        elif self.pos.sens == "Down" : angl=180
        elif self.pos.sens == "Left" : angl=90
        elif self.pos.sens == "Right": angl=-90
        fenetre.blit( pygame.transform.rotate( pygame.image.load("images/"+self.pos.imgs[2]) , angl ) , [self.pos.fx,self.pos.fy] )
        fenetre.blit( pygame.transform.rotate( pygame.image.load("images/"+self.imgs[1])     , angl ) , [self.pos.fx,self.pos.fy] )
        pygame.display.update()

class Perso:
    def __init__(self,x,y,tp,bop,arm):
        self.tp     = tp
        self.nom    = pnom[tp]
        self.vie    = pvie[tp]
        self.vietot = self.vie
        self.resist = pres[tp]
        self.vit    = pvit[tp]
        self.imgs   = pimg[tp]
        self.i      = 4
        self.img    = pygame.image.load("images/"+self.imgs[0])
        # imgs : 0 = haut1 , 1 = bas1 , 2 = gauche1 , 3 = droite1 , 4 = haut2 , 5 = bas2 , 6 = gauche2 , 7 = droite2
        self.px     = x
        self.py     = y
        self.fx     = x
        self.fy     = y
        self.tx     = ptxx[tp]
        self.ty     = ptyy[tp]
        self.sens   = "Up"
        self.tpp    = tp
        self.cgc    = random.choice(atpp)
        self.cfc    = random.choice(stpp)
        self.arme   = Arme(self.fx,self.fy,self.cgc,self)
        self.melee  = Melee(self,self.cfc)
        self.armsel = 1  # 1 = arme / 2 = melee
        self.imganim= pnim[tp]
        self.ianim  = 0
        self.i      = 0 
        self.bop    = bop
        self.tues   = 0
        # False = bot , True = player
    
    def bouger(self,aa):
        if aa == "Up":
            self.sens=aa
            self.arme.sens=aa
            self.py-=self.vit
            self.i      = 4 
            if vt(self) : self.py+=self.vit
            else:
                if self.bop: bm([0,self.vit])
                else  : self.fy-=self.vit
        elif aa == "Down":
            self.sens=aa
            self.arme.sens=aa
            self.py+=self.vit
            self.i      = 180
            if vt(self) : self.py-=self.vit
            else:
                if self.bop : bm([0,-self.vit])
                else   : self.fy+=self.vit
        elif aa == "Left":
            self.sens=aa
            self.arme.sens=aa
            self.px-=self.vit
            self.i      = 90
            if vt(self) :  self.px+=self.vit
            else:
                if self.bop : bm([self.vit,0])
                else   : self.fx-=self.vit
        elif aa == "Right":
            self.sens=aa
            self.arme.sens=aa
            self.px+=self.vit
            self.i      = -90
            if vt(self) : self.px-=self.vit
            else:
                if self.bop : bm([-self.vit,0])
                else   : self.fx+=self.vit
        if self.armsel == 1:
            self.img            = pygame.transform.rotate( pygame.image.load("images/"+self.imgs[1])      , self.i)
            self.arme.img       = pygame.transform.rotate( pygame.image.load("images/"+self.arme.imgs[0]) , self.i)
        else:
            self.img            = pygame.transform.rotate( pygame.image.load("images/"+self.imgs[0])       , self.i)
            self.melee.img      = pygame.transform.rotate( pygame.image.load("images/"+self.melee.imgs[0]) , self.i)

def aff():
    fenetre.fill((0,0,0))
    for o in mape:
        if o.fx >= 0-o.tx and o.fy >= 0-o.ty and o.fx <= tetx and o.fy <= tety:
            fenetre.blit(o.img,[o.fx,o.fy])
    for o in mapeop:
        if o.fx >= 0-o.tx and o.fy >= 0-o.ty and o.fx <= tetx and o.fy <= tety:
            fenetre.blit(o.img,[o.fx,o.fy])
        o.anim()
    for o in prs:
        if o.fx >= 0-o.tx and o.fy >= 0-o.ty and o.fx <= tetx and o.fy <= tety:
            if perso.tp == 8:
                aa=float(float(o.vie)/float(o.vietot)*float(o.tx))
                pygame.draw.rect(fenetre,(180,0,0),(o.fx,o.fy-6,aa,5),0)
                pygame.draw.rect(fenetre,(0,0,0),(o.fx,o.fy-6,o.tx,5),1)
            if o.armsel == 1:
                fenetre.blit(o.img     ,[o.fx,o.fy])
                fenetre.blit(o.arme.img,[o.fx,o.fy])
            else:
                fenetre.blit(o.img      ,[o.fx,o.fy])
                if o.melee.tpt == 1: fenetre.blit(o.melee.img,[o.fx,o.fy])
                else:
                    fenetre.blit( pygame.transform.rotate(pygame.image.load("images/"+o.melee.imganim[o.melee.ianim]),o.i) , [o.fx,o.fy])
                    o.melee.ianim+=1
                    if o.melee.ianim >= len(o.melee.imganim): o.melee.ianim = 0
            if o.imganim != []:
                fenetre.blit( pygame.transform.rotate( pygame.image.load("images/"+o.imganim[o.ianim]) , o.i ), [o.fx,o.fy] )
                o.ianim +=1
                if o.ianim >= len(o.imganim): o.ianim = 0
                
    for o in blts:
        if o.fx >= 0-o.tx and o.fy-o.ty >= 0 and o.fx <= tetx and o.fy <= tety:
            if o.tpp==1:
                if o.forme == 2: pygame.draw.rect  (fenetre,o.cl,(o.fx,o.fy ,  o.tx,o.ty)   ,0)
                else           : pygame.draw.circle(fenetre,o.cl,(o.fx,o.fy), (o.tx+o.ty)/4 ,0)
            elif o.tpp==2:
                fenetre.blit( o.img , [o.fx,o.fy] )
            elif o.tpp==3:
                fenetre.blit( pygame.transform.rotate( pygame.image.load("images/"+o.imganim[o.ianim]) , o.i ) , [o.fx,o.fy])
                o.ianim += 1
                if o.ianim >= len(o.imganim): o.ianim = 0
    
    if perso.armsel == 1  :
        fenetre.blit(perso.img     ,[perso.fx,perso.fy])
        fenetre.blit(perso.arme.img,[perso.fx,perso.fy])
    elif perso.armsel == 2:
        fenetre.blit(perso.img      ,[perso.fx,perso.fy])
        if perso.melee.tpt == 1: fenetre.blit(perso.melee.img,[perso.fx,perso.fy])
        else:
            fenetre.blit( pygame.transform.rotate(pygame.image.load("images/"+perso.melee.imganim[perso.melee.ianim]),perso.i) , [perso.fx,perso.fy])
            perso.melee.ianim+=1
            if perso.melee.ianim >= len(perso.melee.imganim): perso.melee.ianim = 0
    if perso.imganim != []:
        fenetre.blit( pygame.transform.rotate(pygame.image.load("images/"+perso.imganim[perso.ianim]),perso.i) , [perso.fx,perso.fy])
        perso.ianim+=1
        if perso.ianim >= len(perso.imganim): perso.ianim = 0
    
    if affcarte:
        cx=tetx-150
        cy=20
        pygame.draw.rect(fenetre,(20,25,20),(cx   ,cy   ,100,100),5)
        pygame.draw.rect(fenetre,(250,250,250),(cx   ,cy   ,100,100),0)
        for p in prs:
            pygame.draw.rect(fenetre,(200,0,0),(cx+p.px/(tmx/100)+50,cy+p.py/(tmy/100)+50,4,4),0)
        pygame.draw.rect(fenetre,(0,0,200),(cx+perso.px/(tmx/100)+50,cy+perso.py/(tmy/100)+50,4,4),0)
    if affstats:
        fon=pygame.font.SysFont("Comic Sans MS",20)
        fenetre.blit( pygame.image.load("images/fp.png"),[tetx-150,140] )
        fenetre.blit( fon.render( str( len( prs )+1 ) , 20 , (250,250,250) ) , [tetx-128,140] )
        fenetre.blit( pygame.image.load("images/pt.png"),[tetx-110,140] )
        fenetre.blit( fon.render( str(perso.tues) , 20 , (250,250,250) ) , [tetx-88,140] )
        tbvx=500
        if perso.vie >= 0:
            pva=float(perso.vie)/float(perso.vietot)*float(float(tbvx)-2)
            pygame.draw.rect( fenetre , (150,0,0) , (56.5,50,pva-10,50) , 00 )
            pygame.draw.rect( fenetre , (20,20,0) , (50,50,tbvx,50) , 10 )
            fenetre.blit( fon.render( "VIE = "+str(perso.vie)+"/"+str(perso.vietot) , 20 , (250,250,250) ) , [50+tbvx/2.5,60] )
        else:
            pygame.draw.rect( fenetre , (150,0,0) , (56.5,50,10,50) , 00 )
            pygame.draw.rect( fenetre , (20,20,0) , (50,50,tbvx,50) , 10 )
            fenetre.blit( fon.render( "MORT" , 20 , (250,250,250) ) , [50,60] )
        aaa=time.time()-perso.arme.dtirer
        if aaa <= perso.arme.ttirer:
            tbtx=100
            tbpy=10
            pygame.draw.rect( fenetre , (0,50,100) , (50+tbvx+10,70,aaa/perso.arme.ttirer*tbtx,tbpy) ,0)
            pygame.draw.rect( fenetre , (0,0,0) , (50+tbvx+10,70,tbtx,tbpy) ,2)
            
            
        
        
    pygame.display.update()
    fpsClock.tick(fps)


def cm():
    for x in range(int(-tmx/100),int(tmx/100)):
        for y in range(int(-tmy/100),int(tmy/100)  ):
            mape.append( Om(x*50,y*50,0) )

    while len(mapeop) < 0:
        wx,wy=random.randint(-100*100,100*100),random.randint(-100*100,100*100)
        if mapeop != []:
            for m in mapeop:
                if abs(m.px-wx) >= 150 and abs(m.py-wy) >= 150: mapeop.append( Om(wx,wy,1) )
        else: mapeop.append( Om(wx,wy,1) )
    for x in range(nbprs-1):
        prs.append( Perso(random.randint(-tmx/2,tmx/2),random.randint(-tmy/2,tmy/2),random.choice(ptpp),False,0) )
    return mape,mapeop,prs

def bb():
    for p in prs:
        ddf=["Up","Down","Left","Right"]
        for x in range(10): ddf.append(p.sens)
        p.bouger(random.choice(ddf))
        if random.randint(1,5)==1:
            if p.armsel == 1: p.arme.tirer()
            else            : p.melee.att()
        if random.randint(1,20)==1:
            if p.armsel == 1: p.armsel = 2
            else            : p.armsel = 1
    for b in blts:
        b.bouger()
        b.detect()
#####################################################################################################################################


totnbpartiesjoues=open("profil.nath","r").readlines()[2][:-1]

pygame.init()

fenetre=pygame.display.set_mode((tetx,tety))
pygame.display.set_caption("TLBR","images/icontitle.png")
pygame.key.set_repeat(400,30)
fpsClock = pygame.time.Clock()

fenetre.blit( pygame.font.SysFont("Sans Mono",40).render("chargement veuillez patienter",40,(250,0,0) ) , [tetx/2,tety/2] )
pygame.display.update()

mape,mapeop,prs=cm()

ddx,ddy=random.randint(-tmx/2,tmx/2),random.randint(-tmy/2,tmy/2)

perso=Perso(ddx,ddy,int(open("profil.nath","r").readlines()[4][:-1]),True,1)
perso.arme =Arme(perso.fx,perso.fy,int(open("profil.nath","r").readlines()[5][:-1]),perso)
perso.melee=Melee(perso,int(open("profil.nath","r").readlines()[6]))
perso.fx,perso.fy=tetx/2,tety/2
bm( [perso.fx-perso.px,perso.fy-perso.py] )

inm=0

while encour:
    for event in pygame.event.get():
        if   event.type == QUIT    : encour=False
        elif event.type == KEYDOWN :
            if   event.key == K_q    : encour = False
            if   event.key == K_UP   : perso.bouger("Up")
            elif event.key == K_DOWN : perso.bouger("Down")
            elif event.key == K_LEFT : perso.bouger("Left")
            elif event.key == K_RIGHT: perso.bouger("Right")
            elif event.key == K_a    :
                if perso.armsel == 1 : perso.arme.tirer()
                else                 : perso.melee.att()
            elif event.key == K_z    :
                if perso.armsel == 1 : perso.armsel = 2
                else                 : perso.armsel = 1
    bb()
    aff()
    if perso.vie <= 0:
        time.sleep(1.5)
        break
    if len(prs) <= 0: break



encour2=True
nfont=pygame.font.SysFont("Comic",50)

fenetre.fill((20,20,100))

ore=5*perso.tues+((50*5)-5*len(prs))

if   perso.vie <= 0:
    fenetre.blit( nfont.render( "VOUS ETES MORT :( " , 50 , (100,0,0) ) , [tetx/2-200,tety/2] )
    fenetre.blit( nfont.render( "vous avez tue : "+str(perso.tues)+" ennemis" , 50 , (70,0,0) ) , [tetx/2-200,tety/2+100] )
    fenetre.blit( nfont.render( "vous avez fait un top "+str(len(prs)+1) , 50 , (70,0,0) ) , [tetx/2-200,tety/2+200] )
elif len(prs) == 0:
    fenetre.blit( nfont.render( "VOUS AVEZ FAIT UN TOP 1 ;] " , 50 , (0,100,0) ) , [tetx/2-200,tety/2] )
    fenetre.blit( nfont.render( "vous avez tue : "+str(perso.tues)+" ennemis" , 50 , (0,70,0) ) , [tetx/2-200,tety/2+100] )
else:
    fenetre.blit( nfont.render( "VOUS AVEZ QUITTE LA PARTIE :[ " , 50 , (100,0,0) ) , [tetx/2-200,tety/2] )
    fenetre.blit( nfont.render( "vous avez tue : "+str(perso.tues)+" ennemis" , 50 , (70,0,0) ) , [tetx/2-200,tety/2+100] )
    fenetre.blit( nfont.render( "vous avez fait un top "+str(len(prs)+1) , 50 , (70,0,0) ) , [tetx/2-200,tety/2+200] )

fenetre.blit( nfont.render( "VOUS AVEZ GAGNE "+str(ore)+" ARGENT" , 50 , (170,150,50) ) , [tetx/2-200,tety/2+400] )

fenetre.blit( nfont.render( "PRESS Q TO EXIT " , 50 , (0,0,0) ) , [10,10] )

pygame.display.update()

##########################################################################################################################################

sts=open("profil.nath","r").readlines()
pseudo          =sts[0][:-1]
argent          =int(sts[1][:-1])
totpartiesjoues =int(sts[2][:-1])
tottop1         =int(sts[3][:-1])
pselec          =int(sts[4][:-1])
aselec          =int(sts[5][:-1])
mselec          =int(sts[6])

def save_profil():
    txt=str(pseudo)+"\n"+str(argent)+"\n"+str(totpartiesjoues)+"\n"+str(tottop1)+"\n"+str(pselec)+"\n"+str(aselec)+"\n"+str(mselec)
    f=open("profil.nath","w")
    f.write(txt)
    f.close()

argent+=ore
if len(prs) == 0: tottop1+=1
totpartiesjoues+=1
save_profil()

##########################################################################################################################################

f=open("hist.nath","a")
ff="\n"+str(len(prs)+1)+"|"+str(perso.tues)+"|"+str(perso.tpp)+"|"+str(perso.cgc)+"|"+str(perso.cfc)
#print(ff)
f.write(ff)
f.close()
while encour2:
    if encour2==False: exit()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:
                import subprocess
                subprocess.Popen(["python","main.py"])
                exit()

