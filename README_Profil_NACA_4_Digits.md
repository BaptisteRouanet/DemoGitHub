# Profil NACA 4 digits

**_Objectifs_** :

Ce programme python a pour objectif de tracer un profil NACA00XX _(4 digits, symétrique)_ selon les paramètres choisis par l'utilisateur. 

**Entrées**

L’utilisateur devra fournir :
- Numéro du profil NACA 4 chiffres symétrique
- Corde du profil (en mètre)
- Nombre de points le long de la corde pour le tracé
- Le type de distribution de points le long de la corde : *linéaire* ou *non-uniforme* 

**Sorties**

Le code donne :
- Le graphique du profil
- La position sur la corde de l'épaisseur maximum

Le programme créer également deux fichier enrgistrant le profil calculé, un _.pdf_ et un _.png_, avec le nom du profil et le type de distribution choisi.

**Modules utilisés**

*numpy, matplotlib.pyplot*

**_Fonctions utilisées_** :

**tracer_profil() :**

Trace le profil NACA à partir des données d'entrée. 
Trace également un segment à l'emplacement de l'epaisseur maximum du profil.
- *Entrées : x_up, x_down, y_up, y_down, epaisseur_max, type_calcul, i_max_epaisseur*
- *Sorties : le graphique*

**construire_coordonnees() :**

Donne les tables des coordonnées x et y des intrados/extrados selon les paramètres d'entrée données par l'utilisateur.
Distinction de cas selon le type de distribution *linéaire* ou *non-uniforme*.
- *Entrées : derniers_digits, corde, nbr_points, type_distrib*
- *Sorties : x_up, x_down, y_up, y_down, type_calcul*

**trouver_epaisseur_max() :**

Donne la position sur la corde et l'indice dans les tables du maximum de l'épaisseur.
- *Entrées : x_up, y_up*
- *Sorties : x_max_epaisseur, i_max_epaisseur*

**lancer_code() :**

Demande les données d'entrée à l'utilisateur et fait appelle aux fonctions précédentes pour fournir les sorties présenté en entête.
- *Entrées : input de l'utilisateur (corde, 2 derniers digits du profil NACA, nombre de poitns de calcul, type de distribution)*
- *Sorties : le graphique, la position sur la corde de l'épaisseur maximum*

Fait appelle à :
- **tracer_profil()**
- **construire_coordonnees()**
- **trouver_epaisseur_max()**

## Cas d'utilisation 

Le code va demander tous les paramètres nécessaires en précisant la forme demandée. 

Typiquement :
- c (corde) = un nombre flotant
- 2 derniers digits = un entier de 2 digits
- nombre de points = entier compris entre 10 et 100 000, en dehors de ces extremes le code n'est pas assuré de fonctionner
- type de distribution = 1 ou 2 *(distribution des points de calcul selon x et la valeur associé en y)*
   - entier 1 = distribution linéaire
   - entier 2 = distribution non-uniforme des points de calcul (selon la transformée de Glauert _0.5*(1 − cos θ)_, avec tetha variant entre 0 et pi)

*Si l'utilisateur sort du cadre d'utilisation précisé il s'engage à assumer les erreurs pouvant avoir lieux.*
