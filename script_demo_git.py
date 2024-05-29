"""
def hello_world() :
    print('Hello World!')

hello_world()

def fonction_inutile():
    print('Hey !')

fonction_inutile()
"""
def calculer_factorielle(n):
    if n == 0:
        return 1
    elif n>0 :
        return n*calculer_factorielle(n-1)
    else :
        print("Ce cas n'est pas pris en compte")
# print(calculer_factorielle(10))

def calculer_approximé_erf(x,nmax=10):
    from math import pi
    result = 0
    for n in range(nmax):
        result += ((-1)**n * x**(2*n+1))/((2*n+1)*calculer_factorielle(n))
    result = result*2/(pi**0.5)
    return result

print(calculer_approximé_erf(2.3,25))

import sys

weight = 70
if weight < 80:
    sys.exit("weight less than 80")
else:
    print("weight is not less than 80")


