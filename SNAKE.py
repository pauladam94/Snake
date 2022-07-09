# coding : utf8
"""

python SNAKE.py
cd Documents\Perso\Python\Snake

code principale du jeu snake
développé par Paul ADAM 

"""
## importation des modules 
import pygame as py
from time import sleep
import fonction_snake as fonc
import DATA as data
import random

## initialisation de pygame
## on charge tout pygame mais on aurait pu charger des modules en particuliers
## ex : pygame.init()
py.init()

## def couleur de fonc
C_FOND = data.BLANC

# Initialisation de la fenetre graphique avec son nom
fenetre = py.display.set_mode((data.LARGUEUR,data.HAUTEUR + 80), py.DOUBLEBUF | py.HWSURFACE | py.RESIZABLE)
py.display.set_caption("Snake GAME P.A.")

# afichage logo et démarrage :
fonc.aff_debut(fenetre)
A=True
FIN = True
while A :
    # receptionnaire des touches du clavier
    #  [2]
    for event in py.event.get() :
        if event.type == py.QUIT :
            A = False
            FIN = False
            break
        if event.type == py.KEYDOWN :
            if event.key == py.K_SPACE :
                A = False 
                break

## affichage du fond
fenetre.fill(C_FOND)

## Vérif des paramètres d'affichage dans le terminal :
print(py.display.Info())

## nombre de pixel par coté de carré
cote=int(data.LARGUEUR/20)

# initialisation des variables principales du Programme :
#Xs0 = 5*(data.LARGUEUR/²cote)
#Ys0 = 5*(data.HAUTEUR/cote)
Xs0 = 5 * cote
Ys0 = 5 * cote
Xs1 = 5 * cote
Ys1 = 5 * cote

# def direction initial
DIRECTION = "bas"

# def taille initial du snake
taille = 2

#d ef vitese du snake : <0.05 ==> impossible
speed_init=100
speed = speed_init

# affichage de la grille
#fonc.quadrillage(fenetre, data.NOIR, data.HAUTEUR+40 , data.LARGUEUR+40, cote, 29)

# def couleur du fruit
#C_fruit = data.ROUGE

#compteur de passaga dans la main boucle
compt0 = 0
compt6 = 0

# def du score initial
score = 0

# affichage score :
fonc.aff_score(fenetre,score)

listXs = [Xs0, Xs1]
listYs = [Ys0, Ys1]
x_last = listXs[taille-1] + 2
y_last = listYs[taille-1] + 2


# dessin du fruit initial :
Xsf , Ysf = fonc.dessin_fruit_style ( compt0,fenetre, 20, listXs, listYs, cote )
Xsc,Ysc = -100,-100


# def var power up coeur:
seuil_coeur = 0

py.display.flip()


# def variable de boucle
lancement = False
# Coeur du programme 
if FIN :
    lancement = True
# réceptionnaire evenements
# on pose (Xs0,Ys0) les coordonnées de la tete du snake 
# et ainsi de suite pour le reste du corps (Xs1,Ys1) etc ...
while lancement :
    py.display.flip()
    #Initialisation des variables de boucle
    # [1]
    t_touche, B = True, True

    # receptionnaire des touches du clavier
    #  [2]
    for event in py.event.get() :
        if event.type == py.QUIT :
            lancement = False
            break
        elif event.type == py.KEYDOWN :
            if B and event.key == py.K_UP and DIRECTION != "bas" and DIRECTION != "haut" :
                Ys0 -= cote
                DIRECTION = "haut"
                t_touche, B = False, False
            elif B and event.key == py.K_DOWN and DIRECTION != "haut" and DIRECTION != "bas":
                Ys0 += cote
                DIRECTION="bas"
                t_touche, B=False, False
            elif B and event.key == py.K_LEFT and DIRECTION != "droite" and DIRECTION != "gauche":
                Xs0 -= cote
                DIRECTION="gauche"
                t_touche , B = False, False
            elif B and event.key == py.K_RIGHT and DIRECTION != "gauche" and DIRECTION != "droite":
                Xs0 += cote
                DIRECTION="droite"
                t_touche , B = False, False

    # Avancé du snake en fonction de la direction : 
    # si aucunes touches appuyées
    # [3]
    if t_touche :
        Xs0,Ys0 = fonc.direct_pos(DIRECTION,Xs1,Ys1,cote)
    
    # test limite de terrain de la prochaine position :
    # actualisation si nécessaire de Xs0 et Ys0
    # [4]
    Xs0,Ys0 = fonc.limit_terrain(Xs0, Ys0, cote)

    # actualisation de toute les coords du snake :
    # [5]
    for i in range(taille) :
        exec("Xs" + str(taille-i) +", Ys" + str(taille-i) + "= Xs" + str(taille-i-1) +", Ys" + str(taille-i-1))
        exec("listXs[i] = Xs" + str(i))
        exec("listYs[i] = Ys" + str(i))

    # test du fruit et positionnement du fruit  :
    # [6]
    if (Xsf, Ysf) == (Xs0, Ys0):
        compt6 += 1
        Xsf , Ysf = fonc.dessin_fruit_style (compt6,fenetre, 20, listXs, listYs, cote ) 
        taille += 1
        score += 5
        fonc.aff_score(fenetre,score)
        listXs.append(int())
        listYs.append(int())

    # arrivée intanpestive du coeur 
    # qui fait gagner 50 points sup 
    # [7]
    if (Xsc, Ysc) == (Xs0, Ys0):
        score += 50
        Xsc,Ysc=-10,-10
        #speed -= 20
        fonc.aff_score(fenetre,score)
    if compt0 % 100 == 0 and compt0 != 0 :
        seuil_coeur = compt0 + 30
        Xsc , Ysc = fonc.dessin_fruit_style (-1,fenetre, 20, listXs, listYs, cote ) 
    if compt0 == seuil_coeur and Xsc>0 :
        speed = speed_init
        py.draw.rect(fenetre,C_FOND,[Xsc+2,Ysc+2,cote-2,cote-2])
        
    # dessin de la tete du snake :
    # [8]
    # fonc.dessin_carre(fenetre, fonc.VERT_FLASHI, fonc.MARRON , Xs0, Ys0, cote)
    fonc.dessin_tete(fenetre, Xs0, Ys0, cote, DIRECTION)

    # effacement de la dernière tete du snake par la queue
    # [9]
    if taille >= 3 :
        fonc.dessin_carre(compt0,fenetre, data.VERT, data.MARRON , Xs2, Ys2, cote)
        
    # verif de queue mangée
    # [10]
    if fonc.verif_queue_manger(listXs, listYs, taille) == True :
        fonc.fin_loose(fenetre, score)
        lancement = False
        break

    # test de fin de jeu
    # [11]
    if score >= 1000 :
        fonc.fin_win(fenetre, score)
        lancement = False
        break

    # effacement dernière image : (bout de la queue)
    # [12]
    py.draw.rect(fenetre, C_FOND, (x_last,y_last,cote-2, cote-2))
    x_last = listXs[taille-1] + 2
    y_last = listYs[taille-1] + 2

    # attente qui crée un effet plus ou moins fort de vitesse :
    # speed définit au début en miliseconde
    # [13]
    py.time.delay(speed)
    compt0+=1


sleep(1)
py.quit()