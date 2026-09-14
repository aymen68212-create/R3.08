"""
triangle_rectangle.py
---------------------
Classe TriangleRectangle représentant un triangle rectangle dans un repère 2D.
Dépend de la classe Point (point.py dans le même dossier).

UML :
+--------------------------------------------+
|          TriangleRectangle                 |
+--------------------------------------------+
| - cote1        : float                    |
| - cote2        : float                    |
| - angle_droit  : Point                    |
+--------------------------------------------+
| + __init__(cote1, cote2, angle_droit=...) |
| + hypothenuse() -> float                  |
| + perimetre()   -> float                  |
| + surface()     -> float                  |
| + est_isocele() -> bool                   |
+--------------------------------------------+
"""

import math
from point import Point


class TriangleRectangle:
    """
    Représente un triangle rectangle.
    Les deux petits côtés (cathètes) sont adjacents à l'angle droit,
    dont la position est donnée par un Point.
    """

    def __init__(self,
                 cote1: float,
                 cote2: float,
                 angle_droit: Point = None):
        """
        Constructeur du TriangleRectangle — 2 modes d'utilisation :

        Mode 1 — angle droit à l'origine :
            TriangleRectangle(cote1, cote2)
            → angle_droit initialisé à Point(0, 0)

        Mode 2 — angle droit spécifié :
            TriangleRectangle(cote1, cote2, angle_droit)

        Args:
            cote1 (float)              : Longueur du premier côté de l'angle droit.
            cote2 (float)              : Longueur du second côté de l'angle droit.
            angle_droit (Point, optional): Position du sommet de l'angle droit.
                                          Par défaut Point(0, 0).
        """
        self.cote1       = cote1
        self.cote2       = cote2
        self.angle_droit = angle_droit if angle_droit is not None else Point()

    def hypothenuse(self) -> float:
        """
        Calcule la longueur de l'hypoténuse via le théorème de Pythagore.

        Returns:
            float: √(cote1² + cote2²)
        """
        return math.sqrt(self.cote1 ** 2 + self.cote2 ** 2)

    def perimetre(self) -> float:
        """
        Calcule le périmètre du triangle rectangle.

        Returns:
            float: cote1 + cote2 + hypoténuse.
        """
        return self.cote1 + self.cote2 + self.hypothenuse()

    def surface(self) -> float:
        """
        Calcule la surface (aire) du triangle rectangle.

        Returns:
            float: (cote1 × cote2) / 2
        """
        return (self.cote1 * self.cote2) / 2

    def est_isocele(self) -> bool:
        """
        Détermine si le triangle rectangle est isocèle.
        Un triangle rectangle isocèle a ses deux cathètes de même longueur.

        Returns:
            bool: True si cote1 == cote2, False sinon.
        """
        return math.isclose(self.cote1, self.cote2)

    def __str__(self) -> str:
        return (f"TriangleRectangle(cote1={self.cote1}, cote2={self.cote2}, "
                f"angle_droit={self.angle_droit})")


# ──────────────────────────────────────────────
# Point d'entrée principal
# ──────────────────────────────────────────────

def main():
    # Mode 1 : angle droit à l'origine par défaut
    t1 = TriangleRectangle(3.0, 4.0)
    print(f"Triangle 1 : {t1}")
    print(f"  Hypoténuse : {t1.hypothenuse():.4f}")
    print(f"  Périmètre  : {t1.perimetre():.4f}")
    print(f"  Surface    : {t1.surface():.4f}")
    print(f"  Isocèle    : {t1.est_isocele()}")

    # Mode 2 : angle droit spécifié
    angle = Point(2, 5)
    t2 = TriangleRectangle(6.0, 6.0, angle)
    print(f"\nTriangle 2 : {t2}")
    print(f"  Hypoténuse : {t2.hypothenuse():.4f}")
    print(f"  Périmètre  : {t2.perimetre():.4f}")
    print(f"  Surface    : {t2.surface():.4f}")
    print(f"  Isocèle    : {t2.est_isocele()}")

    # Triangle isocèle classique 45-45-90
    t3 = TriangleRectangle(5.0, 5.0)
    print(f"\nTriangle 3 (isocèle attendu) : {t3}")
    print(f"  Isocèle : {t3.est_isocele()}")


if __name__ == "__main__":
    main()
