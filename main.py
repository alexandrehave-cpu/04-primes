from math import sqrt

def isprime(p):
    """
    Détermine si un nombre entier est premier.

    Un nombre premier est un entier naturel supérieur ou égal à 2
    qui n'admet exactement que deux diviseurs distincts : 1 et lui-même.

    Args:
        p (int): Nombre entier à tester.

    Returns:
        bool: True si p est un nombre premier, False sinon.

    Examples:
        >>> isprime(2)
        True
        >>> isprime(4)
        False
        >>> isprime(17)
        True
    """
    if p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False

    for i in range(3, int(sqrt(p)) + 1, 2):
        if p % i == 0:
            return False
    return True


def main():
    """
    Fonction principale du programme.

    Parcourt les entiers de 0 à 99 et affiche ceux qui sont premiers.
    Cette fonction sert à tester visuellement la validité de isprime().

    Returns:
        None

    Example:
        >>> main()
        2, 3, 5, 7, 11, 13, 17, ...
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()  # retour à la ligne final


if __name__ == "__main__":
    main()

