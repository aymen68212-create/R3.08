"""
point.py
--------
Classe Point représentant un point dans un repère cartésien 2D.

UML :
+---------------------------+
|          Point            |
+---------------------------+
| - x : float              |
| - y : float              |
+---------------------------+
| + __init__(x=0, y=0)     |
| + distanceCoord(a, b)    |
| + distancePoint(camarade) |
+---------------------------+
"""

import math


class Point:
    """Représente un point dans un repère cartésien (x, y)."""

    def __init__(self, x: float = 0, y: float = 0):
        """
        Constructeur du Point.

        Args:
            x (float): Abscisse du point. Par défaut 0.
            y (float): Ordonnée du point. Par défaut 0.
        """
        self.x = x
        self.y = y

    def distanceCoord(self, a: float, b: float) -> float:
        """
        Calcule la distance entre ce point et un point donné par ses coordonnées.

        Args:
            a (float): Abscisse de l'autre point.
            b (float): Ordonnée de l'autre point.

        Returns:
            float: La distance euclidienne entre les deux points.
        """
        return math.sqrt((self.x - a) ** 2 + (self.y - b) ** 2)

    def distancePoint(self, camarade: "Point") -> float:
        """
        Calcule la distance entre ce point et un autre objet Point.

        Args:
            camarade (Point): L'autre point.

        Returns:
            float: La distance euclidienne entre les deux points.
        """
        return self.distanceCoord(camarade.x, camarade.y)

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"


# ──────────────────────────────────────────────
# Point d'entrée principal
# ──────────────────────────────────────────────

def main():
    # Création d'un point par défaut → origine (0, 0)
    p0 = Point()
    print(f"Point par défaut : {p0}")

    # Création d'un point avec coordonnées spécifiées
    p1 = Point(3.0, 4.0)
    print(f"Point p1 : {p1}")

    p2 = Point(6.0, 8.0)
    print(f"Point p2 : {p2}")

    # Distance via coordonnées
    d_coord = p1.distanceCoord(p2.x, p2.y)
    print(f"Distance p1 → p2 (via coordonnées) : {d_coord:.4f}")

    # Distance via objet Point
    d_point = p1.distancePoint(p2)
    print(f"Distance p1 → p2 (via objet Point) : {d_point:.4f}")

    # Distance de p1 à l'origine
    d_origine = p1.distancePoint(p0)
    print(f"Distance p1 → origine : {d_origine:.4f}")


if __name__ == "__main__":
    main()