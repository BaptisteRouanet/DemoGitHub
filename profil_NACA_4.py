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
def tracer_profil(x_up, x_down, y_up, y_down, epaisseur_max):
    print('on rentre dans tracer profil')
    # quelques parametre pour le graphique
    plt.rcParams['font.size'] = 14
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 100

    # données à tracer
    plt.plot(x_up, y_up, label="Extrados")
    plt.plot(x_down, y_down, label="Intrados")
    plt.title(f'Profil NACA00{epaisseur_max}')
    plt.savefig(f'Profil NACA00{epaisseur_max}.pdf')
    plt.savefig(f'Profil NACA00{epaisseur_max}.png')
    plt.show()


# Créer un tableau des coordonnées a partir des valeurs demandées à l'utilisateur.
def construire_coordonnees(derniers_digits, corde, nbr_points, type_distrib):
    print('on rentre dans construire coordonnees')
    t_max = derniers_digits/100
    y_t = np.zeros(nbr_points)
    if type_distrib == 1:
        x_c = np.arange(0, 1, 1 / (nbr_points - 1), dtype=float)
        x_c = np.append(x_c, 1.0)
        for i in range(nbr_points):
            y_t[i] = 5 * t_max * (0.2969 * np.sqrt(x_c[i]) - 0.1260 * x_c[i] - 0.3516 * x_c[i] ** 2 + 0.2843 * x_c[i] ** 3 - 0.1036 * x_c[i] ** 4)
    else:
        theta_points = np.arange(0, np.pi, 1 / (nbr_points - 1), dtype=float)
        theta_points = np.append(theta_points, np.pi)
        print(theta_points)
        x_c = np.zeros_like(theta_points)
        for i in range(nbr_points):
            x_c[i] = 0.5 * (1 - np.cos(theta_points[i]))
            y_t[i] = 5 * t_max * (0.2969 * np.sqrt(x_c[i]) - 0.1260 * x_c[i] - 0.3516 * x_c[i] ** 2 + 0.2843 * x_c[i] ** 3 - 0.1036 * x_c[i] ** 4)
    x_up = x_c * corde
    x_down = x_c * corde
    y_up = y_t * corde
    y_down = -y_t * corde
    return x_up, x_down, y_up, y_down


# Trouver l'epaisseur maximum du profil à partir des coordonnées construites.
def trouver_epaisseur_max(x_up, y_up):
    print('on rentre dans epaisseur max')
    return float(x_up[np.argmax(y_up)])


# Lance les fonctions avec les entrées utilisateur pour obtenir les données de sortie demandées
def lancer_code():
    print("Ce code permet de tracer un profil NACA 4 digit symétrique.\n"
          "Pour cela il faudra fournir les deux dernier digits : NACA00XX\n"
          "Ils représentent le pourcentage de corde à laquelle se trouve l’épaisseur maximale du profil\n"
          "Il sera également demandé la corde du profil (la distance entre les bords d'attaque et de fuite.\n")
    corde = float(input("Quel est la corde 'c' (Ex: c = 12.4) ?    c = "))
    derniers_digits = int(input("Quels sont les deux derniers digits 'NACA00XX' (Ex: NACA0045 --> t = 45) ?    t = "))
    nbr_points = int(input("Combien de points souhaitez vous pour la précision ?   n = "))
    type_distrib = int(input("Quel type de distribution souhaitez vous (linéaire = 1 / non-uniforme = 2)?   1/2 = "))
    x_up, x_down, y_up, y_down = construire_coordonnees(derniers_digits, corde, nbr_points, type_distrib)
    print(trouver_epaisseur_max(x_up, y_up))
    tracer_profil(x_up, x_down, y_up, y_down, derniers_digits)


lancer_code()
