import sys


class Matrix:
    """
    • Le plus grand carré :
        ◦ Il s’agit de trouver le plus grand carré possible sur un plateau en
        évitant des obstacles.
        ◦ Un plateau vous est transmis dans un fichier passé en argument du
        programme.
        ◦ La première ligne du plateau contient les informations pour lire la
        carte :
            – Le nombre de lignes du plateau ;
            – Le caractère "vide" ;
            – Le caractère "obstacle" ;
            – Le caractère "plein".
        ◦ Le plateau est composé de lignes de ’caractère "vide"’ et de
        ’caractère "obstacle"’.
        ◦ Le but du programme est de remplacer les ’caractère "vide"’ par des
        ’caractère "plein"’ pour représenter le plus grand carré possible.
        ◦ Dans le cas où il y en a plusieurs solutions, on choisira de
        représenter le carré le plus en haut à gauche.
    """

    _matrix = None

    _rows = None
    _cols = None

    _empty = None
    _obstacle = None
    _filling = None

    def __init__(self, string=""):
        """
        • Carte valide :
            ◦ Toutes les lignes doivent avoir la même longueur.
            ◦ Il y a au moins une ligne d’au moins une case.
            ◦ À la fin de chaque ligne il y a un retour à la ligne.
            ◦ Les caractères présent dans la carte doivent être uniquement ceux
            présenté à la première ligne.
            ◦ En cas de carte invalide vous afficherez sur la sortie d’erreur:
            map error suivi d’un retour à la ligne puis il passera au traitement
            du plateau suivant.
        """

        # rows + empty + obstacle + filling + \n + one column + \n = 7 chars
        assert len(string) > 7, "Il y a au moins une ligne d’au moins une case."

        # Parse first line
        m = string[:-1].split("\n")
        *n, self._empty, self._obstacle, self._filling = m.pop(0)
        self._rows = int("".join(n))
        self._cols = len(m[0])
        # or raise ValueError

        assert len(m) is self._rows and all(
            len(r) is self._cols for r in m
        ), "Toutes les lignes doivent avoir la même longueur."

        assert all(set(r) <= set([self._empty, self._obstacle]) for r in m), (
            "Les caractères présent dans la carte doivent être uniquement ceux"
            "présenté à la première ligne."
        )

        self._matrix = m

    def print(self, title="") -> None:
        """ Print self on tty """
        if title:
            print(title)
        print("".join([row + "\n" for row in self._matrix]))

    def solve(self):
        (size, (right, bottom)) = self._calculate()
        self._fill(((right - size + 1, bottom - size + 1), (right + 1, bottom + 1)))

    def _calculate(self):
        """ calculate max square size """

        best = (0, (0, 0))  # size and bottom/right corners
        last_col = [0] * self._cols

        for i in range(self._rows):

            last_val = 0  # left border

            for j in range(self._cols):

                value = last_col[j]

                if self._matrix[i][j] is self._obstacle:
                    # if there is an obstacle square size is 0
                    last_col[j] = 0
                else:
                    # square of size min(top, left, top/left ) squares
                    last_col[j] = min(value, last_val, last_col[j - 1]) + 1

                # if this is the new best size.
                if best[0] < last_col[j]:
                    best = (last_col[j], (j, i))

                last_val = value

        return best

    def _fill(self, coords):
        """ fill out a rectangle represented by coords by appropriate chars """

        ((x1, y1), (x2, y2)) = coords

        for i in range(len(self._matrix)):
            if i in range(y1, y2):
                self._matrix[i] = (
                    self._matrix[i][:x1]
                    + self._filling * (x2 - x1)
                    + self._matrix[i][x2:]
                )


if __name__ == "__main__":

    print("\033c", end="")  # reset tty

    pname, *fnames = sys.argv

    if not fnames:
        print(f"Missing parameters.\nhelp: python3 {pname} map1.txt [map2.txt ...]")
        exit(1)

    for fname in fnames:
        with open(fname) as file:
            try:
                m = Matrix(file.read())
                m.print(f"Content of '{fname}':")
                m.solve()
                m.print("Best square:")
                input("Press any key for next map ...")
                print("\033c", end="")
            except (AssertionError, ValueError):
                print("Map error.")
                continue
