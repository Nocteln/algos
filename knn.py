# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('top14.csv', encoding='utf-8')

# def knn(poids, taille):
#     df['distance'] = (df['Taille'] - taille) ** 2 + (df['Poids'] - poids) ** 2
#     newdf = df.sort_values(by='distance', ascending=True)
    
#     # Sélectionner les 6 joueurs les plus proches
#     nearest_players = newdf.head(20)
    
#     # Créer un graphique de dispersion pour visualiser toutes les distances par rapport aux postes
#     plt.figure(figsize=(8, 5))
    
#     # Tracer tous les joueurs en bleu
#     plt.scatter(newdf['Poste'], newdf['distance'], color='blue', marker='o', label='Tous les joueurs')
    
#     # Tracer les 6 joueurs les plus proches en rouge
#     plt.scatter(nearest_players['Poste'], nearest_players['distance'], color='red', marker='o', label='6 joueurs les plus proches')
    
#     plt.title('Distances des joueurs par rapport au poste')
#     plt.xlabel('Poste')
#     plt.ylabel('Distance')
#     plt.xticks(rotation=45)
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# knn(93, 188)


import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons

# Données d'exemple
x_train , y_train = make_moons(100, noise=0.05, random_state=1)
x_test , y_test = make_moons(50, noise=0.12, random_state=1)
k = 2

def plot_knn(X_train, y_train, X_test, k):
    plt.figure(figsize=(10, 6))
    plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='coolwarm', label='Training Data')
    plt.scatter(X_test[:, 0], X_test[:, 1], color='black', marker='x', label='Test Data')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')

    for i in range(len(X_test)):
        distances = []
        for j in range(len(X_train)):
            distance = np.sqrt(np.sum(np.square(X_test[i] - X_train[j])))
            distances.append((distance, y_train[j]))
        distances.sort(key=lambda x: x[0])
        neighbors = [distances[i][1] for i in range(k)]
        majority_class = max(set(neighbors), key=neighbors.count)

        # plt.annotate(f'Predicted: {majority_class}', xy=(X_test[i][0], X_test[i][1]), xytext=(X_test[i][0]+0.5, X_test[i][1]+0.5),
        #              arrowprops=dict(facecolor='black', shrink=0.05))

    plt.legend()
    plt.title('KNN Classification')
    plt.show()

# Utilisation de la fonction pour afficher le graphe
plot_knn(x_train, y_train, x_test, k)
