#### Imports et définition des variables globales
"""
Ce programme teste et encode des chaînes de caractères
"""
# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères
       passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if s=="":
        return []
    tab=[]
    nb_occ=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            nb_occ=nb_occ+1
        else:
            tab.append((s[i-1],nb_occ))
            nb_occ=1
    tab.append((s[-1],nb_occ))
    return tab

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères
       passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if s=="":
        return []
    nb_occ=1
    while nb_occ<len(s) and s[nb_occ]==s[0]:
        nb_occ=nb_occ+1
    return [(s[0],nb_occ)]+artcode_r(s[nb_occ:])

#### Fonction principale

def main():
    """
    Cette fonction teste si le programme affiche le bon tableau d'occurrences
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
