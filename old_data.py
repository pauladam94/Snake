"""
def verif():
	return()

# commande dans le programme
# dessin du quadrillage : (optionnel)
# ms.quadrillage(fenetre, ms.NOIR, ms.HAUTEUR , ms.LARGEUR, cote, 20)
def quadrillage(window, COULEUR, HAUTEUR , LARGEUR, cote, nb_c):
    y = cote
    x = cote
    for i in range (nb_c - 1) :
        py.draw.line(window, COULEUR , [x,0], [x , HAUTEUR] , 2)
        x+=cote

    for i in range (nb_c - 1) :
        py.draw.line(window, COULEUR , [0,y], [LARGEUR , y], 2 )
        y+=cote
"""
"""
def case_list(cote, nb_c):
    x = 0
    y = 0
    compt_l = 0
    list=[]
    for ligne in range(nb_c-1):
        compt_c = 0
        for colonne in range(nb_c-1):
            list.append((x,y))
            compt_c += 1
            x = int(compt_c * cote)
            y = int(compt_l * cote)
        compt_l += 1
    #print(list)
    return(list)
"""
"""
def dessin_fruit (window, COULEUR, nb_c, list_x, list_y, cote) :
    test = True
    while test :
        compteur = 0
        #print("c pas cool")
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
    py.draw.circle(window, COULEUR,[xf , yf] , 8)
    #print("x=",x,"y=",y)
    return(x, y)
"""
