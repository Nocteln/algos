tab = [5,2,4,8,2,46,2,-6] 

def insertion(tab):
    for i in range(1, len(tab)):
        cle = tab[i]
        j = i-1
        while j >= 0 and tab[j] > cle:  # tant que j est postif (donc qu'il reste des clef dans le tableau) & tab[j] est plus grand que le nombre a inserer
            tab[j+1] = tab[j] # on interverti les nombres
            j = j-1
        tab[j+1] = cle
    return tab
        

print(insertion(tab))