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