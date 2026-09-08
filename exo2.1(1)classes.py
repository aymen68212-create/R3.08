class Tasse:
    matière : str = "céramique"
    def __init__(self, couleur : str, contenance : float, marque : str):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque
    def __str__(self):
        return f"{self.couleur} {self.marque} {self.contenance}"

if __name__ == "__main__":
    mc = Tasse("bleue", 125, "toto")
    print(mc)
    print(vars(mc))
    print(mc.Tasse)
    print(mc.matière)
    print(Tasse.matière)
    mc.matière = "cuivre"
    print(mc.matière)
    print(Tasse.matière)
    print(vars(mc))
    print(mc.matière)