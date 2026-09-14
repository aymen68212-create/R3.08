"""
cercle.py
---------
Classe Cercle représentant un cercle dans un repère cartésien 2D.
Dépend de la classe Point (point.py dans le même dossier).

UML :
+---------------------------------------+
|               Cercle                 |
+---------------------------------------+
| - centre : Point                     |
| - rayon  : float                     |
+---------------------------------------+
| + __init__(rayon, centre=Point(0,0)) |
| + diametre() -> float                |
| + perimetre() -> float               |
| + surface() -> float                 |
| + intersecte(autre) -> bool          |
| + contient_point(p) -> bool          |
+---------------------------------------+
"""

import math
from point import Point


class Cercle:
    """Représente un cercle défini par un centre (Point) et un rayon."""

    def __init__(self, rayon: float, centre: Point = None):
        """
        Constructeur du Cercle.

        Mode 1 — centre à l'origine :
            Cercle(rayon)
        Mode 2 — centre spécifié :
            Cercle(rayon, centre)

        Args:
            rayon (float): Le rayon du cercle.
            centre (Point, optional): Le centre du cercle. Par défaut Point(0, 0).
        """
        self.rayon = rayon
        # Si aucun centre n'est fourni, on utilise l'origine
        self.centre = centre if centre is not None else Point()

    def diametre(self) -> float:
        """
        Calcule le diamètre du cercle.

        Returns:
            float: Le diamètre (2 * rayon).
        """
        return 2 * self.rayon

    def perimetre(self) -> float:
        """
        Calcule le périmètre (circonférence) du cercle.

        Returns:
            float: Le périmètre (2 * π * rayon).
        """
        return 2 * math.pi * self.rayon

    def surface(self) -> float:
        """
        Calcule la surface (aire) du cercle.

        Returns:
            float: La surface (π * rayon²).
        """
        return math.pi * self.rayon ** 2

    def intersecte(self, autre: "Cercle") -> bool:
        """
        Détermine si ce cercle est en intersection avec un autre cercle.
        Deux cercles s'intersectent si la distance entre leurs centres
        est inférieure à la somme de leurs rayons.

        Args:
            autre (Cercle): L'autre cercle à tester.

        Returns:
            bool: True s'ils s'intersectent, False sinon.
        """
        distance_centres = self.centre.distancePoint(autre.centre)
        return distance_centres < (self.rayon + autre.rayon)

    def contient_point(self, p: Point) -> bool:
        """
        Détermine si un point appartient au cercle (est à l'intérieur ou sur le cercle).

        Args:
            p (Point): Le point à tester.

        Returns:
            bool: True si le point est dans le cercle, False sinon.
        """
        return self.centre.distancePoint(p) <= self.rayon

    def __str__(self) -> str:
        return f"Cercle(centre={self.centre}, rayon={self.rayon})"


# ──────────────────────────────────────────────
# Point d'entrée principal
# ──────────────────────────────────────────────

def main():
    # Mode 1 : cercle centré à l'origine, rayon 5
    c1 = Cercle(5)
    print(f"Cercle 1 : {c1}")
    print(f"  Diamètre  : {c1.diametre():.4f}")
    print(f"  Périmètre : {c1.perimetre():.4f}")
    print(f"  Surface   : {c1.surface():.4f}")

    # Mode 2 : cercle avec centre spécifié
    centre2 = Point(8, 0)
    c2 = Cercle(4, centre2)
    print(f"\nCercle 2 : {c2}")
    print(f"  Diamètre  : {c2.diametre():.4f}")
    print(f"  Périmètre : {c2.perimetre():.4f}")
    print(f"  Surface   : {c2.surface():.4f}")

    # Test d'intersection
    print(f"\nC1 et C2 s'intersectent : {c1.intersecte(c2)}")

    # Cercle loin → pas d'intersection
    c3 = Cercle(1, Point(100, 100))
    print(f"C1 et C3 s'intersectent : {c1.intersecte(c3)}")

    # Test appartenance d'un point
    p_dans   = Point(3, 3)
    p_dehors = Point(10, 10)
    print(f"\nLe point {p_dans} est dans C1  : {c1.contient_point(p_dans)}")
    print(f"Le point {p_dehors} est dans C1 : {c1.contient_point(p_dehors)}")


if __name__ == "__main__":
    main()