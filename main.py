import numpy  as np
import time

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



def compute_next_frame(frame):
    padded_frame = np.pad(frame, 1, mode="constant")

    # Créer une nouvelle frame pour les modifications
    nouvelle_frame = frame.copy()

    # Étape 1 : Parcourir la matrice
    for i in range(1, padded_frame.shape[0] - 1):
        for j in range(1, padded_frame.shape[1] - 1):
            # Étape 2 : Calculer le nombre de voisins
            number_neighbors = compute_number_neighbors(padded_frame, i, j)
            
            # Étape 3 : Application des règles du jeu de la vie
            if padded_frame[i, j] == 1:
                # Une cellule vivante meurt si elle a moins de 2 ou plus de 3 voisins vivants
                if number_neighbors < 2 or number_neighbors > 3:
                    nouvelle_frame[i-1, j-1] = 0
            else:
                # Une cellule morte devient vivante si elle a exactement 3 voisins vivants
                if number_neighbors == 3:
                    nouvelle_frame[i-1, j-1] = 1
    
    return nouvelle_frame





while True:
    afficher_grille(frame)
    frame = compute_next_frame(frame)

# Pause pour observer les changements (sinon la boucle sera trop rapide)
   
    time.sleep(1)    