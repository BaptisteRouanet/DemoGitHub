# Ce programme est un jeu du pendu
# Le programme propose de trouver un mot à partir d'un fichier de mots

# fonction importer_random_mot
import random
import unicodedata
import os


def trouver_mot(mot, nbre_essais=6):
    mot_vide = ['_' for _ in range(len(mot))]
    lst_mot = [mot[i] for i in range(len(mot))]
    i = nbre_essais
    nbr_lettres_restantes = len(mot)
    lettres_util = []
    while i > 0:
        lettre = input(f"Quelle lettre choisissez vous ?   ")
        if trouver_lettre(lettre, lst_mot):
            [mot_vide, nbr_lettres_restantes] = changer_lettre(lettre, mot_vide, lst_mot, nbr_lettres_restantes)
            print("Bravo ! La lettre est ajoutée, nous avons maintenant :\n"
                  f"{mot_vide}\n")
            lettres_util.append(lettre)
            print(f"Il reste {i}/{nbre_essais} essais\n"
                  f"Rappel des lettres utilisées : {lettres_util}\n")
            if nbr_lettres_restantes == 0:
                print(f"Bravo ! Vous avez trouvé le mot '{mot}'.")
                recommencer()
        else:
            print("Dommage :( . La lettre n'est pas dans le mot\n"
                  f"Pour rappel nous avons {mot_vide}")
            lettres_util.append(lettre)
            i -= 1
            print(f"Il reste {i}/{nbre_essais} essais\n"
                  f"Rappel des lettres utilisées : {lettres_util}\n")
    print(f"Le mot était : {mot}")
    recommencer()


def trouver_lettre(lettre, lst_mot):  # fonction verifier que la lettre est dans le mot
    for i in range(len(lst_mot)):
        if lst_mot[i] == lettre:
            return True
    return False


def changer_lettre(lettre, mot_vide, lst_mot, nbr_lettres_restantes):  # fonction ajouter la lettre dans le mot vide
    for i in range(len(lst_mot)):
        if lst_mot[i] == lettre:
            mot_vide[i] = lettre
            nbr_lettres_restantes -= 1
    return [mot_vide, nbr_lettres_restantes]


def recommencer():
    ask_restart = input(f"Voulez vous reessayer avec un autre mot ?\n Oui/Non   ")
    if ask_restart == "Oui" or ask_restart == "oui":
        new_mot = donner_mot()
        ask_nbre_essais = input(f"Voulez vous changer le nombre d'essais possibles ?\n Oui/Non   ")
        if ask_nbre_essais == "Oui" or ask_nbre_essais == "oui":
            nbre_essais = int(input(f"Entrez le nombre d'essais souhaités pour cet essais :   "))
            trouver_mot(new_mot, nbre_essais)
        else:
            trouver_mot(new_mot)
    else:
        print("Merci d'avoir joué. A bientôt!")
        quit()


def donner_mot():
    ask_trouver_fichier = input(f"Voulez vous importer les mots d'un de vos fichier .txt ?\nOui/Non   ")
    if ask_trouver_fichier == "Oui" or ask_trouver_fichier == "oui":
        ask_chemin_fichier = input(f"Quel est l'emplacement du fichier ? :  ")
        ask_nom_fichier = input(f"Quel est le nom du fichier ? :   ")
        chemin = ask_chemin_fichier + os.sep + ask_nom_fichier + '.txt'
        test_chemin = os.path.isfile(chemin)
        if test_chemin:
            return choisir_mot(chemin)
    else:
        return choisir_mot()


def choisir_mot(chemin="mots_pendu.txt"):
    with open(chemin, "r", encoding='utf-8') as text_file:
        lines = text_file.read().split()
        lines_decode = []
        for line in lines:
            lines_decode.append(unicodedata.normalize('NFD', line).encode('ascii', 'ignore').decode("utf-8"))
    return random.choice(lines_decode)

print("Bonjour, ce code permet de jouer au 'Jeu du pendu'.\n"
      "Vous avez la possibilité d'importer votre propre set de mot.\n"
      "Pour cela donnez dans les phases suivantes l'accés au fichier sous la forme :\n"
      r"Chemin = C:\User et Nom = Fichier "+"\nLe code s'occupera du reste.\nAmusez vous bien !")
trouver_mot(donner_mot())
