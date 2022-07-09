# coding: utf8
"""
test de tkinter
ensemble de méthodes tkinter

"""

import tkinter as tk
from Module_snake import *

# début générale de la fonction
fenetre = tk.Tk()
fenetre.title("Test de Tkinter")

#position et taille fenetre.geometry
LARGUEUR = 500
HAUTEUR = 500

#ABSCISSE = 200
#ORDONNEE = 200


# récupération la résolution de l'écran
# et donc recup de x et y d'une fenetre centré
#"""
screen_x = int(fenetre.winfo_screenwidth())
screen_y = int(fenetre.winfo_screenheight())

posX = (screen_x // 2) - (LARGUEUR // 2)
posY = (screen_y // 2) - (HAUTEUR // 2)
#"""

fenetre.geometry("{}x{}+{}+{}".format(LARGUEUR,HAUTEUR,posX,posY))

#interdiction du redimentionnement False ou True
"""
fenetre.resizable( width = False , height = True )
"""

# position de la fenetre et taille
"""
fenetre.positionfrom("user")
fenetre.sizefrom("user")
"""

#  
"""
fenetre.minsize(100,100)
fenetre.maxsize(1000,1000)
"""

#methode pour fermer la fenetre
#fenetre.quit()

#tkinter.draw.rect(fenetre,(0,0,0),(0,0,10,10))


### Widgets :
# .Label
# les labels (des dictionnaires)
# 
""" 
label_t = tk.Label(fenetre, text="Entrez \n votre code")
print(label_t["text"])
#print(label.cget("text"))
#label.config(text="nouveau message")
label_t.pack()
"""

# .Entry
# show pour dire ce qu'affiche le programme 
# pour chaque caractère écritt 
#
#exportselection savoir quoi faire d'une selection
#

"""
entry_i = tk.Entry(fenetre, width=45 ,show="*", exportselection=0)
entry_i.pack()
"""

# .Button  affichage d'un bouton
# commande permet d'effectuer une fonction lors 
# de l'appui du bouton
"""
def fonc():
	print("test widgets")
button_t = tk.Button(fenetre, text="Entrer", width=20, height=3, command=fonc)
button_t.pack()
"""


# .Checkbutton
# pas coché = 0 coché =1
"""
check=tk.Checkbutton(fenetre, text="Hello", offvalue=2, onvalue=5)
check.pack()
"""

# .Radiobutton + test avec un observeur pour récupérer $
# les données 
# 
"""

#		label["text"]="Il est trop Chauddd le bac c'est carrrééé"
#		label["text"]="Cette homme est nul \n il a pas eu son bac"
def update(*arg):
    if gender.get():
        vlabel.set("Il est trop Chauddd le bac c'est carrrééé")
    else :
        vlabel.set("Cette homme est nul \n il a pas eu son bac")

gender       = tk.IntVar()
vlabel = tk.StringVar()
gender.trace("w",update)
radio1 = tk.Radiobutton(fenetre, text = "bac", value=1, variable=gender)
radio2 = tk.Radiobutton(fenetre, text = "pas bac", value=0, variable=gender)
label  = tk.Label(fenetre, text="hey", textvariable=vlabel)
radio1.pack()
radio2.pack()
label.pack()
"""

#widget=tk.Scale(fenetre, from_=10, to=100)
#widget.pack()

#widget=tk.Spinbox(app, from_=1, to=10)
#widget.pack()


"""
lb=tk.Listbox(fenetre)
lb.insert(1,"Windows")
lb.insert(2,"")
lb.insert(4,"hey")
lb.insert(3,"why ?")
lb.pack()
"""

#message d'erreur, fenetre modale
#showerror(titre_fen,msg)
#showinfo()
#showwarning()
#askquestion() => oui ou non
#askokcancel() => ok ou annuler
#askyesno() => oui ou non
#askretrycancel() => recommencer ou annuler
"""
from tkinter import messagebox
def show_window():
	messagebox.showerror("erreur","un probleme est survenu")

msg=tk.Button(fenetre, text="déclencher une erreur", command=show_window)
msg.pack()

"""

## création d'objet :
"""
Tkinter : python
StringVar() : str()
IntVar() : int()
DoubleVar() : float()
BooleanVar() : bool()
"""

#"""

# récupération des variables pour les utiliser 
# avec un observeur (var_label.set())
"""
def update_label(*arg):
	var_label.set(var_entry.get())

var_entry = tk.StringVar()
var_entry.trace("w",update_label)
entry = tk.Entry(fenetre, text=var_entry)


var_label=tk.StringVar()
label = tk.Label(fenetre, text="ddd" ,textvariable = var_label )

entry.pack()
label.pack()
"""

# Widgets de tableau mainframe ... on mettra ensuite mainframe dans 
# les paramètres des autres widgets pour qu'il soit dans le tableau 
# crée avec la commande .Frame
"""
mframe= tk.Frame(fenetre, width=100, height=100, borderwidth=2)
mframe.pack()

# on a aussi .LabelFrame dans lequel on rajoute un paramètre text="<titre>"
"""
 
#"""

#positionnement des widgets avec le .pack()*
"""
à voir avec vidéo pyhton #24 Formation vidéo
  
"""

fenetre.mainloop()