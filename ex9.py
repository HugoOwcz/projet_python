
#owczarczak hugo 1er3 / léger angélo 1er3

from tkinter import *
from random import *

def newallumettes():
    global nballumette
    global tour
    nballumette=25
    Allumette.delete(ALL)
    y=390
    for i in range(25):
        Allumette.create_line(10,y,140,y, fill='black')
        y=y-15
    if random()>0.5:
        texte.set('Vous commencez.')
        tour=0
    else:
        texte.set("L'ordinatuer commence.")
        tour=1

def retirerallumettes1():
    global nballumette
    global tour
    if tour==0:
        Allumette.delete(ALL)
        nballumette-=1
        if nballumette<=0:
            texte.set("L'ordinateur a gagné.")
            tour=2
        else:
            y=390
            for i in range(nballumette):
                Allumette.create_line(10,y,140,y,fill='black')
                y=y-15
            texte.set("Faite jouer l'ordinateur")
            tour=1

def retirerallumettes2():
    global nballumette
    global tour
    if tour==0:
        Allumette.delete(ALL)
        nballumette-=2
        if nballumette<=0:
          texte.set("L'ordinateur a gagné.")
          tour=2
        else:
            y=390
            for i in range(nballumette):
                Allumette.create_line(10,y,140,y,fill='black')
                y=y-15
            texte.set("Faite jouer l'ordinateur")
            tour=1

def retirerallumettes3():
    global nballumette
    global tour
    if tour==0:
        Allumette.delete(ALL)
        nballumette-=3
        if nballumette<=0:
            texte.set("L'ordinateur a gagné.")
            tour=2
        else:
            y=390
            for i in range(nballumette):
                Allumette.create_line(10,y,140,y,fill='black')
                y=y-15
            texte.set("Faite jouer l'ordinateur")
            tour=1

def ordi():
    global nballumette
    global tour
    if tour==1:
        Allumette.delete(ALL)
        y=390
        if nballumette==1:
            nballumette-=1
            if nballumette<=0:
                texte.set("Vous avez gagné.")
                tour=2
        elif nballumette==2:
            nballumette-=1
            if nballumette<=0:
                texte.set("Vous avez gagné.")
                tour=2
            for i in range(nballumette):
                Allumette.create_line(10,y,140,y, fill='black')
                y=y-15
            texte.set("A vous de jouer")
            tour=0
        elif nballumette==3:
            nballumette-=2
            if nballumette<=0:
                texte.set("Vous avez gagné.")
                tour=2
            for i in range(nballumette):
                Allumette.create_line(10,y,140,y, fill='black')
                y=y-15
            texte.set("A vous de jouer")
            tour=0
        elif nballumette==4:
            nballumette-=3
            if nballumette<=0:
                texte.set("Vous avez gagné.")
                tour=2
            for i in range(nballumette):
                Allumette.create_line(10,y,140,y, fill='black')
                y=y-15
            texte.set("A vous de jouer")
            tour=0
        elif nballumette==6:
            nballumette-=1
            if nballumette<=0:
                texte.set("Vous avez gagné.")
                tour=2
            for i in range(nballumette):
                Allumette.create_line(10,y,140,y, fill='black')
                y=y-15
            texte.set("A vous de jouer")
            tour=0
        elif nballumette==7:
            nballumette-=2
            if nballumette<=0:
                texte.set("Vous avez gagné.")
                tour=2
            for i in range(nballumette):
                Allumette.create_line(10,y,140,y, fill='black')
                y=y-15
            texte.set("A vous de jouer")
            tour=0
        elif nballumette==8:
            nballumette-=3
            if nballumette<=0:
                texte.set("Vous avez gagné.")
                tour=2
            for i in range(nballumette):
                Allumette.create_line(10,y,140,y, fill='black')
                y=y-15
            texte.set("A vous de jouer")
            tour=0
        else:
            nballumette-=3
            if nballumette<=0:
                texte.set("Vous avez gagné.")
            for i in range(nballumette):
                Allumette.create_line(10,y,140,y, fill='black')
                y=y-15
            texte.set("A vous de jouer")
            tour=0


Jeu2=Tk()

Jeu2.title('Jeu des allumettes')
Jeu2.geometry('350x550')
Jeu2['bg']='grey'

texte=StringVar()
texte.set('Cliquez sur le bouton ci-dessus pour lancer une partie')
début=Label(Jeu2, textvariable=texte)
début.grid(row=2,column=2)

Quitter=Button(Jeu2, text='Quitter', command=Jeu2.destroy)
Quitter.grid(row=6, column=2)

Allumette=Canvas(Jeu2, width=150, height=400)
Allumette.grid(row=5,column=2)

New2=Button(Jeu2, text='Nouvelle Partie', command=newallumettes)
New2.grid(row=0, column=2)

Un=Button(Jeu2, text='1', command=retirerallumettes1)
Un.grid(row=3,column=1)

Deux=Button(Jeu2, text='2', command=retirerallumettes2)
Deux.grid(row=3,column=2)

Trois=Button(Jeu2, text='3', command=retirerallumettes3)
Trois.grid(row=3,column=3,)

Ordi=Button(Jeu2, text='Ordi', command=ordi)
Ordi.grid(row=4, column=2)

Jeu2.mainloop()



