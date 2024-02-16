
import random
import json
from tkinter import *
from tkinter import messagebox


class Pion:

    def __init__(self, joueur):
        self._joueur = joueur
        self._position = None
        self._case_possible = []

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def get_joueur(self):
        return self._joueur

    def set_joueur(self, joueur):
        self._joueur = joueur

    def get_case_possible(self):
        return self._case_possible
    
    def set_case_possible(self, case_possible):
        self._case_possible = case_possible

    def calcul_case_possible(self, plateau):
        """
            IN : le plateau de jeu
            Recherche toute les cases possible pour le pion en prenant en compte les autres élément du plateau
        """
        self._case_possible = []
        x = self._position[0]
        y = self._position[1]
        if x-2 >= 0 and y-1 >= 0:
            if plateau[x-2][y-1] is None:
                self._case_possible.append((x-2, y-1))
        if x-2 >= 0 and y+1 < len(plateau):
            if plateau[x-2][y+1] is None:
                self._case_possible.append((x-2, y+1))
        if x+2 < len(plateau) and y-1 >= 0:
            if plateau[x+2][y-1] is None:
                self._case_possible.append((x+2, y-1))
        if x+2 < len(plateau) and y+1 < len(plateau):
            if plateau[x+2][y-1] is None:
                self._case_possible.append((x+2, y+1))
        if x-1 >= 0 and y-2 >= 0:
            if plateau[x-1][y-2] is None:
                self._case_possible.append((x-1, y-2))
        if x+1 < len(plateau) and y-2 >= 0:
            if plateau[x+1][y-2] is None:
                self._case_possible.append((x+1, y-2))
        if x-1 >= 0 and y+2 < len(plateau):
            if plateau[x-1][y+2] is None:
                self._case_possible.append((x-1, y+2))
        if x+1 < len(plateau) and y+2 < len(plateau):
            if plateau[x+1][y+2] is None:
                self._case_possible.append((x+1, y+2))


class Croix:

    def __init__(self, position, joueur):
        self._position = position
        self._joueur = joueur

    def get_pos(self):
        return self._position

    def set_pos(self, position):
        self._position = position

    def get_joueur(self):
        return self._joueur

    def set_joueur(self, joueur):
        self._joueur = joueur

    def cherche_nb_voisin(self, plateau):
        """
            IN : le plateau de jeu
            OUT : le plus grand nombre de croix aligné
        """
        compteur = 1
        x = self._position[0]
        y = self._position[1]

        while x > 0:
            x -= 1
            if isinstance(plateau[x][y], Croix) and plateau[x][y].get_joueur() == self._joueur:
                compteur += 1
            else:
                break
        x = self._position[0]
        while x < len(plateau)-1:
            x += 1
            if isinstance(plateau[x][y], Croix) and plateau[x][y].get_joueur() == self._joueur:
                compteur += 1
            else:
                break
        compteur_final = compteur
        compteur = 1
        x = self._position[0]

        while y > 0:
            y -= 1
            if isinstance(plateau[x][y], Croix) and plateau[x][y].get_joueur() == self._joueur:
                compteur += 1
            else:
                break
        y = self._position[1]
        while y < len(plateau)-1:
            y += 1
            if isinstance(plateau[x][y], Croix) and plateau[x][y].get_joueur() == self._joueur:
                compteur += 1
            else:
                break
        compteur_final = max(compteur_final, compteur)
        compteur = 1
        y = self._position[1]

        while y > 0 and x > 0:
            y -= 1
            x -= 1
            if isinstance(plateau[x][y], Croix) and plateau[x][y].get_joueur() == self._joueur:
                compteur += 1
            else:
                break
        x = self._position[0]
        y = self._position[1]
        while y < len(plateau)-1 and x < len(plateau)-1:
            y += 1
            x += 1
            if isinstance(plateau[x][y], Croix) and plateau[x][y].get_joueur() == self._joueur:
                compteur += 1
            else:
                break
        compteur_final = max(compteur_final, compteur)
        compteur = 1
        x = self._position[0]
        y = self._position[1]

        while y > 0 and x < len(plateau)-1:
            y -= 1
            x += 1
            if isinstance(plateau[x][y], Croix) and plateau[x][y].get_joueur() == self._joueur:
                compteur += 1
            else:
                break
        x = self._position[0]
        y = self._position[1]
        while y < len(plateau)-1 and x > 0:
            y += 1
            x -= 1
            if isinstance(plateau[x][y], Croix) and plateau[x][y].get_joueur() == self._joueur:
                compteur += 1
            else:
                break
        return max(compteur_final, compteur), self._joueur


class Jeu:

    def __init__(self, taille, joueur_1, joueur_2, nombre_pion_pour_gagne):
        self._taille_plateau = taille
        self._plateau = []
        self.creer_plateau()
        self._pion_1 = Pion(joueur_1)
        self._pion_2 = Pion(joueur_2)
        self._joueur_qui_joue = self._pion_2.get_joueur()
        self._tour_de_jeu = 0
        self._nombre_pion_pour_gagne = nombre_pion_pour_gagne
        self._gagne = [False, None]

    def get_taille_plateau(self):
        return self._taille_plateau

    def set_taille_plateau(self, taille_plateau):
        self._taille_plateau = taille_plateau

    def get_plateau(self):
        return self._plateau

    def set_plateau(self, plateau):
        self._taille_plateau = plateau

    def get_joueur_qui_joue(self):
        return self._joueur_qui_joue

    def set_joueur_qui_joue(self, joueur_qui_joue):
        self._joueur_qui_joue = joueur_qui_joue

    def get_tour_de_jeu(self):
        return self._tour_de_jeu

    def set_tour_de_jeu(self, tour_de_jeu):
        self._tour_de_jeu = tour_de_jeu

    def get_nombre_pion_pour_gagne(self):
        return self._nombre_pion_pour_gagne

    def set_nombre_pion_pour_gagne(self, nombre_pion_pour_gagne):
        self._nombre_pion_pour_gagne = nombre_pion_pour_gagne

    def creer_plateau(self):
        """
            Créer le plateau avec toute les cases contenant l'élément None
        """
        self._plateau = []
        for i in range(self._taille_plateau):
            self._plateau.append([])
            for j in range(self._taille_plateau):
                self._plateau[i].append(None)

    def mouvement_possible(self, x, y):
        """
            IN : les coordonées x et y d'une possible case pour le pion
            OUT : un booléen iniquant si la case aux coordonées x et y est une cases possible pour le pion
        """
        if self._tour_de_jeu > 2:
            if (x, y) in self._pion_1.get_case_possible() and self._joueur_qui_joue == self._pion_1.get_joueur():
                return True
            if (x, y) in self._pion_2.get_case_possible() and self._joueur_qui_joue == self._pion_2.get_joueur():
                return True
            return False
        return self._plateau[x][y] is None

    def mouvement(self, x, y):
        """
            IN : les coordonées x et y de la nouvelle case du pion
            Déplace le pion aux coordonées x et y rentré et crée une instance de la classe Croix aux ancienne coordonées du pion
        """
        if self._joueur_qui_joue == self._pion_1.get_joueur():
            if self._tour_de_jeu == 1:
                self._pion_1.set_position((x, y))
                self._plateau[x][y] = self._pion_1
            else:
                tmp_x = self._pion_1.get_position()[0]
                tmp_y = self._pion_1.get_position()[1]
                self._plateau[tmp_x][tmp_y] = Croix(self._pion_1.get_position(), self._pion_1.get_joueur())
                self._pion_1.set_position((x, y))
                self._plateau[x][y] = self._pion_1
        else:
            if self._tour_de_jeu == 2:
                self._pion_2.set_position((x, y))
                self._plateau[x][y] = self._pion_2
            else:
                tmp_x = self._pion_2.get_position()[0]
                tmp_y = self._pion_2.get_position()[1]
                self._plateau[tmp_x][tmp_y] = Croix(self._pion_2.get_position(), self._pion_2.get_joueur())
                self._pion_2.set_position((x, y))
                self._plateau[x][y] = self._pion_2

    def gagne(self):
        """
            Fonction qui regarde si un joueur a gagné la partie et met à jour l'attribut gagne en conséquence
        """
        for ligne in self._plateau:
            for element in ligne:
                if isinstance(element, Croix) and not self._gagne[0]:
                    tmp = element.cherche_nb_voisin(self._plateau)
                    if tmp[0] >= self._nombre_pion_pour_gagne:
                        self._gagne = [True, tmp[1]]


class Affichage(Jeu):

    def __init__(self):
        self._attribut_plateau = []

        self._temporaire = None
        self._taille = None
        self._nb_pion = None
        self._joueur_1 = None
        self._joueur_2 = None
        self._ordinateur = None
        self._valider = False
        self._donnes = None

        self.parametrage()

        if self._donnes is not None:
            self._attribut_plateau = [self._donnes["taille"], self._donnes["pion_joueur"][0], self._donnes["pion_joueur"][1], self._donnes["pion_pour_gagner"]]

        if self._valider:
            Jeu.__init__(self, self._attribut_plateau[0], self._attribut_plateau[1], self._attribut_plateau[2], self._attribut_plateau[3])

            if self._donnes is not None:
                self._ordinateur = self._donnes['ordinateur']
                self._pion_1.set_position(self._donnes["pion_pos"][0])
                self._pion_2.set_position(self._donnes["pion_pos"][1])
                self._plateau[self._pion_1.get_position()[0]][self._pion_1.get_position()[1]] = self._pion_1
                self._plateau[self._pion_2.get_position()[0]][self._pion_2.get_position()[1]] = self._pion_2
                self._tour_de_jeu = self._donnes["tour_de_jeu"]-1
                croix_pos = self._donnes["croix"]["pos"]
                croix_joueur = self._donnes["croix"]["joueur"]
                for i in range(len(croix_pos)):
                    self._plateau[croix_pos[i][0]][croix_pos[i][1]] = Croix(croix_pos[i], croix_joueur[i])
                if self._donnes["joueur_du_tour"] == self._pion_1.get_joueur():
                    self._joueur_qui_joue = self._pion_2.get_joueur()
                else:
                    self._joueur_qui_joue = self._pion_1.get_joueur()

            self._root = None
            self._plateau_dessin = None
            self._str_historique = None
            self._tour_de_jeu_texte = None
            self._joueur_qui_joue_var = None

            self.affichage()

    def update(self):
        """
            Fonction qui va faire toute les modifications du jeu à chaque interaction
        """
        if self._pion_1.get_position() is not None:
            self._pion_1.calcul_case_possible(self._plateau)
        if self._pion_2.get_position() is not None:
            self._pion_2.calcul_case_possible(self._plateau)
        self.draw()
        if self._tour_de_jeu > (self._nombre_pion_pour_gagne-1)*2:
            self.gagne()
        rejouer = None
        if self._gagne[0]:
            if self._gagne[1] == self._pion_1.get_joueur():
                rejouer = messagebox.askquestion(self._pion_1.get_joueur()+' a gagné.', 'Voulez-vous rejouer ?')
            else:
                rejouer = messagebox.askquestion(self._pion_2.get_joueur() + ' a gagné.', 'Voulez-vous rejouer ?')
        if rejouer == 'yes':
            self.restart()
        if rejouer == 'no':
            self._root.destroy()
        self._tour_de_jeu += 1
        self._tour_de_jeu_texte.set(str(self._tour_de_jeu))
        if self._joueur_qui_joue == self._pion_1.get_joueur():
            self._joueur_qui_joue = self._pion_2.get_joueur()
        else:
            self._joueur_qui_joue = self._pion_1.get_joueur()
        if self._joueur_qui_joue == self._pion_2.get_joueur():
            self._joueur_qui_joue_var.set(self._attribut_plateau[2])
        else:
            self._joueur_qui_joue_var.set(self._attribut_plateau[1])
        if self._ordinateur and self._joueur_qui_joue == self._pion_2.get_joueur():
            self.ordinateur()

    def draw(self):
        """
            Fonction qui va dessiné le plateau
        """
        self._plateau_dessin.delete('all')
        taille = 500 // self._taille_plateau
        for i in range(self._taille_plateau):
            for j in range(self._taille_plateau):
                self._plateau_dessin.create_rectangle(0+taille*j, 0+taille*i, taille+taille*j, taille+taille*i, outline='white')
                if self._joueur_qui_joue == self._pion_2.get_joueur() and (i, j) in self._pion_1.get_case_possible():
                    self._plateau_dessin.create_oval(0+taille*j+2, 0+taille*i+2, taille+taille*j-2, taille+taille*i-2, outline='blue')
                elif isinstance(self._plateau[i][j], Pion) and self._plateau[i][j].get_joueur() == self._attribut_plateau[1]:
                    self._plateau_dessin.create_oval(0+taille*j+2, 0+taille*i+2, taille+taille*j-2, taille+taille*i-2, fill='blue')
                elif isinstance(self._plateau[i][j], Croix) and self._plateau[i][j].get_joueur() == self._attribut_plateau[1]:
                    self._plateau_dessin.create_line(0+taille*j+2, 0+taille*i+2, taille+taille*j-2, taille+taille*i-2, fill='blue')
                    self._plateau_dessin.create_line(taille+taille*j-2, 0+taille*i+2, 0+taille*j+2, taille+taille*i-2, fill='blue')
                elif self._joueur_qui_joue == self._pion_1.get_joueur() and (i, j) in self._pion_2.get_case_possible():
                    self._plateau_dessin.create_oval(0+taille*j+2, 0+taille*i+2, taille+taille*j-2, taille+taille*i-2, outline='red')
                elif isinstance(self._plateau[i][j], Pion) and self._plateau[i][j].get_joueur() == self._attribut_plateau[2]:
                    self._plateau_dessin.create_oval(0+taille*j+2, 0+taille*i+2, taille+taille*j-2, taille+taille*i-2, fill='red')
                elif isinstance(self._plateau[i][j], Croix) and self._plateau[i][j].get_joueur() == self._attribut_plateau[2]:
                    self._plateau_dessin.create_line(0+taille*j+2, 0+taille*i+2, taille+taille*j-2, taille+taille*i-2, fill='red')
                    self._plateau_dessin.create_line(taille+taille*j-2, 0+taille*i+2, 0+taille*j+2, taille+taille*i-2, fill='red')

    def click(self, event):
        """
            IN : les coordonées x et y du click
            Appelle de toute les fonction en conséquence du click
        """
        y = event.x // (500 // self._taille_plateau)
        x = event.y // (500 // self._taille_plateau)
        if self.mouvement_possible(x, y):
            self.mouvement(x, y)
            self.update()

    def ordinateur(self):
        """
            Fonction qui fait joué l'ordinateur si la fonction a été sélectionné lors du paramétrage
        """
        if self._tour_de_jeu > 2:
            coup_possible = self._pion_2.get_case_possible()
            coup = random.randint(0, len(coup_possible)-1)
            self.mouvement(coup_possible[coup][0], coup_possible[coup][1])
        else:
            x = random.randint(0, self._taille_plateau-1)
            y = random.randint(0, self._taille_plateau-1)
            while self._plateau[x][y] is not None:
                x = random.randint(0, self._taille_plateau-1)
                y = random.randint(0, self._taille_plateau-1)
            self.mouvement(x, y)
        self.update()

    def sauvegarder(self):
        """
            Fonction qui sauvegarde la partie dans un fichier texte
        """
        fichier = open("save.txt", "w")
        croix = {"pos": [], "joueur": []}
        for ligne in self._plateau:
            for element in ligne:
                if isinstance(element, Croix):
                    croix["pos"].append(element.get_pos())
                    croix["joueur"].append(element.get_joueur())
        json.dump({"ordinateur": self._ordinateur, "taille": self._taille_plateau, "croix": croix, "tour_de_jeu": self._tour_de_jeu, "pion_pour_gagner": self._nombre_pion_pour_gagne, "pion_joueur": (self._pion_1.get_joueur(), self._pion_2.get_joueur()), "pion_pos": (self._pion_1.get_position(), self._pion_2.get_position()), "joueur_du_tour": self._joueur_qui_joue}, fichier)
        fichier.close()

    def charger(self):
        """
            Fonction que charge la partie sauvegarder dans le fichier texte si le joueur l'a demandé
        """
        fichier = open("save.txt", "r")
        self._donnes = json.load(fichier)
        fichier.close()
        self._valider = True

    def restart(self):
        """
            Fonction qui relance une partie si le joueur le veut à la fin d'une partie
        """
        self._root.destroy()
        self._valider = False
        self.parametrage()
        if self._valider:
            self._taille_plateau = self._attribut_plateau[0]
            self.creer_plateau()
            self._pion_1 = Pion(self._attribut_plateau[1])
            self._pion_2 = Pion(self._attribut_plateau[2])
            self._nombre_pion_pour_gagne = self._attribut_plateau[3]
            self._joueur_qui_joue = self._pion_2.get_joueur()
            self._tour_de_jeu = 0
            self._gagne = [False, None]
            self.affichage()

    def affichage(self):
        """
            Fonction qui crée la fenêtre Tkinter du jeu
        """
        self._root = Tk()
        self._root.geometry('700x500')

        _frame1 = Frame(self._root, width=500, height=500)
        _frame1.grid(row=0, column=0, rowspan=2)
        self._plateau_dessin = Canvas(_frame1, width=500, height=500, bg='black')
        self._plateau_dessin.pack()
        self._plateau_dessin.bind('<Button-1>', self.click)

        frame2 = Frame(self._root)
        frame2.grid(row=0, column=1)
        self._str_historique = StringVar()
        affichage_historique = Label(frame2, textvariable=self._str_historique)
        affichage_historique.pack()

        frame3 = Frame(self._root)
        frame3.grid(row=1, column=1)
        self._tour_de_jeu_texte = StringVar()
        label_tour_de_jeu = Label(frame3, textvariable=self._tour_de_jeu_texte)
        label_tour_de_jeu.pack()
        self._joueur_qui_joue_var = StringVar()
        joueur_qui_joue_texte = Label(frame3, textvariable=self._joueur_qui_joue_var)
        joueur_qui_joue_texte.pack()
        save = Button(frame3, text='Sauvegarder', command=self.sauvegarder)
        save.pack()

        self.update()
        self._root.mainloop()

    def parametrage(self):
        """
            Fonction qui crée la fenêtre de paramétrage du jeu
        """
        charger = messagebox.askquestion('Charger partie', "Voulez-vous charger une partie ?")
        if charger == 'yes':
            self.charger()
        else:
            self._temporaire = Tk()
            self._temporaire.geometry('400x500')
            self._taille = IntVar()
            self._nb_pion = IntVar()
            self._joueur_1 = StringVar()
            self._joueur_2 = StringVar()
            self._ordinateur = Variable()

            self._taille.set(8)
            self._nb_pion.set(4)
            self._joueur_1.set('joueur 1')
            self._joueur_2.set('joueur 2')
            self._ordinateur.set(True)

            text_barre = Label(self._temporaire, text='Dimension du plateau')
            text_barre.pack()
            barre = Scale(self._temporaire, variable=self._taille, from_=8, to=12, orient=HORIZONTAL)
            barre.pack()
            text_bouton = Label(self._temporaire, text='Nombre de pions à aligner pour gagner :')
            text_bouton.pack()

            bouton_4 = Checkbutton(self._temporaire, text="4", variable=self._nb_pion, onvalue=4)
            bouton_5 = Checkbutton(self._temporaire, text="5", variable=self._nb_pion, onvalue=5)
            bouton_6 = Checkbutton(self._temporaire, text="6", variable=self._nb_pion, onvalue=6)
            bouton_4.pack()
            bouton_5.pack()
            bouton_6.pack()

            joueur_1_text = Label(self._temporaire, text='Nom du premier joueur :')
            joueur_1_text.pack()
            joueur_1_nom = Entry(self._temporaire, textvariable=self._joueur_1)
            joueur_1_nom.pack()

            text_ordi = Label(self._temporaire, text='Voulez-vous jouer contre un ordinateur ?')
            text_ordi.pack()
            bouton_ordi_oui = Checkbutton(self._temporaire, text='Oui', variable=self._ordinateur, onvalue=True)
            bouton_ordi_oui.pack()
            bouton_ordi_non = Checkbutton(self._temporaire, text='Non', variable=self._ordinateur, onvalue=False)
            bouton_ordi_non.pack()

            joueur_2_text = Label(self._temporaire, text="Nom du deuxième joueur ou de l'ordinateur :")
            joueur_2_text.pack()
            joueur_2_nom = Entry(self._temporaire, textvariable=self._joueur_2)
            joueur_2_nom.pack()

            bouton_valider = Button(self._temporaire, text='Valider', command=self.valider)
            bouton_valider.pack()

            self._temporaire.mainloop()

    def valider(self):
        """
            Fonction qui permet de valider les paramètres du jeu et de lancer la partie
        """
        taille = self._taille.get()
        nb_pion = self._nb_pion.get()
        joueur_1 = self._joueur_1.get()
        joueur_2 = self._joueur_2.get()
        self._ordinateur = self._ordinateur.get()
        self._attribut_plateau = [taille, joueur_1, joueur_2, nb_pion]
        self._valider = True
        self._temporaire.destroy()


a = Affichage()
