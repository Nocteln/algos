import numpy as np
from collections import Counter
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def euclidean_distance(x1, x2):
    distance = np.sqrt(np.sum((x1 - x2) ** 2))
    return distance

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions

    def _predict(self, x):
        # Calcul de la distance
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]

        # Sélection des k plus proches voisins
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # Vote majoritaire pour la classification
        most_common = Counter(k_nearest_labels).most_common()
        return most_common[0][0]

if __name__ == "__main__":
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

    clf = KNN(k=5)
    clf.fit(X_train, y_train)

    input_X = []  
    input_y = []  

    while True:
        plt.figure()
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolor='k', s=50, label="Données d'entraînement")

        # Saisie des valeurs pour prédiction
        input_values = []
        for i in range(X.shape[1]):
            value = float(input(f"Entrez la valeur pour la caractéristique {i + 1}: "))
            input_values.append(value)

        # Prédiction
        prediction = clf.predict([input_values])[0]
        print(f"Classe prédite : {prediction}")

        # Ajout des valeurs saisies aux listes
        input_X.append(input_values)
        input_y.append(prediction)

        # Convertir input_X en un tableau NumPy
        input_X_array = np.array(input_X)

        # Affichage des points saisis en rouge
        plt.scatter(input_X_array[:, 0], input_X_array[:, 1], c='red', marker='x', s=100, label="Saisie utilisateur")
        plt.xlabel("Longueur du sépale (cm)")
        plt.ylabel("Largeur du sépale (cm)")
        plt.title("Scatter Plot : Longueur du sépale vs. Largeur du sépale")
        plt.legend()
        plt.show()

"""
Longueur du sépale (sepal length) :
Exemple 1 : 5.1
Exemple 2 : 4.9
Exemple 3 : 6.0
Largeur du sépale (sepal width) :
Exemple 1 : 3.5
Exemple 2 : 3.0
Exemple 3 : 3.2
Longueur du pétale (petal length) :
Exemple 1 : 1.4
Exemple 2 : 1.5
Exemple 3 : 4.7
Largeur du pétale (petal width) :
Exemple 1 : 0.2
Exemple 2 : 0.1
Exemple 3 : 1.4
"""