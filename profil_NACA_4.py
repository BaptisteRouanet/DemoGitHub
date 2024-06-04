# ----------------------------------------------------------------------------------------------------------------------
#
#       Génération et tracé de profil NACA 4 chiffres symétrique
#
# ----------------------------------------------------------------------------------------------------------------------


# Ce code a pour fonction de tracer le profil NACA à 4 chiffres selon
# les données entrèes par l'utilisateur

# — La corde du profil c est la distance entre le bord d’attaque et le bord de fuite
# — L’épaisseur maximale du profil t est un pourcentage de la corde. Le pourcentage
#   d’épaisseur t est donné par les deux derniers chiffres du code du profil.


import numpy as np
import matplotlib.pyplot as plt


# Tracer le profil NACA à partir des coordonnées (x,y).
def tracer_profil(x_up, x_down, y_up, y_down, epaisseur_max, type_calcul, i_max_epaisseur):

    # quelques parametre pour le graphique
    plt.rcParams['font.size'] = 14
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 100
    # Points de l'epaisseur max
    x_max = [x_up[i_max_epaisseur], x_down[i_max_epaisseur]]
    y_max = [y_up[i_max_epaisseur], y_down[i_max_epaisseur]]

    # données à tracer
    # Epaisseur max
    plt.plot(x_max, y_max, '--r', linewidth=2)
    plt.text(x_max[0]*1.1, 0+0.05*y_max[0], "Epaisseur maximum du profil", fontsize='small', fontstyle='italic', color='r')
    # Intra et Extrados
    plt.plot(x_up, y_up, label="Extrados", linewidth=3)
    plt.plot(x_down, y_down, label="Intrados", linewidth=3)

    # Titres, cadrillage et legend
    plt.title(f'Profil NACA00{epaisseur_max} - {type_calcul}')
    plt.savefig(f'Profil_NACA00{epaisseur_max}-{type_calcul}.pdf')
    plt.savefig(f'Profil_NACA00{epaisseur_max}-{type_calcul}.png')
    plt.legend()
    plt.grid(color='k', linestyle='-', linewidth=1)
    plt.xlabel("Corde")
    plt.ylabel("Epaisseur")

    # Affichage
    plt.show()


# Créer un tableau des coordonnées a partir des valeurs demandées à l'utilisateur.
def construire_coordonnees(derniers_digits, corde, nbr_points, type_distrib):
    t_max = derniers_digits/100
    y_t = np.zeros(nbr_points)

    # Calcul lineaire
    if type_distrib == 1:
        type_calcul = "Lineaire"
        x_c = np.linspace(0, 1, nbr_points - 1, dtype=float)
        x_c = np.append(x_c, 1.0)
        for i in range(nbr_points):
            y_t[i] = 5 * t_max * (0.2969 * np.sqrt(x_c[i]) - 0.1260 * x_c[i] - 0.3516 * x_c[i] ** 2 + 0.2843 * x_c[i] ** 3 - 0.1036 * x_c[i] ** 4)

    # Calcul non-uniforme
    else:
        type_calcul = "Non-uniforme"
        theta_points = np.linspace(0, np.pi, nbr_points - 1, dtype=float)
        theta_points = np.append(theta_points, np.pi)
        x_c = np.zeros_like(theta_points)
        for i in range(nbr_points):
            x_c[i] = 0.5 * (1 - np.cos(theta_points[i]))
            y_t[i] = 5 * t_max * (0.2969 * np.sqrt(x_c[i]) - 0.1260 * x_c[i] - 0.3516 * x_c[i] ** 2 + 0.2843 * x_c[i] ** 3 - 0.1036 * x_c[i] ** 4)

    # tables de coordonnées des points des courbes à tracer
    x_up = x_c * corde
    x_down = x_c * corde
    y_up = y_t * corde
    y_down = -y_t * corde

    return x_up, x_down, y_up, y_down, type_calcul


# Trouver l'epaisseur maximum du profil à partir des coordonnées construites.
def trouver_epaisseur_max(x_up, y_up):
    print("L'épaisseur maximum du profil est :")
    return float(x_up[np.argmax(y_up)]), np.argmax(y_up)


# Lance les fonctions avec les entrées utilisateur pour obtenir les données de sortie demandées
def lancer_code():
    # Lancement du code
    print("Ce code permet de tracer un profil NACA 4 digit symétrique.\n"
          "Pour cela il faudra fournir les deux derniers digits : NACA00XX\n"
          "Ils représentent le pourcentage de corde à laquelle se trouve l’épaisseur maximale du profil\n"
          "Il sera également demandé la corde du profil (la distance entre les bords d'attaque et de fuite.\n")
    # Input des entrées (corde, deux digits, nbr de point et type de calcul)
    corde = float(input("Quel est la corde 'c' (Ex: c = 12.4) ?    c = "))
    derniers_digits = int(input("Quels sont les deux derniers digits 'NACA00XX' (Ex: NACA0045 --> t = 45) ?    t = "))
    nbr_points = int(input("Combien de points souhaitez vous pour la précision ?   n = "))
    type_distrib = int(input("Quel type de distribution souhaitez vous (linéaire = 1 / non-uniforme = 2)?   1/2 = "))
    # On récupère les données calculées à l'aide des données en input et la fonction construire_coordonnees
    x_up, x_down, y_up, y_down, type_calcul = construire_coordonnees(derniers_digits, corde, nbr_points, type_distrib)
    # On récupère et affiche l'épaisseur max à l'aide de trouver_epaisseur_max
    x_max_epaisseur, i_max_epaisseur = trouver_epaisseur_max(x_up, y_up)
    print(f"%.2f" % x_max_epaisseur)
    # On trace le profil
    tracer_profil(x_up, x_down, y_up, y_down, derniers_digits, type_calcul, i_max_epaisseur)


# Appel de la fonction pour lancer le code
lancer_code()
