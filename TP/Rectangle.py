
from Point import Point


class Rectangle:

    def __init__(self,
                 origine: Point = None,
                 longueur: float = 1.0,
                 hauteur: float = 1.0):
        self.origine  = origine if origine is not None else Point()
        self.longueur = longueur
        self.hauteur  = hauteur

    @classmethod
    def depuis_coins(cls, bas_gauche: Point, haut_droit: Point) -> "Rectangle":
        longueur = haut_droit.x - bas_gauche.x
        hauteur  = haut_droit.y - bas_gauche.y
        return cls(bas_gauche, longueur, hauteur)

    # ── Calculs ───────────────────────────────────────────

    def surface(self) -> float:
        return self.longueur * self.hauteur

    def perimetre(self) -> float:
        return 2 * (self.longueur + self.hauteur)

    # ── Positions des coins ────────────────────────────────

    def coin_bas_gauche(self) -> Point:
        return Point(self.origine.x, self.origine.y)

    def coin_bas_droit(self) -> Point:
        return Point(self.origine.x + self.longueur, self.origine.y)

    def coin_haut_gauche(self) -> Point:
        return Point(self.origine.x, self.origine.y + self.hauteur)

    def coin_haut_droit(self) -> Point:
        return Point(self.origine.x + self.longueur, self.origine.y + self.hauteur)

    def contient_point(self, p: Point) -> bool:
        dans_x = self.origine.x <= p.x <= self.origine.x + self.longueur
        dans_y = self.origine.y <= p.y <= self.origine.y + self.hauteur
        return dans_x and dans_y

    def __str__(self) -> str:
        return (f"Rectangle(origine={self.origine}, "
                f"longueur={self.longueur}, hauteur={self.hauteur})")


# ──────────────────────────────────────────────
# Point d'entrée principal
# ──────────────────────────────────────────────

def main():
    # Mode 1 : rectangle par défaut
    r1 = Rectangle()
    print(f"Rectangle par défaut : {r1}")
    print(f"  Surface   : {r1.surface()}")
    print(f"  Périmètre : {r1.perimetre()}")

    # Mode 2 : tous les attributs spécifiés
    r2 = Rectangle(Point(1, 2), 6.0, 4.0)
    print(f"\nRectangle r2 : {r2}")
    print(f"  Surface   : {r2.surface()}")
    print(f"  Périmètre : {r2.perimetre()}")
    print(f"  Coin bas-gauche  : {r2.coin_bas_gauche()}")
    print(f"  Coin bas-droit   : {r2.coin_bas_droit()}")
    print(f"  Coin haut-gauche : {r2.coin_haut_gauche()}")
    print(f"  Coin haut-droit  : {r2.coin_haut_droit()}")

    # Mode 3 : depuis deux coins
    bg = Point(2, 3)
    hd = Point(7, 6)
    r3 = Rectangle.depuis_coins(bg, hd)
    print(f"\nRectangle r3 (depuis coins) : {r3}")
    print(f"  Surface   : {r3.surface()}")
    print(f"  Périmètre : {r3.perimetre()}")

    # Test appartenance d'un point
    p_dans   = Point(4, 4)
    p_dehors = Point(10, 10)
    print(f"\nLe point {p_dans} est dans r2  : {r2.contient_point(p_dans)}")
    print(f"Le point {p_dehors} est dans r2 : {r2.contient_point(p_dehors)}")


if __name__ == "__main__":
    main()