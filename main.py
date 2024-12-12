#### Imports et définition des variables globales
"""Imports et définition des variables globales"""
import sys
sys.setrecursionlimit(1500)

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s :
        return[]

    encoded =[]
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    encoded.append((current_char, count))
    return encoded


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici

    # cas de base
    if not s :
        return[]
    # recherche nombre de caractères identiques au premier
    first_char = s[0]
    count = 1
    while count < len(s) and s[count] == first_char:
        count += 1
    # appel récursif
    return [(first_char, count)] + artcode_r(s[count:])

#### Fonction principale
def main():
    """Fonction principale"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
