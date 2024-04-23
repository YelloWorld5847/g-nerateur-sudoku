from flask import Flask, render_template, request, send_file
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
import os

app = Flask(__name__)

def generate_sudoku_pdf(num_clues, nom):
    num_clues_str = str(num_clues)


    def sudoku_creat(num_clues):
        nombre_none = 0

        grille = [[None for _ in range(9)] for _ in range(9)]

        l = 0

        while l <= 8:
            c = 0
            while c <= 8:

                choice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                # print(f"grille {grille}")

                # print("test colonne :")
                # récupérer la colonne
                colonne = [ligne[c] for ligne in grille if ligne[c] is not None]

                # print(f"colonne : {colonne}")

                # supprimer des chois la colonne
                choice = [x for x in choice if x not in colonne]

                # print("\n")
                # print("test 3x3 :")

                start_row = (l // 3) * 3
                start_col = (c // 3) * 3

                for i in range(3):
                    for j in range(3):
                        element_carre = grille[start_row + i][start_col + j]
                        if element_carre != None:
                            # print(" ")
                            # print(f"choice3X3 : {choice}")
                            # print(element_carre)
                            if element_carre in choice:
                                choice.remove(element_carre)
                                # print(f"choice3X3_ : {choice}")

                # print("\n")
                # print("test ligne :")

                choice = [x for x in choice if x not in grille[l]]

                # print(f"choice : {choice}")

                if len(choice) >= 1:
                    # choisire un chiffre
                    chiffre = random.choice(choice)

                    # ajouter un chiffre
                    grille[l][c] = chiffre


                else:
                    nombre_none += 1
                    grille[l] = [None, None, None, None, None, None, None, None, None]
                    c = -1
                # if nombre_none % 5000 == 0:
                #    print("\n")
                #    for ligne in grille:
                #        print(ligne)

                c += 1
            l += 1

        def est_sudoku_valide(grille):
            # Vérifier les rangées
            for row in grille:
                if len(set(row)) != 9:  # La longueur de l'ensemble doit être 9 (chiffres uniques)
                    return False

            # Vérifier les colonnes
            for col in range(9):
                colonne = [grille[row][col] for row in range(9)]
                if len(set(colonne)) != 9:
                    return False

            # Vérifier les blocs 3x3
            for i in range(3):
                for j in range(3):
                    start_row = i * 3
                    start_col = j * 3
                    bloc = [
                        grille[start_row + r][start_col + c]
                        for r in range(3)
                        for c in range(3)
                    ]
                    if len(set(bloc)) != 9:
                        return False

            # Si tout est correct, la grille est un Sudoku valide
            return True

        def sudoku(grille, num_clues):


            indices = [(r, c) for r in range(9) for c in range(9)]
            random.shuffle(indices)
            for i in range(num_clues):
                row, col = indices.pop()
                grille[row][col] = "X"

            return grille

        if est_sudoku_valide(grille):

            return sudoku(grille, num_clues)
        else:
            print("X")

    sudoku_var1 = sudoku_creat(num_clues)
    sudoku_var2 = sudoku_creat(num_clues)
    sudoku_var3 = sudoku_creat(num_clues)
    sudoku_var4 = sudoku_creat(num_clues)

    sudoku_list = [sudoku_var1, sudoku_var2, sudoku_var3, sudoku_var4]


    # Fonction pour dessiner une seule grille de Sudoku
    def draw_sudoku_grid(c, sudoku, origin_x, origin_y, cell_size):
        # Dessiner les lignes
        for i in range(10):
            # Ligne horizontale
            thickness = 2 if i % 3 == 0 else 1
            c.setLineWidth(thickness)
            c.line(origin_x, origin_y + i * cell_size, origin_x + 9 * cell_size, origin_y + i * cell_size)

            # Ligne verticale
            c.line(origin_x + i * cell_size, origin_y, origin_x + i * cell_size, origin_y + 9 * cell_size)

        # Remplir les cases avec les valeurs de la matrice
        for row in range(9):
            for col in range(9):
                val = sudoku[row][col]
                if val != "X":  # Si ce n'est pas une case vide
                    # Centrer le texte dans la case
                    x_pos = origin_x + col * cell_size + cell_size / 3
                    y_pos = origin_y + (8 - row) * cell_size + cell_size / 3
                    c.drawString(x_pos, y_pos, str(val))

    # Exemples de grilles de Sudoku

    id = ''
    for i in sudoku_list:
        premier_ligne = i[0]
        string_numbers = map(str, premier_ligne)

        result = "".join(string_numbers)

        id += result + "_"

    id = id[:-1]

    nom_pdf = f"{nom}-{num_clues_str}-{id}.pdf"
    # Création du PDF
    c = canvas.Canvas(nom_pdf, pagesize=A4)

    # Taille des cases
    cell_size = 0.9 * cm

    # Positions des 4 grilles pour s'adapter au format A4
    positions = [
        (2 * cm, 18 * cm),  # Grille 1
        (11 * cm, 18 * cm),  # Grille 2
        (2 * cm, 8 * cm),  # Grille 3
        (11 * cm, 8 * cm),  # Grille 4
    ]

    # Dessiner les 4 grilles à leurs positions respectives
    for i in range(4):
        draw_sudoku_grid(c, sudoku_list[i], *positions[i], cell_size)

    c.setFont("Helvetica-Bold", 36)  # Police en gras, taille 36
    c.drawCentredString(A4[0] / 2, A4[1] - 2 * cm, num_clues_str)  # Centrer le texte en haut de la page

    # Finaliser le PDF
    c.showPage()
    c.save()

    return nom_pdf

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_clues_str = request.form['num_clues']
        num_clues = int(num_clues_str)
        nom = "sudoku_grids"
        pdf_file = generate_sudoku_pdf(num_clues, nom)

        return send_file(pdf_file, as_attachment=True, download_name=pdf_file)

    # Afficher le modèle HTML avec le lien vers le CSS
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)