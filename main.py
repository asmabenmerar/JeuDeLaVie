import numpy  as np

frame = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])
def afficher_grille(grille):
    for index_ligne in range(len(grille)):
        ligne = grille[index_ligne]
        for index_cellule in range(len(ligne)):
            cellule = ligne[index_cellule]
            print(cellule, end='')
        print() #saut de ligne apres chaque ligne
    print() #saut de ligne apres toute la grille
afficher_grille(frame)



def compute_number_neighbors(padded_frame, index_line, index_colomn):
    #calculer le nombre de voisins vivants
    number_neighbors = 0
    for ligne in range(index_line - 1, index_line +2):
        for colonne in range(index_colomn - 1, index_colomn + 2):
            if (ligne != index_line or colonne != index_colomn):
                number_neighbors += padded_frame[ligne, colonne]
        return number_neighbors 