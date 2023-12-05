# -*- coding: utf-8 -*-
"""
Made in Marseille
@author: Raphael
"""
#email : raphael.attias@laplateforme.io

import hashlib
import json
import random
import string

def charger_mots_de_passe(chemin):
    try:
        with open(chemin, 'r') as fichier_json:
            data = json.load(fichier_json)
            return data.get("passwords", {})
    except FileNotFoundError:
        return {}

def sauvegarder_mots_de_passe(chemin, mots_de_passe):
    data = {"passwords": mots_de_passe}
    with open(chemin, 'w') as fichier_json:
        json.dump(data, fichier_json)

def generer_mot_de_passe():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    while True:
        mot_de_passe = ''.join(random.choice(caracteres) for _ in range(12))
        if (any(c.islower() for c in mot_de_passe) and
            any(c.isupper() for c in mot_de_passe) and
            any(c.isdigit() for c in mot_de_passe) and
            any(c in string.punctuation for c in mot_de_passe)):
            return mot_de_passe

def afficher_mot_de_passe(libelle):
    mots_de_passe_existants = charger_mots_de_passe("base.json")
    mot_de_passe = mots_de_passe_existants.get(libelle)
    if mot_de_passe:
        print(f"Mot de passe pour '{libelle}' : {mot_de_passe}")
    else:
        print(f"Aucun mot de passe trouvé pour le libellé '{libelle}'.")

def ajouter_mot_de_passe():
    libelle = input("Libellé du mot de passe : ")
    
    # Vérifier si le mot de passe existe déjà
    mots_de_passe_existants = charger_mots_de_passe("base.json")
    if libelle in mots_de_passe_existants:
        print("Un mot de passe avec ce libellé existe déjà.")
        return

    a = 0
    while a < 4:
        choix_generer = input("Voulez-vous générer un mot de passe aléatoire ? (O/N) : ")
        if choix_generer.upper() == "O":
            pwd = generer_mot_de_passe()
            print(f"Mot de passe généré : {pwd}")
            break
        elif choix_generer.upper() == "N":
            pwd = input("Entrez votre mot de passe : ")
            break
        else:
            print("Choix invalide, veuillez répondre par O ou N.")

    if len(pwd) < 8:
        print("Mot de passe trop court")
        return

    if any(char in pwd for char in "!@#$%^&*"):
        a += 1
    else:
        print("Aucun caractère spécial trouvé")

    if any(char.isupper() for char in pwd):
        a += 1
    else:
        print("Au moins une lettre majuscule est requise")

    if any(char.islower() for char in pwd):
        a += 1
    else:
        print("Au moins une lettre minuscule est requise")

    if any(char.isalpha() or char.isdigit() for char in pwd):
        a += 1
    else:
        print("Le mot de passe ne peut contenir que des lettres et des chiffres")

    print("Mot de passe est bien Safe")
    # Hash du mot de passe
    h = hashlib.sha256(pwd.encode('UTF-8'))
    hashed_pwd = h.hexdigest()
    chemin_mots_de_passe = "base.json"
    mots_de_passe_existants[libelle] = hashed_pwd
    sauvegarder_mots_de_passe(chemin_mots_de_passe, mots_de_passe_existants)
    print("Mot de passe ajouté avec succès!")

def verifie_mot_de_passe():
    a = 0
    while a < 4:
        pwd = input("Entrez votre mot de passe : ")
        if len(pwd) < 8:
            print("Mot de passe trop court")
            return

        if any(char in pwd for char in "!@#$%^&*"):
            a += 1
        else:
            print("Aucun caractère spécial trouvé")

        if any(char.isupper() for char in pwd):
            a += 1
        else:
            print("Au moins une lettre majuscule est requise")

        if any(char.islower() for char in pwd):
            a += 1
        else:
            print("Au moins une lettre minuscule est requise")

        if any(char.isalpha() or char.isdigit() for char in pwd):
            a += 1
        else:
            print("Le mot de passe ne peut contenir que des lettres et des chiffres")

        print("Mot de passe est bien Safe")

print("  _____                                    _ ")
print(" |  __ \                                  | |")
print(" | |__) |_ _ ___ _____      _____  _ __ __| |")
print(" |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |")
print(" | |  | (_| \__ \__ )\ V  V / (_) | | | (_| |")
print(" |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|")

# Menu
while True:
    print("\nSélectionnez une option")
    print("1. Ajouter un nouveau mot de passe")
    print("2. Afficher un mot de passe existant")
    print("3. Vérifie ton mot de passe")
    print("q. Quitter")
    
    choix = input("Entrez 1-2-q : ")

    # Gestion du menu
    if choix == "1":
        ajouter_mot_de_passe()
    
    elif choix == "2":
        libelle = input("Entrez le libellé du mot de passe que vous souhaitez afficher : ")
        afficher_mot_de_passe(libelle)
    
    elif choix == "3":
        verifie_mot_de_passe()

    elif choix.lower() == "q":
        break

    else:
        print("Choix invalide, veuillez réessayer.")
