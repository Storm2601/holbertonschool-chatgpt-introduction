#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calcule la factorielle d'un entier n.

    Args:
        n (int): Entier dont on veut calculer la factorielle.

    Returns:
        int: La factorielle de l'entier n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Récupération de l'argument de la ligne de commande
f = factorial(int(sys.argv[1]))
print(f)
