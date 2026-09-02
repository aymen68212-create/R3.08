def grand (a : float, b : float) -> float :
    """
        fonction qui retourne le plus grand nombre entre deux réels
    """
    if a < b :
        print(f"Le plus grand est {b}, donc b ")
    elif a > b :
        print(f"Le plus grand est {a}, donc a ")
    else :
        print(f"Aucun n'est plus grand que l'autre ")

a= float(input("Donnez un nombre "))
b= float(input("Donnez un nombre "))
grand(a, b)







