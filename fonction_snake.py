# coding: utf8

"""
module jeu snake

"""
import pygame as py
import DATA as data
import random


# aff logo et affichage :
def logo(window) :
    logo=data.logo(0,0)
    for i in range(len(logo)):
    	a,b = logo[i]
    	a,b = a*20,b*20
    	logo[i] = a,b
    py.draw.polygon(window, data.MARRON , logo )


def aff_debut(window):
    logo(window)
    py.display.update()
    dem = py.font.SysFont("arial", 30)
    aff = dem.render("appuyez sur la barre espace pour commencer", True, (255,255,255))
    window.blit(aff, [10,400] )
    py.display.update()


# fonction qui permet de renvoyer la prochaine position
# de la tete du serpent en fonction de sa direction
def direct_pos(direction, posx, posy, cote):
    if direction=="haut":
    	posy-=cote
    elif direction=="bas":
        posy+=cote
    elif direction=="gauche":
        posx-=cote
    elif direction=="droite":
    	posx+=cote
    return(posx,posy)


def quadrillage(window, COULEUR, H , L, cote, nb_c):
    y = cote
    x = cote
    for i in range (nb_c - 1) :
        py.draw.line(window, COULEUR , [x,0], [x , H] , 2)
        x+=cote

    for i in range (nb_c - 1) :
        py.draw.line(window, COULEUR , [0,y], [L , y], 2 )
        y+=cote


def dessin_fruit_style (compt,window, nb_c, list_x, list_y, cote) :
    compt_bool=False
    coeur = True
    if compt<0:
    	coeur = False
    if compt%2 == 0 and coeur:
        compt_bool=True
    test = True
    while test :
        compteur = 0
        x = random.randint(0,19)
        y = random.randint(0,19)
        x *= cote
        y *= cote
        for i in range(len(list_x)) :
            if x == list_x[i] and y == list_y[i]:
                compteur += 1
        if compteur == 0 :
            test = False

    xf = x + 13
    yf = y + 14
    if compt_bool == True :
        queue,corps = data.piment(x,y)
        C_q=data.VERT
        C_c=data.ROUGE
    elif compt_bool == False and coeur==True:
        queue,corps = data.fraise(x,y)
        C_q=data.VERT
        C_c=data.ROUGE
    elif coeur == False:
    	queue,corps=data.coeur(x,y)
    	C_q=data.NOIR
    	C_c=data.ROUGE
    #corps = rotate_list(corps,2,x,y)
    #queue = rotate_list(queue,2,x,y)
    py.draw.polygon(window, C_q , queue )
    py.draw.polygon(window, C_c , corps , False)
    return(x, y)

def verif_queue_manger(list_x, list_y, taille) :
    result = False
    compteur=0
    Xs0, Ys0 = list_x[0], list_y[0]
    for i in range(2, len(list_x)) :
        if Xs0 == list_x[i]  and Ys0 == list_y[i]:
           compteur += 1
    if compteur >= 1 :
        result = True
    if taille <= 4 :
        result = False
    return(result)

def fin_win(window, score):
    arial_30 = py.font.SysFont("arial", 30)
    dimension_text = arial_30.render("{}".format(" Vous avez gagné !! : - ))"), True, data.NOIR)
    score = arial_30.render("Score : " + str(score), False, data.BLEU)
    window.blit(dimension_text, [150,200] )
    window.blit(score, [150, 300])
    py.display.flip()
    py.time.delay(2000)


def fin_loose(window, score):
    arial_30 = py.font.SysFont("arial", 30)
    dimension_text = arial_30.render("{}".format(" Vous avez perdu !! ; - ) "), True, data.NOIR)
    score = arial_30.render("Score : " + str(score), False, data.BLEU)
    window.blit(dimension_text, [150,200] )
    window.blit(score, [150, 300])
    py.display.flip()
    py.time.delay(2000)

def dessin_carre(compteur,window, COULEUR_corps, C_style,  x, y, cote) :
    compt_bool=False
    if compteur/2==int(compteur/2) :
        compt_bool=True
    py.draw.rect(window, COULEUR_corps, (x+2 , y+2 , cote-2 , cote-2 ))
    cx,cy=2,3
    if compt_bool:
        x-=10
        cx+=2
    py.draw.rect(window, C_style, (x + 15, y+5, 2, 3))
    if compt_bool:
    	x+=20
    	cx-=2
    	cy+=2
    py.draw.rect(window, C_style, (x + 7, y+20, 2, 3))

def dessin_tete (window, x, y, cote, direct):
    if direct=="haut" :
        xl,yl,l,h = x+13,y+2,2,11
        c=0
    elif direct=="bas":
        xl,yl,l,h = x+13,y+13,2,11
        c=2
    elif direct=="gauche":
        xl,yl,l,h = x+2,y+13,11,3
        c=1
    elif direct=="droite":
        xl,yl,l,h = x+13,y+13,11,3
        c=3
    tete = data.tete_snake( x , y )
    tete = rotate_list( tete , c , x , y )
    py.draw.polygon( window, data.VERT , tete )
    py.draw.rect(window, data.ROUGE, [xl,yl,l,h])

def limit_terrain(x, y, cote) :
    if x == -cote :
        x = data.LARGUEUR-cote
    elif x >= data.LARGUEUR :
        x = 0

    if  y <= -cote :
        y = data.HAUTEUR-cote
    elif  y >= data.HAUTEUR :
        y = 0
    return(x, y)

def rotate_list(list, c, x, y):
    for i in range(len(list)):
        #print(list[i])
        for j in range(c) :
            a,b=list[i]
            ap = b + x - y
            bp = x + y - a + 28
            list[i] = ap,bp
    return(list)

def aff_score(window,score):
    py.draw.rect(window,data.NOIR,[0,540,540,100])
    arial_30 = py.font.SysFont("arial", 30)
    score = arial_30.render("Score : "+str(score), True, data.BLANC)
    window.blit(score, [100,560] )
