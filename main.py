# -*- coding: utf-8 -*-
"""
Made in Marseille

@author: Raphael
"""
# email : raphael.attias@laplateforme.io

import tkinter as tk
import json

# Charger les données du code Morse à partir du fichier "Décodage.json"
try:
    with open("Décodage.json", "r") as fichier:
        data = json.load(fichier)
except Exception as e:
    print(f"Erreur lors du chargement des données du code Morse : {e}")
    data = {}

# Fonction pour déchiffrer un message en code Morse
def decoder_message(message):
    mots = message.split('   ')  # Séparer les mots
    message_decode = ""

    for mot in mots:
        lettres = mot.split(' ')  # Séparer les lettres
        for lettre in lettres:
            if lettre in data.values():
                for cle, valeur in data.items():
                    if valeur == lettre:
                        message_decode += cle
            else:
                message_decode += lettre
        message_decode += ' '

    return message_decode.strip()

# Fonction pour gérer les clics sur les boutons
def bouton_clique(valeur):
    entry_var.set(entry_var.get() + str(valeur))

# Fonction pour réinitialiser le temporisateur après chaque action
def reset_timer():
    fenetre.after(1050, ajouter_espace)

# Fonction pour ajouter un espace
def ajouter_espace():
    entry_var.set(entry_var.get() + ' ')

# Fonction pour effacer
def effacer():
    entry_var.set("")

# Fenêtre principale
fenetre = tk.Tk()
fenetre.geometry("500x500")
fenetre.title("Décodeur de code Morse")

entry_var = tk.StringVar()
entry = tk.Entry(fenetre, textvariable=entry_var, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10, ipadx=10, ipady=10)

# Boutons pour l'entrée du code Morse
btn_court = tk.Button(fenetre, text='.', width=5, font=("Arial", 15), command=lambda: bouton_clique('.'))
btn_court.grid(row=1, column=0)

btn_long = tk.Button(fenetre, text='-', width=5, font=("Arial", 15), command=lambda: bouton_clique('-'))
btn_long.grid(row=1, column=1)

# Bouton pour décoder le message
btn_decoder = tk.Button(fenetre, text='Décoder', width=10, font=("Arial", 15), command=lambda: entry_var.set(decoder_message(entry_var.get())))
btn_decoder.grid(row=1, column=2)

# Bouton pour effacer les entrées
boutoneffacer = tk.Button(fenetre, text="Suppr", width=4, command=effacer, bg="red")
boutoneffacer.grid(row=1, column=3)

# Bouton pour ajouter un espace
bouton_espace = tk.Button(fenetre, text="Espace", width=6, command=lambda: bouton_clique(' '))
bouton_espace.grid(row=2, column=0)

fenetre.mainloop()
