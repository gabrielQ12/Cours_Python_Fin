#!/usr/bin/env python3
# coding: utf-8

import tkinter as tk
import web


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.monbouton = tk.Button(self)
        self.monbouton["text"] = "Cliquez ici"
        self.monbouton["command"] = self.dire_bonjour
        self.monbouton.pack()

    def dire_bonjour(self):
        print("Bonjour ! ")




root = tk.Tk()                     # Permet de créer une application.
root.title("Mon titre")            # Permet de choisir le titre de l'aplication.
root.geometry("1080x720")          # Permet de choisir la taille de la fenetre d'execution.
root.minsize(480,360)              # Permet de definir une taille minimal d'utilisation.
root.config(background="#d4d4d4")  # Permet de definir une couleur de fond.

# label = tk.Label(root, text="Mon label", font=("Arial", 35), bg="#000", fg="#fff")
# label.pack(side=tk.TOP)            # Permet de créer un widget dans la fenetre (avec diver configurations ).

# entry = tk.Entry(root, bd=3)
# entry.pack()                       # Permet de créer un champ de texte dans la fenetre (avec diver configurations ).

# button = tk.Button(text="Cliquez moi", command=dire_bonjour)
# button.pack()                      # Permet d'ajouter un bouton dans la fenetre / command permet d'ajouter une fonction au clicke.

application = Application(master=root)


application.mainloop()

# wc = web.WebCrawler(" une url")
# wc.crawl()

## Le prof utilise l'application PAGE (https://sourceforge.net/projects/page/) qui est très crade et ne fonctionne pas
## sous Linux Mint Victoria, qui est mon environement de travail, je vais donc utiliser le tamplate du prof