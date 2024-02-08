import random
tab = []
for k in range(40):
    tab.append(random.randint(0,100))

def selection(tab):
    for i in range(len(tab)-1): # On boucle sur le tableau mais en retirant 1 car on en a pas besoin
        min = i # Attribue min à i pour pouvoir en changer la valeur
        for j in range(i+1, len(tab)): # on boucle sur tous les éléments plus grand que notre i car ceux d'avant sont déjà trié. Cela nous permet de trouver l'élément le plus petit du tableau a partir de l'index i
            if tab[j] < tab[min]:  # on cherche si la valeur de tab[j] est plus petite que notre ancien minimum
                min = j # si c'est le cas on lui attribue la valeur 
        tab[i], tab[min] = tab[min], tab[i] # On interverti les valeurs
    return tab

print(selection(tab))